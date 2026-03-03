"""
Constants definition module
"""

# Data file path and worksheet name
DATA_PATH = "./problem_1b.xlsx"
SHEET_NAME_READ = "Solution_Solver"
SHEET_NAME_WRITE = "Solution_Gurobi"

LP_PATH = "./problem_1c/instance/production_planning.lp"
MPS_PATH = "./problem_1c/instance/production_planning.mps"

# Number of products input location (Product1 & Product2)
INPUT_PRODUCTS_ROW = 2
INPUT_PRODUCTS_START_COL = 2

# Number of products output location (Product1 & Product2)
OUTPUT_PRODUCTS_ROW = 3
OUTPUT_PRODUCTS_START_COL = 2

# Profit per unit data location (Product1 & Product2)
INPUT_PROFIT_ROW = 3
INPUT_PROFIT_START_COL = 2

# Total profit output location
OUTPUT_TOTAL_PROFIT_ROW = 6
OUTPUT_TOTAL_PROFIT_COL = 4

# Materials used per unit produced data location
INPUT_MATERIALS_START_ROW = 7
INPUT_MATERIALS_START_COL = 2

# Materials limitations data location
INPUT_MATERIAL_LIMITATIONS_START_ROW = 10
INPUT_MATERIAL_LIMITATIONS_COL = 4

# Number limitations data location
INPUT_NUMBER_LIMITATIONS_START_ROW = 12
INPUT_NUMBER_LIMITATIONS_END_ROW = 14
INPUT_NUMBER_LIMITATIONS_NAME_COL = 1
INPUT_NUMBER_LIMITATIONS_OPERATOR_COL = 3
INPUT_NUMBER_LIMITATIONS_COL = 4

# Materials used in total output location
OUTPUT_MATERIALS_TOTAL_START_ROW = 4
OUTPUT_MATERIALS_TOTAL_COL = 4

# Number of products constraints output location
OUTPUT_CONSTRAINTS_START_ROW = 12
OUTPUT_CONSTRAINTS_COL = 2

# Product names list
PRODUCT_NAMES = ["Product1", "Product2"]

# Material names list
MATERIAL_NAMES = ["Frame parts", "Electrical components"]

# Constraint names list
CONSTRAINT_NAMES = [
    "Frame parts used in total",
    "Electrical components used in total",
    "Number of product2",
    "Number of product1",
    "Number of product2"
]

# Model name
MODEL_NAME = "Production Planning"