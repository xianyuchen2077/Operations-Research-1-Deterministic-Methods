"""
Constants definition module
"""

# Data file path and worksheet name
DATA_PATH = "../problem_2b.xlsx"
SHEET_NAME = "Solution_Gurobi"

LP_PATH = "./instance/problem_2c.lp"
MPS_PATH = "./instance/problem_2c.mps"

# Profit per unit data location (Product 1& Product 2)
INPUT_PROFIT_START_ROW = 4
INPUT_PROFIT_START_COL = 2

# Materials used per unit produced data location (2 materials)
INPUT_MATERIALS_START_ROW = 7
INPUT_MATERIALS_START_COL = 2

# Materials available data location (2 materials)
INPUT_MATERIALS_AVAILABLE_START_ROW = 7
INPUT_MATERIALS_AVAILABLE_START_COL = 6

# Output result location
OUTPUT_UNITS_PRODUCED_START_ROW = 11
OUTPUT_UNITS_PRODUCED_START_COL = 2

OUTPUT_PROFIT_START_ROW = 11
OUTPUT_PROFIT_START_COL = 6

# Product names list
PRODUCT_NAMES = ["Product_1", "Product_2"]

# Materials names list
MATERIAL_NAMES = ["Frame_parts", "Electrical_components"]

# Model name
MODEL_NAME = "Problem_2c"