#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2025/10/6 22:06
# @Author: TJY

"""
WorldLight Company Planning Optimization Main Program
"""

from io_openpyxl import readDataOpenpyxl, writeDataOpenpyxl
from model import formulateModel, solveModel, getOptimalSolution, getOptimalDualSolution, saveModel, readModel

import constant

def main():
    """
    Main function
    """

    #
    # Step 1: Formulate the LP model.
    #


    # Read data.
    productProfits, resourceProductUnits , resourceAvailableUnits,product2QuantityLimit = readDataOpenpyxl()

    # Formulate the LP model.
    model = formulateModel(productProfits, resourceProductUnits , resourceAvailableUnits,product2QuantityLimit)


    #
    # Step 2: Solve the LP model.
    #

    solveModel(model)
    soln, objVal = getOptimalSolution(model)

    #
    # Optional: Extract dual variables.
    #

    # dualVariables = getOptimalDualSolution(model)

    #
    # Step 3: Write the solution to the Excel file.
    #

    # Option 1) Use openpyxl
    writeDataOpenpyxl(soln, objVal)



if __name__ == "__main__":
    main()



