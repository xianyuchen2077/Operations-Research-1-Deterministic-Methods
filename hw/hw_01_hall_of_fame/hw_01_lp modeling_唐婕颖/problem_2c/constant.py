#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2025/10/6 22:11
# @Author: TJY

"""
Constants
"""

# Data file path and worksheet name
DATA_PATH = "./data/problem_2b_copy.xlsx"
INPUT_SHEET_NAME = "Data"
OUTPUT_SHEET_NAME="Solution Gurobi"

#LP Model File Paths
LP_PATH = "./instance/WorldLight.lp"
MPS_PATH = "./instance/WorldLight.mps"

# Input Data Location
# Profit per unit data location (Product 1 & Product 2)
INPUT_PROFIT_START_ROW = 4
INPUT_PROFIT_START_COL = 2

#Resource usage per unit produced(Mental Frame Parts & Electrical Components)
INPUT_Resourse_UNITS_START_ROW = 7
INPUT_Resourse_UNITS_START_COL = 2

# Units available data location (Mental Frame Parts & Electrical Components)
INPUT_UNITS_AVAILABLE_START_ROW = 7
INPUT_UNITS_AVAILABLE_START_COL = 6

# Product 2 quantity limit
INPUT_PRODUCT2_LIMIT_START_ROW = 13
INPUT_PRODUCT2_LIMIT_START_COL = 3

# Output result location
OUTPUT_UNITS_PRODUCED_START_ROW = 11
OUTPUT_UNITS_PRODUCED_START_COL = 2

OUTPUT_PROFIT_START_ROW = 11
OUTPUT_PROFIT_START_COL = 6

# Product names list
PRODUCT_NAMES = ["Product 1", "Product 2"]

# Production Resource names list
Resource_NAMES = ["MetalFrameParts", "Electrical Components"]

# Model name
MODEL_NAME = "WorldLight"
