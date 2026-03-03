"""
Constants
"""

# Data file path and worksheet name
DATA_PATH = "./data/world_light.xlsx"
SHEET_NAME = "Solution_Gurobi"

LP_PATH = "./instance/world_light.lp"
MPS_PATH = "./instance/world_light.mps"

# Profit per product (product1 & product2)
INPUT_PROFIT_START_ROW = 4
INPUT_PROFIT_START_COL = 2

# Frame parts/Electrical components used per product
INPUT_START_ROW = 7
INPUT_START_COL = 2

# Frame parts/Electrical components available data location
INPUT_AVAILABLE_START_ROW = 7
INPUT_AVAILABLE_START_COL = 6

# Output result location
OUTPUT_BATCHES_PRODUCED_START_ROW = 11
OUTPUT_BATCHES_PRODUCED_START_COL = 2

OUTPUT_PROFIT_START_ROW = 11
OUTPUT_PROFIT_START_COL = 6

# Product names list
PRODUCT_NAMES = ["Product1", "Product2"]

# Components names list
COMPONENTS_NAMES = ["Frame_parts", "Electrical_components"]

# Model name
MODEL_NAME = "World_Light"
