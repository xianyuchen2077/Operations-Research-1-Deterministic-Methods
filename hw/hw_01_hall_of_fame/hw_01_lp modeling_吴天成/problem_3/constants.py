# -*- coding: utf-8 -*-

"""
Constants
"""

# Data file path and worksheet name
DATA_PATH = "./data/problem_2.xlsx"
INPUT_SHEET_NAME = "Sheet1"

LP_PATH = "./instance/WorldLightProblem.lp"
MPS_PATH = "./instance/WorldLightProblem.mps"

# Profit per light fixture
PROFIT_ROW = 4
PROFIT_COL1 = 2  # 产品1的利润在B4
PROFIT_COL2 = 3  # 产品2的利润在C4

# Metal frame parts used per product produced
FRAME_ROW = 6
FRAME_COL1 = 2   # 产品1的单位框架消耗在B6
FRAME_COL2 = 3   # 产品2的单位框架消耗在C6

# Electrical components used per product produced
ELECTRONIC_ROW = 7
ELECTRONIC_COL1 = 2   # 产品1的单位电力部件消耗在B7
ELECTRONIC_COL2 = 3   # 产品2的单位电力部件消耗在C7

# Resource available data 
FRAME_AVAILABLE_ROW = 6
FRAME_AVAILABLE_COL = 6
ELECTRONIC_AVAILABLE_ROW = 7
ELECTRONIC_AVAILABLE_COL = 6

# Maximum production volume
Max_Product2_ROW = 9
Max_Product2_COL = 3

# Output result
OUTPUT_PRODUCT_ROW = 11
OUTPUT_PRODUCT_COL1 = 2
OUTPUT_PRODUCT_COL2 = 3

OUTPUT_PROFIT_ROW = 11
OUTPUT_PROFIT_COL = 6

# Output worksheet name
OUTPUT_SHEET_NAME = "Solution_Gurobi"

# Product names list
PRODUCT_NAMES = ["Product1", "Product2"]

# Model name
MODEL_NAME = "WorldLight_Optimization"