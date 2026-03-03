"""
Tatham Investment Optimization Main Program
"""

from io_openpyxl import readDataOpenpyxl, writeDataOpenpyxl
import constant
from model import formulateModel, solveModel, getOptimalSolution, readModel, saveModel


def main():
    """
    Main function
    """

    #
    # Step 1: Formulate the IP model.
    #

    # Read data
    unit_Price, delivery_Charge, max_purchase_quantity, min_purchase_quantity, planned_computer_Number = readDataOpenpyxl()

    # Formulate the IP model
    model = formulateModel(unit_Price, delivery_Charge, max_purchase_quantity, min_purchase_quantity, planned_computer_Number)

    # Optional: Save the IP model to an LP or an MPS file.

    saveModel(model, constant.LP_PATH)
    saveModel(model, constant.MPS_PATH)

    #
    # Step 2: Solve the IP model.
    #

    solveModel(model)
    soln, objVal = getOptimalSolution(model)

    #
    # Step 3: Write the solution to the Excel file.
    #

    writeDataOpenpyxl(soln, objVal)


if __name__ == "__main__":
    main()