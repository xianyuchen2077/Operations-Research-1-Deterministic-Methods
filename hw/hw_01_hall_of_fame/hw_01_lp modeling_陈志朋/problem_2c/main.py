"""
WorldLight Company Production Planning Optimization Main Program
"""

from io_openpyxl import readDataOpenpyxl, writeDataOpenpyxl
#from io_pandas import readDataPandas, writeDataPandas
from model import formulateModel, solveModel, getOptimalSolution, getOptimalDualSolution, saveModel, readModel

import constant


def main():
    """
    Main function
    """

    #
    # Step 1: Formulate the LP model.
    #

    # Read data from the Excel file using openpyxl, then formulate the LP model.

    # Read data.
    productProfits, componentsProductNeeded, componentsAvailable = readDataOpenpyxl()

    # Formulate the LP model.
    model = formulateModel(productProfits, componentsProductNeeded, componentsAvailable)

    # Save the model.
    saveModel(model, constant.MPS_PATH)
    saveModel(model, constant.LP_PATH)

    #
    # Step 2: Solve the LP model.
    #

    solveModel(model)
    soln, objVal = getOptimalSolution(model)

    #
    # Step 3: Write the solution to the Excel file.
    #

    # Use openpyxl
    writeDataOpenpyxl(soln, objVal)


if __name__ == "__main__":
    main()
