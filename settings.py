"""General settings for Gen_TD.py"""
EXCEL_FILE = r'C:\Downloads\TD - Kivik -  Kivik CIP & Kyl-lager - 190095.xlsx'  # full path and extension
CONFIG_PATH = 'Config'  # sub-directory of config files
CONFIG_PATH_VALVE = 'Config/Valve'  # sub-directory for valve config
OUTPUT_PATH = r'C:\Project\Python\slask'  # If 'None' files are created in current directory

"""Excel settings"""
ROW = 6  # Excel start row of data
INDEX_REPLACE = '@INDEX'  # string to be replaced in config file

ID_REPLACE = '@ID'  # string to be replaced in config file
COL_ID = 2  # Excel column index of ID, 2 = B column

COMMENT_REPLACE = '@CMT'  # string to be replaced in config file
COL_COMMENT = 3  # Excel column index of Comment, 3 = C column

CONFIG_REPLACE = '@CFG'  # string to be replaced in config file
COL_CONFIG = 4  # Excel column index of Config, 4 = D column

"""Disable options"""
DI_DISABLE = False
DO_DISABLE = False
VALVE_DISABLE = False
