"""
State University Optimization Main Program
"""

from io_openpyxl import readDataOpenpyxl, writeDataOpenpyxl
from model import formulateModel, solveModel, getOptimalSolution
def main():
    """
    Main function
    """

    #
    # Step 1: Formulate the IP model.
    #

    # Read data
    computerCost, deliveryCost, maxQuantity, minQuantity, totalDemand = readDataOpenpyxl()

    # Formulate the IP model
    model = formulateModel(computerCost, deliveryCost, maxQuantity, minQuantity, totalDemand)


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