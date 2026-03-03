from model import formulateModel
import gurobipy as grb

def main():
    data = {
        "Country1": [0, 45, 70, 90, 105, 120],
        "Country2": [0, 20, 45, 75, 110, 150],
        "Country3": [0, 50, 70, 80, 100, 130]
    }

    # 构建模型
    model, x = formulateModel(data)

    # 求解
    model.optimize()

    # 输出
    print("\nOptimal Allocation Results:")
    print("-" * 50)
    if model.status == grb.GRB.OPTIMAL:
        total_assigned = 0
        for c in data.keys():
            for j in range(6):
                if x[c, j].X == 1:
                    print(f"{c} is allocated {j} teams (Gain: {data[c][j]})")
                    total_assigned += j
        print("-" * 50)
        print(f"Total teams used: {total_assigned}")
        print("-" * 50)
        print(f"Optimal Total Effectiveness: {model.ObjVal} additional person-years")

if __name__ == "__main__":
    main()