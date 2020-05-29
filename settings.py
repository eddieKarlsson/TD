"""General settings for Gen_TD.py"""
CONFIG_PATH = 'Config'  # sub-directory of config files
CONFIG_PATH_VALVE = 'Config/Valve'  # sub-directory for valve config

"""Excel settings"""
ROW = 6  # Excel start row of data
INDEX_REPLACE = '@INDEX'  # string to be replaced in config file

ID_REPLACE = '@ID'  # string to be replaced in config file
COL_ID = 2  # Excel column index of ID, 2 = B column

COMMENT_REPLACE = '@CMT'  # string to be replaced in config file
COL_COMMENT = 3  # Excel column index of Comment, 3 = C column

CONFIG_REPLACE = '@CFG'  # string to be replaced in config file
COL_CONFIG = 7  # Excel column index of Config, 4 = G column

"""S7-PLC settings"""
ADR_REPLACE = '@ADR'  # string to be replaced in config file


"""Disable options"""
DI_DISABLE = True
DO_DISABLE = True
VALVE_DISABLE = False
