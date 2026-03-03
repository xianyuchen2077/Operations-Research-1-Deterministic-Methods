"""
Production Planning Optimization Main Program
"""

from io_openpyxl import readDataOpenpyxl, writeDataOpenpyxl
from model import formulateModel, solveModel, getOptimalSolution, getOptimalDualSolution, saveModel, readModel
import constant

def main():
    """
    Main function
    """

    #
    # Step 1: Read data from the Excel file
    #

    # Option 1) Use openpyxl
    productProfits, materialsPerUnit, materialLimitations, numberLimitations = readDataOpenpyxl()

    # print("Profit per unit:")
    # print(productProfits, "\n")

    # print('Materials used per unit produced:')
    # print(materialsPerUnit, "\n")

    # print('Material limitations:')
    # print(materialLimitations, "\n")

    # print('Number limitations:')
    # print(numberLimitations, "\n")

    # Formulate the LP model.
    model = formulateModel(productProfits, materialsPerUnit, materialLimitations, numberLimitations)

    # Option 2) Directly load the LP from the MPS or LP file.

    # model = readModel(constant.MPS_PATH)
    # model = readModel(constant.LP_PATH)

    #
    # Optional: Save the LP model to an LP or an MPS file.
    #

    # Save the model.
    saveModel(model, constant.MPS_PATH)
    saveModel(model, constant.LP_PATH)

    #
    # Step 2: Write the solution to the Excel file
    #

    solveModel(model)
    soln, objVal = getOptimalSolution(model)
    materialsUsed = {
        "Frame parts": {"Total": soln["Product1"] * materialsPerUnit["Frame parts"]["Product1"] + soln["Product2"] * materialsPerUnit["Frame parts"]["Product2"],"Product1": soln["Product1"] * materialsPerUnit["Frame parts"]["Product1"],"Product2": soln["Product2"] * materialsPerUnit["Frame parts"]["Product2"]},
        "Electrical components": {"Total": soln["Product1"] * materialsPerUnit["Electrical components"]["Product1"] + soln["Product2"] * materialsPerUnit["Electrical components"]["Product2"],"Product1": soln["Product1"] * materialsPerUnit["Electrical components"]["Product1"],"Product2": soln["Product2"] * materialsPerUnit["Electrical components"]["Product2"]}
    }
    profit = {
        "Total": objVal,
        "Product1": soln["Product1"]*productProfits["Product1"],
        "Product2": soln["Product2"]*productProfits["Product2"]
    }

    # print("Optimal solution:", soln)
    # print("Optimal objective value:", objVal)
    # print("Materials used:", materialsUsed)
    # print()

    #
    # Optional: Extract dual variables.
    #

    dualVariables = getOptimalDualSolution(model)

    #
    # Step 3: Write the solution to the Excel file
    #

    # Option 1) Use openpyxl
    writeDataOpenpyxl(soln, objVal, materialsUsed, profit)

if __name__ == "__main__":
    main()