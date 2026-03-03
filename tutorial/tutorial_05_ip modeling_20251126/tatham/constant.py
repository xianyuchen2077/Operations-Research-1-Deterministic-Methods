"""
Constants
"""

# Data file path and worksheet name
DATA_PATH = "./data/tatham.xlsx"
SHEET_NAME = "Data"

LP_PATH = "./instance/tatham.lp"
MPS_PATH = "./instance/tatham.mps"

# Investment cost data location (7 investments)
INPUT_INVESTMENT_COST_START_ROW = 5
INPUT_INVESTMENT_COST_START_COL = 2

# NPV data location (7 investments)
INPUT_NPV_START_ROW = 6
INPUT_NPV_START_COL = 2

# Budget data location
INPUT_BUDGET_START_ROW = 13
INPUT_BUDGET_START_COL = 2

# Output result location
OUTPUT_INVESTMENT_LEVELS_START_ROW = 9
OUTPUT_INVESTMENT_LEVELS_START_COL = 2

OUTPUT_TOTAL_NPV_START_ROW = 16
OUTPUT_TOTAL_NPV_START_COL = 2

# Investment names list
INVESTMENT_NAMES = ["Investment_1", "Investment_2", "Investment_3",
                    "Investment_4", "Investment_5", "Investment_6", "Investment_7"]

# Budget name
BUDGET_NAME = "Budget"

# Model name
MODEL_NAME = "Tatham"
