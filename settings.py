"""General settings for Gen_TD.py"""
CONFIG_PATH = 'Config'  # sub-directory of config files
CONFIG_PATH_VALVE = 'Config/Valve'  # sub-directory for valve config

"""Settings"""
ROW = 6  # Excel start row of data
INDEX_REPLACE = '@INDEX'  # string to be replaced in config file

ID_REPLACE = '@ID'  # string to be replaced in config file
COL_ID = 2  # Excel column index of ID, 2 = B column

COMMENT_REPLACE = '@CMT'  # string to be replaced in config file
COL_COMMENT = 3  # Excel column index of Comment, 3 = C column

CONFIG_REPLACE = '@CFG'  # string to be replaced in config file
COL_CONFIG = 7  # Excel column index of Config, 7 = G column

ENG_UNIT_REPLACE = '@ENGUNIT'  # string to be replaced in config file
COL_ENG_UNIT = 11  # Excel column index of Config, 11 = K column

ENG_MIN_REPLACE = '@ENGMIN'  # string to be replaced in config file
COL_ENG_MIN = 14  # Excel column index of Config, 14 = O column

ENG_MAX_REPLACE = '@ENGMAX'  # string to be replaced in config file
COL_ENG_MAX = 15  # Excel column index of Config, 15 = O column

ADR_REPLACE = '@ADR'  # string to be replaced in config file

PLC_NAME = 'PLC1'  # Used in Intouch
PLC_REPLACE = '@PLC'  # string to be replaced in config file

DI_DISABLE = True  # If set to True no files will be generated for DI
DI_START_INDEX = 0  # Start-position index in datablock, used for HMI tags that are absolute.

DO_DISABLE = True
DO_START_INDEX = 0

VALVE_DISABLE = False
VALVE_START_INDEX = 0

MOTOR_DISABLE = False
MOTOR_START_INDEX = 0

AI_DISABLE = False
AI_START_INDEX = 0

AO_DISABLE = False
AO_START_INDEX = 0