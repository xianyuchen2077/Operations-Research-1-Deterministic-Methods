"""
Tatham Investment Optimization Main Program
"""

from io_openpyxl import readDataOpenpyxl, writeDataOpenpyxl
from io_pandas import readDataPandas, writeDataPandas
from model import formulateModel, solveModel, getOptimalSolution, readModel, saveModel


def main():
    """
    Main function
    """

    #
    # Step 1: Formulate the IP model.
    #

    # Option 1) Read data from the Excel file using openpyxl, then formulate the IP model.

    # Read data
    investmentCost, npv, budget = readDataOpenpyxl()

    # Formulate the IP model
    model = formulateModel(investmentCost, npv, budget)

    # Option 2) Read data from the Excel file using pandas, then formulate the IP model.

    # Read data
    # investmentCost, npv, budget = readDataPandas()

    # Formulate the IP model
    # model = formulateModel(investmentCost, npv, budget)

    # Option 3) Directly load the IP from the MPS or LP file.

    # model = readModel(constant.MPS_PATH)
    # model = readModel(constant.LP_PATH)

    #
    # Optional: Save the IP model to an LP or an MPS file.

    # saveModel(model, constant.LP_PATH)
    # saveModel(model, constant.MPS_PATH)

    #
    # Step 2: Solve the IP model.
    #

    solveModel(model)
    soln, objVal = getOptimalSolution(model)

    #
    # Step 3: Write the solution to the Excel file.
    #

    # Option 1) Use openpyxl
    writeDataOpenpyxl(soln, objVal)

    # Option 2) Use pandas
    # writeDataPandas(soln, objVal)


if __name__ == "__main__":
    main()