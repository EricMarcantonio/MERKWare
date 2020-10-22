import json
from os import path


class BadMerkFileException(Exception):
    missing_fields: list = None

    def __init__(self):
        super().__init__()


class CONFIG:
    __config_file_keys = ["folder_name", "type", "secrets", "action"]
    folder_name: str = None
    type: str = None
    secrets = []
    action: str = None
    __json_contents: dict = None

    def __init__(self, folder_name: str):
        if not path.exists(folder_name):
            raise FileNotFoundError("Could not find your config file!")

        with open(folder_name, "r") as f:
            self.__json_contents = json.load(f)
            print(self.__is_valid())
            if self.__is_valid():
                self.folder_name = self.__json_contents["folder_name"]
                self.action = self.__json_contents["action"]
                self.secrets = self.__json_contents["secrets"]
                self.type = self.__json_contents["type"]
            else:
                raise BadMerkFileException()

    def __is_valid(self) -> bool:
        temp = []
        for key in self.__json_contents.keys():
            print(key)
            if key not in self.__config_file_keys:
                return False
            else:
                print(self.__json_contents[key])
                if not self.__json_contents[key]:
                    return False

        return False if len(temp) > 0 else True


lol = CONFIG("merk.config.json")
print(lol.type)
