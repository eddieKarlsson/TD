import sys
import os
import os.path
import openpyxl as xl
from settings import Settings


class GenTD:
    def __init__(self, excel_path, output_path):
        self.excel_path = excel_path
        self.output_path = output_path

        self.all_it_files = []  # Create an empty list
        self.generate()
        self.s = Settings()

    def generate(self):
        """Logging settings"""
        print('Version', self.s.version)

        self.open_td_excel()

        # DI
        if self.s.DI_DISABLE:
            print('DI not generated, disabled in settings file')
        else:
            self.td_gen_di()

        # DO
        if self.s.DO_DISABLE:
            print('DO not generated, disabled in settings file')
        else:
            self.td_gen_do()

        # Valve
        if self.s.VALVE_DISABLE:
            print('Valve not generated, disabled in settings file')
        else:
            self.td_gen_valve()

        # Motor
        if self.s.MOTOR_DISABLE:
            print('Motor not generated, disabled in settings file')
        else:
            self.td_gen_motor()

        # AI
        if self.s.AI_DISABLE:
            print('AI not generated, disabled in settings file')
        else:
            self.td_gen_ai()

        # AO
        if self.s.AO_DISABLE:
            print('AO not generated, disabled in settings file')
        else:
            self.td_gen_ao()

    def open_td_excel(self):
        try:
            wb = xl.load_workbook(self.excel_path, data_only=True)
        except FileNotFoundError as e:
            print(e)
            print('Error! Excel file not found, program will exit')
            sys.exit()
        else:
            self.wb = wb

    def td_single(self, config_file, ref_txt):
        """Read a text file and copy the data inside notifiers to memory"""
        with open(config_file, 'r') as config:
            exists_in_config = False
            section_found = False
            inst_data = ''
            begin = '[gen.' + ref_txt + '_begin]'
            end = '[gen.' + ref_txt + '_end]'

            for line in config:
                if end in str(line):
                    section_found = False
                if section_found:
                    inst_data += line
                if begin in str(line):
                    exists_in_config = True
                    section_found = True
        if not exists_in_config:
            print(ref_txt, 'not found in config file!')

        return inst_data

    def td_multiple(self, config_file, ref_txt, excelsheet, udt_size=30,
                    udt_offset=14, start_index=0):
        """Get text lines from config file and replace by data in excel,
           then append the new lines to memory"""
        # Try to open excelsheet, otherwise prompt user
        try:
            active_sheet = self.wb[excelsheet]  # open sheet
        except KeyError:
            msg = f'Error! {excelsheet} sheet does not exist, prog will exit'
            print(msg)
            sys.exit()

        with open(config_file, 'r') as config:
            exists_in_config = False
            section_found = False
            inst_data = ''
            begin = '[gen.' + ref_txt + '_begin]'
            end = '[gen.' + ref_txt + '_end]'
            adrIndx = start_index - 1  # -1 to have first 0

            for i in range(self.s.ROW, active_sheet.max_row + 1):
                cell_id = active_sheet.cell(row=i, column=self.s.COL_ID)
                cell_config = active_sheet.cell(row=i,
                                                column=self.s.COL_CONFIG)
                cell_comment = active_sheet.cell(row=i,
                                                 column=self.s.COL_COMMENT)
                cell_engunit = active_sheet.cell(row=i,
                                                 column=self.s.COL_ENG_UNIT)
                cell_engmin = active_sheet.cell(row=i,
                                                column=self.s.COL_ENG_MIN)
                cell_engmax = active_sheet.cell(row=i,
                                                column=self.s.COL_ENG_MAX)

                adrIndx += 1

                if cell_id.value is None:
                    break

                config.seek(0, 0)  # Seek to beginning of file
                for lineIndex, line in enumerate(config, start=1):
                    if end in str(line):
                        section_found = False
                    if section_found:
                        line = line.replace(self.s.ID_REPLACE, cell_id.value)

                        if cell_config.value is not None:
                            line = line.replace(self.s.CONFIG_REPLACE,
                                                cell_config.value)

                        # Replace index
                        line = line.replace(self.s.INDEX_REPLACE, str(adrIndx))

                        # calculate address by offset & datatype udt_size
                        adress = (adrIndx * udt_size) + udt_offset
                        # Replace '@ADR'
                        line = line.replace(self.s.ADR_REPLACE, str(adress))

                        # Replace PLC
                        line = line.replace(self.s.PLC_REPLACE,
                                            self.s.PLC_NAME)

                        # check if eng unit exists, if not insert empty string
                        if cell_engunit.value is None:
                            line = line.replace(self.s.ENG_UNIT_REPLACE, '')
                        else:
                            line = line.replace(self.s.ENG_UNIT_REPLACE,
                                                cell_engunit.value)

                        # check if eng min exists, if not insert 0
                        if cell_engmin.value is None:
                            line = line.replace(self.s.ENG_MIN_REPLACE, '0')
                        else:
                            line = line.replace(self.s.ENG_MIN_REPLACE,
                                                str(cell_engmin.value))

                        # check if eng max exists, if not insert 100
                        if cell_engmax.value is None:
                            line = line.replace(self.s.ENG_MAX_REPLACE, '100')
                        else:
                            line = line.replace(self.s.ENG_MAX_REPLACE,
                                                str(cell_engmax.value))

                        # check if comment exists, if not insert empty string
                        if cell_comment.value is None:
                            line = line.replace(self.s.COMMENT_REPLACE, '')
                        else:
                            line = line.replace(self.s.COMMENT_REPLACE,
                                                cell_comment.value)

                        inst_data += line  # Create instance data
                    if begin in str(line):
                        exists_in_config = True
                        section_found = True
            if not exists_in_config:
                print(ref_txt, 'in config file not found!')
            else:
                print('Generated from row:',
                      self.s.ROW, 'to', i - 1, 'of', ref_txt, 'in',
                      active_sheet)

        return inst_data

    def td_multiple_config(self, sub_dir, ref_txt, excelsheet):
        """Same as td_multiple, but config stored in different files"""
        # Try to open excelsheet, otherwise prompt user
        try:
            active_sheet = self.wb[excelsheet]  # open sheet
        except KeyError:
            msg = f'Error! {excelsheet} sheet does not exist, prog will exit'
            print(msg)
            sys.exit()

        # Setup variables
        exists_in_config = False
        section_found = False
        inst_data = ''
        begin = '[gen.' + ref_txt + '_begin]'
        end = '[gen.' + ref_txt + '_end]'
        zeroIdx = 0

        # loop through excel rows, get value at corresponding cell
        for i in range(self.s.ROW, active_sheet.max_row + 1):
            cell_id = active_sheet.cell(row=i, column=self.s.COL_ID)
            cell_config = active_sheet.cell(row=i, column=self.s.COL_CONFIG)
            cell_comment = active_sheet.cell(row=i, column=self.s.COL_COMMENT)
            zeroIdx += 1

            if cell_id.value is None:
                break

            # combine file path and open corresponding file
            filename = cell_config.value + '.txt'
            file_and_path = os.path.join(sub_dir, filename)
            with open(file_and_path, 'r') as config:
                for line in config:
                    if end in str(line):
                        section_found = False
                    if section_found:
                        line = line.replace(self.s.ID_REPLACE, cell_id.value)

                        if cell_config.value is not None:
                            line = line.replace(self.s.CONFIG_REPLACE,
                                                cell_config.value)
                        line = line.replace(self.s.INDEX_REPLACE, str(zeroIdx))

                        # check if comment exists, if insert empty string
                        if cell_comment.value is None:
                            line = line.replace(self.s.COMMENT_REPLACE, '')
                        else:
                            line = line.replace(self.s.COMMENT_REPLACE,
                                                cell_comment.value)

                        inst_data += line  # Create instance data
                    if begin in str(line):
                        exists_in_config = True
                        section_found = True
        if not exists_in_config:
            print(ref_txt, 'in config file not found!')
        else:
            print('Generated from row:', self.s.ROW, 'to',
                  i - 1, 'of', ref_txt, 'in', active_sheet)
        return inst_data
