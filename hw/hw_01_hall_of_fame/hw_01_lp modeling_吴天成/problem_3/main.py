# -*- coding: utf-8 -*-

# main.py
from io_openpyxl import read_data_openpyxl, write_solution_openpyxl
from io_pandas import read_data_pandas, write_solution_pandas
from model import create_and_solve_model
import constants
import os

def main():
    """
    主程序：可以选择使用openpyxl或pandas进行数据读写
    """
    print("WorldLight公司优化问题求解\n")
    
    # 让用户选择IO方法
    print("请选择数据读写方法:")
    print("1. 使用 openpyxl")
    print("2. 使用 pandas")
    
    choice = input("请输入选择 (1 或 2): ").strip()
    
    if choice == "1":
        read_data_func = read_data_openpyxl
        write_solution_func = write_solution_openpyxl
        method_name = "openpyxl"
    elif choice == "2":
        read_data_func = read_data_pandas
        write_solution_func = write_solution_pandas
        method_name = "pandas"
    else:
        print("无效选择，默认使用 openpyxl")
        read_data_func = read_data_openpyxl
        write_solution_func = write_solution_openpyxl
        method_name = "openpyxl"
    
    print(f"\n使用 {method_name} 方法进行数据读写...")
    
    try:
        # 1. 从Excel读取数据
        print("正在从Excel文件读取数据...")
        model_data = read_data_func()
        if model_data is None:
            return
        
        # 2. 创建并求解模型
        print("正在创建和求解优化模型...")
        solution = create_and_solve_model(model_data)
        if solution is None:
            return
        
        # 3. 打印结果到控制台
        print("\n=== 最优解决方案 ===")
        print(f"{constants.PRODUCT_NAMES[0]}产量: {solution['product1']:.2f} 单位")
        print(f"{constants.PRODUCT_NAMES[1]}产量: {solution['product2']:.2f} 单位")
        print(f"最大利润: ${solution['optimal_profit']:.2f}")
        
        # 4. 将结果写回Excel
        success = write_solution_func(solution)
        if success:
            print(f"任务完成！结果已写入 {constants.DATA_PATH} 的 '{constants.MODEL_NAME}' 工作表中")
        else:
            print("结果写入失败")
        
    except Exception as e:
        print(f"程序执行错误: {e}")

if __name__ == "__main__":
    main()
