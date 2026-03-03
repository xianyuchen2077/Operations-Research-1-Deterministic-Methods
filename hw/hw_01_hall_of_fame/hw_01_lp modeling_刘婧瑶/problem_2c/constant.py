"""
Constants
"""

# Data file path and worksheet name
DATA_PATH = "./data/problem_2c_data.xlsx"
SHEET_NAME = "Data"

SOLUTION_SHEET_NAME = "Solution_Gurobi"


LP_PATH = "./instance/wyndor.lp"
MPS_PATH = "./instance/wyndor.mps"

# Profit per batch data location (Doors & Windows)
INPUT_PROFIT_START_ROW = 3
INPUT_PROFIT_START_COL = 2

# Hours used per batch produced data location (3 plants)
INPUT_HOURS_START_ROW = 6
INPUT_HOURS_START_COL = 2

# Hours available data location (3 plants)
INPUT_HOURS_AVAILABLE_START_ROW = 6
INPUT_HOURS_AVAILABLE_START_COL = 6

# Output result location
OUTPUT_BATCHES_PRODUCED_START_ROW = 2
OUTPUT_BATCHES_PRODUCED_START_COL = 2

OUTPUT_PROFIT_START_ROW = 2
OUTPUT_PROFIT_START_COL = 5

# Product names list
PRODUCT_NAMES = ["Product 1", "Product 2"]

# Plant names list
PLANT_NAMES = ["Frame part", "Electrical component", "Product 2 limit"]

# Model name
MODEL_NAME = "WorldLight"
