"""
Constants
"""

# Data file path and worksheet name
DATA_PATH = "../problem_2b.xlsx"
SHEET_NAME_INPUT = "problem_2b"
SHEET_NAME_OUTPUT = "Solution_Gurobi"

LP_PATH = "./instance/problem_2b.lp"
MPS_PATH = "./instance/problem_2b.mps"

# unit price of computers (3 vendors)
UNIT_PRICE_START_ROW = 4
UNIT_PRICE_START_COL = 2

# delivery charge of computers (3 vendors)
DELIVERY_CHARGE_START_ROW = 5
DELIVERY_CHARGE_START_COL = 2

# the maximum quantity each vendor can supply (3 vendors)
MAX_QUANTITY_START_ROW = 6
MAX_QUANTITY_START_COL = 2

# the minimum required purchase quantity (3 vendors)
MIN_PURCHASE_QUANTITY_START_ROW = 7
MIN_PURCHASE_QUANTITY_START_COL = 2

# total number of computers planned to purchase
PLANNED_COMPUTER_NUMBER_START_ROW = 14
PLANNED_COMPUTER_NUMBER_START_COL = 5

# Output result location
OUTPUT_WHETHER_PURCHASE_START_ROW = 2
OUTPUT_WHETHER_PURCHASE_START_COL = 2

OUTPUT_PURCHASE_NUMBERS_START_ROW = 3
OUTPUT_PURCHASE_NUMBERS_START_COL = 2

OUTPUT_MIN_TOTAL_COST_START_ROW = 5
OUTPUT_MIN_TOTAL_COST_START_COL = 2

OUTPUT_TITLE_ROW = 1
OUTPUT_TITLE_COL = 2

# Vendor names list
VENDOR_NAMES = ["Vendor_1", "Vendor_2", "Vendor_3"]

# Number of computers planned to purchase name
PLANNED_COMPUTER_NUMBER = "total_number_of_computers_planned_to_purchase"

# Model name
MODEL_NAME = "Computer_Purchase_Optimization"
