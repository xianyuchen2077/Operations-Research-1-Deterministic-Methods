"""
Formulate and solve the problem using Gurobi.
"""

import gurobipy as grb

import constant


def formulateModel(productProfits, companyProductMaterials,  companyAvailableMaterials) -> grb.Model:
    """
    Formulate a Gurobi model based on the given instance data.

    Parameters
    ----------
    productProfits : dict
        The profit per batch for each product
        - Keys: product names (`Product 1`, `Product 2`)
        - Values: profit per unit
    companyProductMaterials : nested dict
        The materials required to produce one unit of each product
        - Keys: material names (`Frame parts`, `Electrical components`)
        - Values: dict
            - Keys: product names (`Product 1`, `Product 2`)
            - Values: materials required
    companyAvailableMaterials : dict
        The available materials on the company
        - Keys: material names (`Frame parts`, `Electrical components`)
        - Values: available materials
    Returns
    -------
    model : gurobipy.Model
        The formulated Gurobi model
    """

    # Create a Gurobi model.
    model = grb.Model(constant.MODEL_NAME)

    # Define decision variables.
    unitProductionDecisions = {}
    for product, profit in productProfits.items():
        unitProductionDecisions[product] = model.addVar(lb=0.0,
                                                         ub=grb.GRB.INFINITY,
                                                         vtype=grb.GRB.CONTINUOUS,
                                                         name=f"{product}")
    # 添加Product_2的数量不超过29的约束
    if "Product_2" in unitProductionDecisions:
        model.addConstr(
            unitProductionDecisions["Product_2"] <= 20,
            name="Product_2_Max_Limit"
        )

    # Define the objective function.
    objExpr = grb.LinExpr()
    for product, profit in productProfits.items():
        objExpr += profit * unitProductionDecisions[product]
    model.setObjective(objExpr, grb.GRB.MAXIMIZE)

    # Define the constraints.
    for material, availableMaterial in companyAvailableMaterials.items():
        # For each material, the total used units <= the available material.
        lhsExpr = grb.LinExpr()
        for product, material in companyProductMaterials[material].items():
            lhsExpr += material * unitProductionDecisions[product]

        model.addConstr(lhsExpr <= availableMaterial, f"{material}")

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


def getOptimalSolution(model) -> dict[str, float]:
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

    print(f"The optimal objective function value: {objVal}\n")

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
