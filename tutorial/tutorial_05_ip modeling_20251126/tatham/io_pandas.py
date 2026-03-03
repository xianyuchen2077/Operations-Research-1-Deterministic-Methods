"""
Reading from and writing to an Excel file using pandas.
"""

import pandas as pd

import constant


def readDataPandas() -> tuple[dict, dict, dict]:
    """
    Read data from an Excel file using pandas.

    Returns
    -------
    investmentCost : dict
        The investment cost for each investment.
        - Keys: investment index (1 to 7)
        - Values: investment cost
    npv : dict
        The NPV for each investment.
        - Keys: investment index (1 to 7)
        - Values: NPV
    budget : dict
        The budget available for investments.
        - Key: "Budget"
        - Values: budget amount
    """

    # Read data from the Input sheet
    data = pd.read_excel(constant.DATA_PATH, sheet_name=constant.SHEET_NAME, header=None)

    # Create dictionaries from the relevant rows and columns
    investmentCost = {}
    startRow = constant.INPUT_INVESTMENT_COST_START_ROW - 1
    startCol = constant.INPUT_INVESTMENT_COST_START_COL - 1
    for i, investmentName in enumerate(constant.INVESTMENT_NAMES):
        investmentCost[investmentName] = data.iloc[startRow, startCol + i]
    
    npv = {}
    startRow = constant.INPUT_NPV_START_ROW - 1
    startCol = constant.INPUT_NPV_START_COL - 1
    for i, investmentName in enumerate(constant.INVESTMENT_NAMES):
        npv[investmentName] = data.iloc[startRow, startCol + i]

    budget = {}
    budget[constant.BUDGET_NAME] = data.iloc[constant.INPUT_BUDGET_START_ROW - 1,
                                              constant.INPUT_BUDGET_START_COL - 1]

    return investmentCost, npv, budget


def writeDataPandas(soln, objVal) -> None:
    """
    Write the solution back to the original Excel sheet using pandas.

    Parameters
    ----------
    soln : dict
        The investment levels for each investment.
        - Keys: investment index (1 to 7)
        - Values: investment level (0 or 1)
    constrVal : float
        The total amount invested.
    objVal : float
        The total NPV achieved.
    """

    # Read data from the inputSheet.
    data = pd.read_excel(constant.DATA_PATH, sheet_name=constant.SHEET_NAME, header=None)

    # Write data to the output sheet
    startRow = constant.OUTPUT_INVESTMENT_LEVELS_START_ROW - 1
    startCol = constant.OUTPUT_INVESTMENT_LEVELS_START_COL - 1
    for i, investmentName in enumerate(constant.INVESTMENT_NAMES):
        data.iloc[startRow, startCol + i] = soln[investmentName]

    data.iloc[constant.OUTPUT_TOTAL_NPV_START_ROW - 1,
              constant.OUTPUT_TOTAL_NPV_START_COL - 1] = objVal

    # Save to Excel file.
    data.to_excel(constant.DATA_PATH, sheet_name=constant.SHEET_NAME, index=False, header=False)
