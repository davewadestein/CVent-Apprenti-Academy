"""Class example"""
from config import MAX_NUM
import code_runner


class Files:
    files = {
        "100": list(range(1, 11)),
        "200": [],
        "400": [],
      "OTHER": [], # files can, in theory, have non-int names
    }

    current_file = {
          "name": None,
        "cursor": 0,
    }

    @classmethod
    def GRAB(cls, file):
        if not file in cls.files: # invalid filename
            raise Exception(f'Unknown filename: {file}')
        if cls.current_file["name"]:
            raise Exception(f'Cannot open {file} because ' +
                    f'{cls.current_file["name"]} is already open')
        cls.current_file['name'], cls.current_file['cursor'] = file, 0


    @classmethod
    def FILE(cls, register):
        pass


    @classmethod
    def SEEK(cls, value):
        """SEEK if file is open, otherwise exception"""

        cls.ensure_file_is_open()
        position = code_runner.get_register_contents_or_value(value)

        if not (-MAX_NUM <= position <= MAX_NUM):
            raise Exception(f"Illegal SEEK Position: {position}")

        if position == -MAX_NUM:
            position = 0
        elif position == MAX_NUM:
            position = len(Files.files[cls.current_file['name']])

        cls.current_file['cursor'] = position


    @classmethod
    def VOID(cls):
        cls.ensure_file_is_open()
        if cls.is_current_file_at_eof():
            raise Exception('Cannot VOID with current file at EOF')
        del cls.files[cls.current_file['name']][cls.current_file['cursor']]


    @classmethod
    def DROP(cls):
        cls.current_file['name'] = None


    @classmethod
    def file_is_open(cls):
        """Several instructions require a file to be open"""
        return cls.current_file['name']


    @classmethod
    def ensure_file_is_open(cls):
        if not cls.file_is_open():
            raise Exception('No file is open!')


    @classmethod
    def is_current_file_at_eof(cls):
        return cls.current_file["cursor"] >= len(cls.files[cls.current_file["name"]])


    @classmethod
    def read_value_from_file(cls):
        print(cls.current_file)
        value = cls.files[cls.current_file["name"]][cls.current_file["cursor"]]
        cls.current_file["cursor"] += 1
        return value


    @classmethod
    def write_value_to_file(cls, value):
        if cls.is_current_file_at_eof():
            cls.files[cls.current_file["name"]].append(value)
        else:
            cls.files[cls.current_file["name"]][cls.current_file["cursor"]] = value
        cls.current_file["cursor"] += 1


    @classmethod
    def print_final_value_of_files(cls):
        for file in cls.files:
            print(f'{file}: {cls.files[file]}')
