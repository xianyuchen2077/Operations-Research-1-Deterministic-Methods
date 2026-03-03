import gurobipy as grb

def formulateModel(data_dict):
    """
    构建医疗团队分配的整数规划模型
    data_dict 格式: {国家名: [收益0, 收益1, 收益2, 收益3, 收益4, 收益5]}
    """
    model = grb.Model("Medical_Allocation")

    countries = list(data_dict.keys())
    team_options = range(6) # 0~5

    # 1.定义变量:x[country, teams]为二进制变量
    x = model.addVars(countries, team_options, vtype=grb.GRB.BINARY, name="x")

    # 2.设置目标函数:最大化总收益
    model.setObjective(
        grb.quicksum(data_dict[c][j] * x[c, j] for c in countries for j in team_options),
        grb.GRB.MAXIMIZE
    )

    # 3.添加约束
    # 约束1:每个国家必须且只能选择一种分配方案
    for c in countries:
        model.addConstr(grb.quicksum(x[c, j] for j in team_options) == 1, name=f"one_choice_{c}")

    # 约束2:分配队伍总数不超过5
    model.addConstr(
        grb.quicksum(j * x[c, j] for c in countries for j in team_options) <= 5,
        name="total_teams_limit"
    )

    return model, x