import json


def read_json(file_path) -> dict:
    """Reads a dictionary and gives back a dictionary

        Args:
            file_path(str): the file path of the json file

        returns:
            data(dict): a dictionary with the datas from the json file
    """
    with open(file_path, "r") as file:
        data = json.load(file)
    return data


def update_json(file_path: str, data: dict) -> None:
    """Updates a json file

        Args:
            file_path(str): the file path of the json file
            data(dict): the dictionary with the new data
        returns:
            None
    """
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)


def print_json(file_path: str) -> None:
    """Prints the data from a json file as an dictionary

        Args:
            file_path(str): the file path of the json file

        returns:
            None
    """
    data = read_json(file_path)
    print(json.dumps(data, indent=4))


def create_json(file_path: str) -> None:
    """Creates an empty json file. !!!The difference between update and create is: updates contains a data input

        Args:
            file_path(str): the file path of the json file

        returns:
            None
    """
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

