def make_copy_file(file_name:str):
    with open(file_name, "r") as objfile:
        file = objfile.read()
    isolated_file_name, suffix = exract_suffix_and_file_name(file_name)
    file_name_copy = isolated_file_name + "_copy" + suffix
    with open(file_name_copy, "w") as objfile:
        objfile.write(file)


def exract_suffix_and_file_name(file_name) -> tuple:
    name_splitup = file_name.split(".")
    suffix = "." + name_splitup[-1]
    isolated_file_name = "".join(name_splitup[:-1])
    return isolated_file_name, suffix

def make_new_file(file_name, file_data):
    with open(file_name, "w") as fileobj:
        fileobj.write(file_data)

def only_ten_first_lines(file_name):


make_copy_file("olympic-medals.csv")

