    def td_gen_motor(self):
        """Create and concetenate all text lines to different files"""
        # setup variables
        config_file = os.path.join(s.CONFIG_PATH, 'Config_motor.txt')
        sheet = 'Motor'

        # Check what output path to use, if 'None' create in current directory, otherwise as specified
        if self.output_path is None:
            file_path = 'Generated Motor'
        elif self.output_path == OUTPUT_PATH_START_VALUE:
            file_path = 'Generated Motor'
        else:
            file_path = os.path.join(self.output_path, 'Generated Motor')
        # Create sub-directory if it doesn't exist
        if not os.path.exists(file_path):
            os.makedirs(file_path)

        """PLC"""
        # PLC Datablock, if all elements exists concatenate data and create file
        db_header_data = self.td_single(config_file, 'db_header')
        db_var_data = self.td_multiple(config_file, 'db_var', sheet)
        db_footer_data = self.td_single(config_file, 'db_footer')
        if db_header_data != '' and db_var_data != '' and db_footer_data != '':
            filename = 'PLC_' + sheet + '_DB.db'
            file_and_path = os.path.join(file_path, filename)
            with open(file_and_path, 'w', encoding='cp1252') as dbFile:
                data = db_header_data
                data += db_var_data
                data += db_footer_data
                dbFile.write(data)
                print(filename, 'created')
                logging.info(filename + ' created')

        """Intouch IO:Int"""
        IT_IOInt_header = self.td_single(config_file, 'IT_IOInt_Header')
        IT_IOInt_data = self.td_multiple(config_file, 'IT_IOInt_Tag', sheet, udt_size=30, udt_offset=14,
                                         start_index=s.MOTOR_START_INDEX)
        """Intouch Memory:Int"""
        IT_MemInt_header = self.td_single(config_file, 'IT_MemInt_Header')
        IT_MemInt_data = self.td_multiple(config_file, 'IT_MemInt_Tag', sheet, start_index=s.MOTOR_START_INDEX)

        if IT_IOInt_data != '' and IT_IOInt_header != '' and IT_MemInt_header != '' and IT_MemInt_data != '':
            filename = 'IT_' + sheet + '.csv'
            file_and_path = os.path.join(file_path, filename)
            self.all_it_files.append(file_and_path)  # Append full path to list, will be used in another function
            with open(file_and_path, 'w', encoding='cp1252') as itFile:
                data = IT_IOInt_header
                data += IT_IOInt_data
                data += IT_MemInt_header
                data += IT_MemInt_data

                itFile.write(data)
                print(filename, 'created')
                logging.info(filename + ' created')
        print('Generated files put in...', file_path)
        logging.info('Generated Motor files put in ' + file_path)
