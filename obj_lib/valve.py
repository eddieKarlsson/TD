import os
import os.path
from gen_obj_func import GenObjFunc as genfunc


class Valve:
    """Object specifik code to concetenate text lines and create files"""

    def __init__(self, gen_main, output_path, obj_list):
        self.s = gen_main.s  # Instanciate settings

        self.cp = self.s.CONFIG_PATH_VALVE  # Config folder path
        self.cf = os.path.join(self.s.CONFIG_PATH_VALVE, 'valve.txt')

        self.output_path = output_path
        self.out_file_path = os.path.join(self.output_path, 'Generated Valve')

        self.ol = obj_list

        self.gen = genfunc(gen_main)

        self.type = 'valve'

        self.rl = []  # Create empty list "result list"

        self.generate()

    def _s7plc_db(self):
        data = self.gen.single(self.cf, self.rl, 'S7PLC_DB_Header')
        data += self.gen.multiple(self.ol, self.cf, self.rl, 'S7PLC_DB_Var')
        data += self.gen.single(self.cf, self.rl, 'S7PLC_DB_Footer')

        filename = 'S7PLC_' + self.type + '_DB.db'
        file_and_path = os.path.join(self.out_file_path, filename)
        with open(file_and_path, 'w', encoding='cp1252') as f:
            f.write(data)

    def generate(self):
        """Create and concetenate all text lines to different files"""
        # Create sub-directory if it doesn't exist
        if not os.path.exists(self.out_file_path):
            os.makedirs(self.out_file_path)

        self._s7plc_db()

        #  self._intouch()

        self.gen.result(self.rl, type='VALVE')
