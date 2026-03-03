"""
Formulate and solve the Tatham Example using Gurobi.
"""

import gurobipy as grb

import constant


def formulateModel(unit_Price, delivery_Charge, max_purchase_quantity, min_purchase_quantity, planned_computer_Number) -> grb.Model:
    """
    Formulate a Gurobi model based on the given instance data.

    Parameters
    ----------
    unit_Price : dict
        The unit price for each vendor.
        - Keys: vendor name
        - Values: unit price
    delivery_Charge : dict
        The delivery charge for each vendor.
        - Keys: vendor name
        - Values: delivery charge
    max_purchase_quantity : dict
        The maximum quantity each vendor can supply.
        - Keys: vendor name
        - Values: maximum quantity
    min_purchase_quantity : dict
        The minimum required purchase quantity for each vendor.
        - Keys: vendor name
        - Values: minimum quantity
    planned_computer_Number : dict
        The total number of computers planned to purchase.
        - Key: "total_number_of_computers_planned_to_purchase"
        - Values: planned number
    Returns
    -------
    model : grb.Model
        The formulated Gurobi model.
    """

    # Create a new model
    model = grb.Model(constant.MODEL_NAME)

    # Define decision variables
    # Pay attention to the change in variable type: BINARY rather than CONTINUOUS
    purchaseDecisions = {}
    for vendorName in constant.VENDOR_NAMES:
        purchaseDecisions[vendorName] = model.addVar(vtype=grb.GRB.BINARY, name="whether_purchase_from_" + vendorName)

    purchase_Numbers = {}
    for vendorName in constant.VENDOR_NAMES:
        purchase_Numbers[vendorName] = model.addVar(vtype=grb.GRB.CONTINUOUS, name="Number_purchased_from_" + vendorName)

    # Define the objective function
    objExpr = grb.LinExpr()
    for vendorName in constant.VENDOR_NAMES:
        objExpr += purchaseDecisions[vendorName] * (purchase_Numbers[vendorName] * float(unit_Price[vendorName]) + float(delivery_Charge[vendorName]))
    model.setObjective(objExpr, grb.GRB.MINIMIZE)

    # Define the number constraint
    lhsExpr = grb.LinExpr()
    for vendorName in constant.VENDOR_NAMES:
        currentPurchaseNumber = purchase_Numbers[vendorName]
        maxQuantity = max_purchase_quantity[vendorName]
        minQuantity = min_purchase_quantity[vendorName]
        purchaseDecision = purchaseDecisions[vendorName]
        model.addConstr(currentPurchaseNumber >= 0, name="nonnegative_purchase_number_from_" + vendorName)
        model.addConstr(currentPurchaseNumber >= purchaseDecision*minQuantity, name="min_purchase_quantity_from_" + vendorName)
        model.addConstr(currentPurchaseNumber <= purchaseDecision*maxQuantity, name="max_purchase_quantity_from_" + vendorName)

        lhsExpr += currentPurchaseNumber
    model.addConstr(lhsExpr == float(planned_computer_Number[constant.PLANNED_COMPUTER_NUMBER]), name=constant.PLANNED_COMPUTER_NUMBER)
    # Return the model
    return model


def solveModel(model) -> None:
    """
    Optimize the given Gurobi model.

    Parameters
    ----------
    model : gurobipy.Model
        The Gurobi model to be optimized

    """
    model.optimize()


def getOptimalSolution(model) -> tuple[dict[str, float], float]:
    """
    Get the optimal solution and objective value of the optimized Gurobi model.

    Parameters
    ----------
    model : gurobipy.Model
        The Gurobi model to be optimized

    Returns
    -------
    tuple
        A tuple (soln, objVal) where:
        soln : dict[str, float]
            The optimal solutions
            - Keys: variable names
            - Values: optimal decision variable values
        objVal : float
            The optimal objective function value
    """
    soln = {}
    for var in model.getVars():
        soln[var.VarName] = var.X

    objVal = model.objVal

    # Print the optimal solutions and objective function value.
    print("\nThe optimal solutions:")
    for varName, varValue in soln.items():
        print(f"    {varName}: {varValue}")

    print(f"The optimal objective function value: {objVal}\n")

    return soln, objVal


def readModel(filePath) -> grb.Model:
    """
    Load a Gurobi model from a MPS or LP file.

    Parameters
    ----------
    filePath : str
        The path to the file to load the model from

    Returns
    -------
    model : gurobipy.Model
        The loaded Gurobi model
    """
    model = grb.read(filePath)

    return model


def saveModel(model, filePath) -> None:
    """
    Save the given Gurobi model to a file, either in MPS or LP format.

    Parameters
    ----------
    model : gurobipy.Model
        The Gurobi model to be saved
    filePath : str
        The path to the file to save the model to
    """
    model.write(filePath)
