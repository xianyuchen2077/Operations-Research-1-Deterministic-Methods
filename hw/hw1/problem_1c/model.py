"""
Formulate and solve the Wyndor Example using Gurobi.
"""

import gurobipy as grb

import constant


def formulateModel(productProfits, materialsPerUnit, materialLimitations, numberLimitations) -> grb.Model:
    """
    Formulate a Gurobi model based on the given instance data.

    Parameters
    ----------
    productProfits : dict
        The profit per unit for each product
        - Keys: product names (`Product1`, `Product2`)
        - Values: profit per unit
    materialsPerUnit : nested dict
        The materials required to produce one unit of each product
        - Keys: material names (`Frame parts`, `Electrical components`)
        - Values: dict
            - Keys: product names (`Product1`, `Product2`)
            - Values: materials required
    materialLimitations : dict
        The material limitations
        - Keys: material names (`Frame parts`, `Electrical components`)
        - Values: available materials
    numberLimitations : dict
        The number limitations
        - Keys: product names (`Product1`, `Product2` and `max`, `min`)
        - Values: available products

    Returns
    -------
    model : gurobipy.Model
        The formulated Gurobi model
    """

    # Create a Gurobi model.
    model = grb.Model(constant.MODEL_NAME)

    # Define decision variables.
    batchProductionDecisions = {}
    for product, profit in productProfits.items():
        batchProductionDecisions[product] = model.addVar(lb=0.0,
                                                        ub=grb.GRB.INFINITY,
                                                        vtype=grb.GRB.CONTINUOUS,
                                                        name=f"{product}")

    # Define the objective function.
    objExpr = grb.LinExpr()
    for product, profit in productProfits.items():
        objExpr += profit * batchProductionDecisions[product]
    model.setObjective(objExpr, grb.GRB.MAXIMIZE)

    # Define the constraints.
    for material, availableAmount in materialLimitations.items():
        # For each material, the total used <= the available amount.
        lhsExpr = grb.LinExpr()
        for product, amount in materialsPerUnit[material].items():
            lhsExpr += amount * batchProductionDecisions[product]
        model.addConstr(lhsExpr <= availableAmount, f"{material}")
    for product, limitations in numberLimitations.items():
        if "max" in limitations:
            model.addConstr(batchProductionDecisions[product] <= limitations["max"], f"{product}_max")
        if "min" in limitations:
            model.addConstr(batchProductionDecisions[product] >= limitations["min"], f"{product}_min")

    # Return the model.
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
    Get the optimal solution of the (optimized) Gurobi model.

    Parameters
    ----------
    model : gurobipy.Model
        The Gurobi model to be optimized

    Returns
    -------
    soln : dict
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

    print(f"\nThe optimal objective function value: {objVal}\n")

    return soln, objVal


def getOptimalDualSolution(model, constrNames=None) -> dict[str, float]:
    """
    Get the optimal dual variable values of a given set of constraints.

    Parameters
    ----------
    model : gurobipy.Model
        The Gurobi model to extract the optimal dual variable values from
    constrNames : str or list of str, optional
        The names of the constraints to extract the optimal dual variable values from
        - If None, extract for all constraints
        - If a string, extract for the specified constraint
        - If a list of strings, extract for the specified set of constraints

    Returns
    -------
    duals : dict
        The optimal dual variable values of the specified constraints
        - Keys: constraint names
        - Values: optimal dual variable values
    """

    duals = {}

    if constrNames is None:
        constrs = model.getConstrs()

        for constr in constrs:
            duals[constr.constrName] = constr.pi
            print(f"{constr.constrName}: Optimal dual variable value = {constr.pi}")

        return duals

    if isinstance(constrNames, str):
        constrNames = [constrNames]

    if not isinstance(constrNames, list):
        raise ValueError("constrNames must be a string or a list of strings")

    for constrName in constrNames:
        constr = model.getConstrByName(constrName)
        if constr is not None:
            duals[constrName] = constr.pi
            print(f"Constr {constrName}: Optimal dual variable value = {constr.pi}")
        else:
            duals[constrName] = None
            print(f"{constrName}: Not found")

    return duals


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
