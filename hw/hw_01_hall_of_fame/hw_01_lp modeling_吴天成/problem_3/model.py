# -*- coding: utf-8 -*-

# model.py
import gurobipy as gp
from gurobipy import GRB
import constants

def create_and_solve_model(data):
    """
    根据数据创建并求解Gurobi模型
    """
    try:
        # 初始化模型
        model = gp.Model("WorldLight_Optimization")
        
        # 创建决策变量
        x1 = model.addVar(vtype=GRB.CONTINUOUS, name=constants.PRODUCT_NAMES[0])
        x2 = model.addVar(vtype=GRB.CONTINUOUS, name=constants.PRODUCT_NAMES[1])
        
        # 设置目标函数
        model.setObjective(
            data["profit"][0] * x1 + data["profit"][1] * x2,
            GRB.MAXIMIZE
        )
        
        # 添加约束
        # 1. 金属框架约束: x1 + 3*x2 <= 200
        model.addConstr(
            x1 + data["resource_usage"][0][1] * x2 <= data["resource_avail"][0],
            "Frame_Parts"
        )
        
        # 2. 电子元件约束: 2*x1 + 2*x2 <= 300
        model.addConstr(
            data["resource_usage"][1][0] * x1 + data["resource_usage"][1][1] * x2 <= data["resource_avail"][1],
            "Electrical_Components"
        )
        
        # 3. 产品2产量上限: x2 <= 60
        model.addConstr(x2 <= data["max_product2"], "Max_Product2")
        
        # 可选：保存模型文件（用于调试）
        model.write(constants.LP_PATH)
        model.write(constants.MPS_PATH)
        print(f"模型已保存为: {constants.LP_PATH} 和 {constants.MPS_PATH}")
        
        # 求解模型
        model.optimize()
        
        # 检查并返回结果
        if model.status == GRB.OPTIMAL:
            solution = {
                'product1': x1.x,
                'product2': x2.x,
                'optimal_profit': model.objVal,
                'profit_coef': data["profit"]
            }
            print("模型求解成功!")
            return solution
        else:
            raise Exception(f"未找到最优解。求解状态: {model.status}")
            
    except Exception as e:
        print(f"模型求解错误: {e}")
        return None
