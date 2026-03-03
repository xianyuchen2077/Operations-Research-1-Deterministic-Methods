"""
Formulate and solve the Tatham Example using Gurobi.
"""

import gurobipy as grb

import constant


def formulateModel(investmentCost, npv, budget) -> grb.Model:
    """
    Formulate a Gurobi model based on the given instance data.

    Parameters
    ----------
    investmentCost : dict
        The investment cost for each investment.
        - Keys: investment index
        - Values: investment cost
    npv : dict
        The NPV for each investment.
        - Keys: investment index
        - Values: NPV
    budget : dict
        The budget available for investments.
        - Key: "Budget"
        - Values: budget amount

    Returns
    -------
    model : grb.Model
        The formulated Gurobi model.
    """

    # Create a new model
    model = grb.Model(constant.MODEL_NAME)

    # Define decision variables
    # Pay attention to the change in variable type: BINARY rather than CONTINUOUS
    investmentDecisions = {}    
    for investmentName in constant.INVESTMENT_NAMES:
        investmentDecisions[investmentName] = model.addVar(vtype=grb.GRB.BINARY, 
                                                           name=investmentName)

    # Define the objective function
    objExpr = grb.LinExpr()
    for investmentName in constant.INVESTMENT_NAMES:
        objExpr += npv[investmentName] * investmentDecisions[investmentName]
    model.setObjective(objExpr, grb.GRB.MAXIMIZE)

    # Define the budget constraint
    lhsExpr = grb.LinExpr()
    for investmentName in constant.INVESTMENT_NAMES:
        lhsExpr += investmentCost[investmentName] * investmentDecisions[investmentName]
    model.addConstr(lhsExpr <= budget[constant.BUDGET_NAME], name=constant.BUDGET_NAME)

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
