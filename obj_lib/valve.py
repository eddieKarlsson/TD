import os
import os.path
from gen_obj_func import GenObjFunc as genfunc


class Valve:
    """Sub-class object for generator """

    def __init__(self, gen_main, output_path, obj_list):
        self.s = gen_main.s
        self.config_file = os.path.join(self.s.CONFIG_PATH_VALVE,
                                        'config_valve.txt')

        self.output_path = output_path
        self.file_path = os.path.join(self.output_path, 'Generated Valve')

        self.obj_list = obj_list

        self.gen = genfunc(gen_main)

        self.type = 'valve'

        self.rl = []  # Create empty list "result list"

        self.generate()

    def _plc(self):
        """PLC"""
        # PLC Datablock
        db_header_data = self.gen.single(self.config_file,
                                         'db_header', self.rl)
        db_var_data = self.gen.multiple(self.obj_list, self.config_file,
                                        'db_var', self.rl)
        db_footer_data = self.gen.single(self.config_file,
                                         'db_footer', self.rl)

        filename = 'PLC_' + self.type + '_DB.db'
        file_and_path = os.path.join(self.file_path, filename)
        with open(file_and_path, 'w', encoding='cp1252') as dbFile:
            data = db_header_data
            data += db_var_data
            data += db_footer_data
            dbFile.write(data)

    def _intouch(self):
        """Intouch IO:Int"""
        IT_IOInt_header = self.gen.single(self.config_file,
                                          'IT_IOInt_Header', self.rl)
        IT_IOInt_data = self.gen.multiple(self.obj_list, self.config_file,
                                          'IT_IOInt_Tag', self.rl,
                                          data_size=30, data_offset=14)

        """Intouch Memory:Int"""
        IT_MemInt_header = self.gen.single(self.config_file,
                                           'IT_MemInt_Header', self.rl)
        IT_MemInt_data = self.gen.multiple(self.obj_list, self.config_file,
                                           'IT_MemInt_Tag', self.rl)

        filename = 'IT_' + self.type + '.csv'
        file_and_path = os.path.join(self.file_path, filename)
        with open(file_and_path, 'w', encoding='cp1252') as itFile:
            data = IT_IOInt_header
            data += IT_IOInt_data
            data += IT_MemInt_header
            data += IT_MemInt_data

            itFile.write(data)

    def generate(self):
        """Create and concetenate all text lines to different files"""
        # Create sub-directory if it doesn't exist
        if not os.path.exists(self.file_path):
            os.makedirs(self.file_path)

        self._plc()
        self._intouch()

        self.gen.result(self.rl, type='VALVE')
