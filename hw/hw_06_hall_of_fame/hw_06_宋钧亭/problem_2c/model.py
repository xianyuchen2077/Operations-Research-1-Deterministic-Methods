"""
Formulate and solve the State University Example using Gurobi.
"""

import gurobipy as grb

import constant


def formulateModel(computerCost, deliveryCost, maxQuantity, minQuantity, totalDemand) -> grb.Model:
    """
    Formulate a Gurobi model based on the given instance data.

    Parameters
    ----------
    computerCost: dict
        The cost per computer for each vendor.
        - Keys: vendor index
        - Values: computer cost
    deliveryCost: dict
        The cost of delivery for each vendor.
        - Keys: vendor index
        - Values: delivery cost
    maxQuantity: dict
        The maximum quantity to be ordered for each vendor.
        - Keys: vendor index
        - Values: maximum quantity
    minQuantity: dict
        The minimum quantity to be ordered for each vendor.
        - Keys: vendor index
        - Values: minimum quantity
    totalDemand: int
        The total demand for state university

    Returns
    -------
    model : grb.Model
        The formulated Gurobi model.
    """

    # Create a new model
    model = grb.Model(constant.MODEL_NAME)

    # Define decision variables
    # Pay attention to the change in variable type: BINARY rather than CONTINUOUS
    selectDecisions = {}
    for vendorName in constant.VENDOR_NAMES:
        varName = f"{constant.WHETHER_TO_ORDER_NAME}[{vendorName}]"
        selectDecisions[vendorName] = model.addVar(vtype=grb.GRB.BINARY,
                                                           name=varName)

    orderDecisions = {}
    for vendorName in constant.VENDOR_NAMES:
        varName = f"{constant.QUANTITY_TO_ORDER_NAME}[{vendorName}]"
        orderDecisions[vendorName] = model.addVar(vtype=grb.GRB.INTEGER,
                                                  name=varName)

    # Define the objective function
    objExpr = grb.LinExpr()
    for vendorName in constant.VENDOR_NAMES:
        objExpr += computerCost[vendorName] * orderDecisions[vendorName]+deliveryCost[vendorName]*selectDecisions[vendorName]
    model.setObjective(objExpr, grb.GRB.MINIMIZE)

    # Define the constraint
    lhsExpr1 = grb.LinExpr()
    for vendorName in constant.VENDOR_NAMES:
        lhsExpr1 += orderDecisions[vendorName]
    model.addConstr(lhsExpr1 == totalDemand, name=constant.TOTAL_DEMAND_NAME)

    for vendorName in constant.VENDOR_NAMES:
        model.addConstr(orderDecisions[vendorName] <= maxQuantity[vendorName]*selectDecisions[vendorName], name=f"{constant.MAX_QUANTITY_NAME}[{vendorName}]")

    for vendorName in constant.VENDOR_NAMES:
        model.addConstr(orderDecisions[vendorName]>=minQuantity[vendorName]*selectDecisions[vendorName], name=f"{constant.MIN_QUANTITY_NAME}[{vendorName}]")

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


def getOptimalSolution(model) -> dict[str, float]:
    """
    Get the optimal solution and objective value of the optimized Gurobi model.

    Parameters
    ----------
    model : gurobipy.Model
        The Gurobi model to be optimized

    Returns
    -------
   soln : dict
        The selection of ordering or not and the quantity of ordering
        - Keys: whether to order[investment index] or quantity to order[investment index]
        - Values:  (0 or 1) or int
    objVal : int
        The total cost.
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