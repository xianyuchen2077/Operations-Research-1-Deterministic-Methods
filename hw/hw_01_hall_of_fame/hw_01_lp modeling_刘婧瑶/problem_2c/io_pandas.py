"""
Reading from and writing to an Excel file using pandas.
"""

import pandas as pd
import constant


def readDataPandas() -> tuple[dict, dict, dict]:
    """
    Read production planning data from an Excel file using pandas.

    Returns
    -------
    productProfits : dict
        The profit per batch for each product.
    plantProductHours : nested dict
        The hours required to produce one batch of each product at each plant.
    plantAvailableHours : dict
        The available hours at each plant.
    """

    # Read data from the inputSheet.
    data = pd.read_excel(constant.DATA_PATH, sheet_name=constant.SHEET_NAME, header=None)

    # Create dictionaries based on start coordinates and list lengths.
    productProfits = {}
    startRow = constant.INPUT_PROFIT_START_ROW - 1
    startCol = constant.INPUT_PROFIT_START_COL - 1
    for j, productName in enumerate(constant.PRODUCT_NAMES):
        profitValue = data.iloc[startRow, startCol + j]
        productProfits[productName] = profitValue

    plantAvailableHours = {}
    startRow = constant.INPUT_HOURS_AVAILABLE_START_ROW - 1
    startCol = constant.INPUT_HOURS_AVAILABLE_START_COL - 1
    for i, plantName in enumerate(constant.PLANT_NAMES):
        hours = data.iloc[startRow + i, startCol]
        plantAvailableHours[plantName] = hours

    plantProductHours = {}
    startRow = constant.INPUT_HOURS_START_ROW - 1
    startCol = constant.INPUT_HOURS_START_COL - 1
    for i, plantName in enumerate(constant.PLANT_NAMES):
        hoursPerProduct = {}
        for j, productName in enumerate(constant.PRODUCT_NAMES):
            hours = data.iloc[startRow + i, startCol + j]
            hoursPerProduct[productName] = hours
        plantProductHours[plantName] = hoursPerProduct

    return productProfits, plantProductHours, plantAvailableHours


def writeDataPandas(soln, objVal) -> None:
    """
    Write the solution back to the original Excel sheet using pandas.

    Parameters
    ----------
    soln : dict
        The optimal solutions (key is the full variable name).
    objVal : float
        The optimal objective function value.
    """
    # Read data from the inputSheet.
        # 读取原始数据（保持Data工作表不变）
    original_data = pd.read_excel(constant.DATA_PATH, sheet_name=constant.SHEET_NAME, header=None)
    
    # 创建解决方案数据框
    solution_data = pd.DataFrame({
        '': ['Units Produced'],
        'Product 1': [soln['Product 1']],
        'Product 2': [soln['Product 2']],
        '': [''],
        'Total Profit': [objVal]
    })
    
    # 使用ExcelWriter来写入多个工作表
    with pd.ExcelWriter(constant.DATA_PATH, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        # 删除已存在的解决方案工作表（如果存在）
        if constant.SOLUTION_SHEET_NAME in writer.book.sheetnames:
            idx = writer.book.sheetnames.index(constant.SOLUTION_SHEET_NAME)
            writer.book.remove(writer.book.worksheets[idx])
        
        # 写入解决方案到新工作表
        solution_data.to_excel(writer, sheet_name=constant.SOLUTION_SHEET_NAME, index=False, header=True)
    
    print(f"解决方案已写入工作表: {constant.SOLUTION_SHEET_NAME}")
