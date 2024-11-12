import os
# Am ende wird kein pfad gefunden. waru?!

# path to directory: /Users/felipepietzsch/Masterschool/Ohne Titel/Masterschool/Codio/Uni_corp/All_pdfs
# path to new Directory: /Users/felipepietzsch/Masterschool/Ohne Titel/Masterschool/Codio/Uni_corp/invoices
# path to months: /Users/felipepietzsch/Masterschool/Ohne Titel/Masterschool/Codio/Uni_corp/invoices/"month"
def create_new_file_name(new_parent_dir, month, file_name) -> str:
    """makes new file name and returns it

    Args:
        new_parent_dir(str): the new parent dir für for all files
        month(str): the last ending of each file (after the last "_", before the suffix)
    """
    master_dir = os.getcwd().split("/")[-1]
    new_file_name = os.path.join('Users/felipepietzsch/Masterschool/Ohne Titel/Masterschool/Codio',
                                 master_dir, new_parent_dir, month, file_name)
    return new_file_name


def move_files(old_dir, new_parent_dir):
    """Gets a path and creates a list of all files in this path.
    Changes the name of each file in list, wich for loop

    Args:
        old_dir(str): name of dir with files we want to move to other dir
        new_parent_dir(str): name of dir, where the files will be moved in
    """
    files_to_move = os.listdir(old_dir)
    for file in files_to_move:
        os.rename('Users/felipepietzsch/Masterschool/Ohne Titel/Masterschool/Codio/Uni_corp/All_pdfs/' + file, create_new_file_name(new_parent_dir, get_month(file), file))


def does_path_exist(dir_content, path):
    if path in dir_content:
        pass
    else:
        raise FileNotFoundError("Dir does not exist")


def move_files_to_new_dir(parent_dir):
    aktual_dir = os.getcwd()
    print(f"You are now in {aktual_dir}")
    dir_content = os.listdir(aktual_dir)
    print(f"The content of this dir is: \n{dir_content}")
    while True:
        try:
            path = input("From wich dir you want to move files?\n(type in dir name from list): ")
            does_path_exist(dir_content, path)
            break
        except FileNotFoundError as e:
            print(e)
    move_files(path, parent_dir)



def end_programm() -> None:
    """Does nothing. Is called, when programm should end"""
    pass


def get_month(file_name):
    """Splits up file_name(str) with "_" -> list of 'firstname', 'lastname', 'month.suffix'
    splits up last element of list with "." -> list of month, suffix
    returns its first -> month

    """
    name_split_up = file_name.split("_")
    month = name_split_up[-1].split(".")[0]
    return month


def extract_month_name(file_name:str) -> str:
    """extract "month" form file_name

    Args:
        file_name(str): looks like this: "firstname_lastname_month.pdf"

    Returns:
        month(str): extracted month, from file_name

    """
    month = get_month(file_name)
    return month


def create_child_folder_struc(file_list:list) -> None:
    """Creates for each file, with a new "month" in its name, a new folder

    Args:
        file_list(list): list of file_names

    Returns:
        None
    """
    for file_name in file_list:
        try:
            os.mkdir(extract_month_name(file_name))
        except FileExistsError:
            continue


def want_to_continue(y_or_n):
    while True:
        try:
            is_continue(y_or_n)
        except ValueError as e:
            print(e)


def is_continue(y_or_n):
    if y_or_n == "y":
        create_parent_dir()
    elif y_or_n == "n":
        end_programm()
    else:
        raise ValueError("Wrong Input. Type in 'y' or 'n'")


def create_parent_dir() -> str:
    while True:
        try:
            new_dir_name = input("I will create a new dir\n Wich name should it has?: ")
            os.mkdir(new_dir_name)
            break
        except FileExistsError as e:
            print(e)
            yes_or_no = input("You want to continue?(y/n): ")
            want_to_continue(yes_or_no)
    return new_dir_name


def create_new_dir_structure(file_list) -> str:
    """Creates a new Directory ("invoices") creates - depending on file-name ending - new folders with name of "month"
    goes in the new dir
    creates a new folder, for each file_name form file_list, with a new "month" in its name
    goes back to current used dir

    Args:
          file_list(list): a list of file_names

    Returns:
         None
    """
    new_dir_name = create_parent_dir()
    os.chdir(new_dir_name)
    create_child_folder_struc(file_list)
    os.chdir("..")
    return new_dir_name


def get_list_of_content(path) -> list:
    """Gets all content from folder path into a list

    Args:
        path(str): the name of a directory

    Returns:
        content_lst(list): a list of all files in the directory
    """
    while True:
        try:
            content_lst = os.listdir(path)
            return content_lst
        except FileNotFoundError:
            print("Path does not exist. Type in a new path")


def get_directory_path() -> str:
    path = input("From wich dir, you want to order files?\n(The path has to exist): ")
    return path


def is_actual_dir_correct():
    actual_dir = os.getcwd()
    y_or_n = input(f"Hello, your actual location is:\n{actual_dir}\nAre you in the correct location?(y/n): ")
    if y_or_n == "y":
        pass
    elif y_or_n == "n":
        new_dir = input("In wich dir you want to change?: ")
        os.chdir(new_dir)
    print(f"You are now in{os.getcwd()}")


def main() -> None:
    """Get path from Input
    get list of content from path(folder)
    creates new directories for every Month, depending on wich months exists in File names
    renames all Files so, they are in the correct mont-folder
    """
    # go to corrrect dir
    print("=====File_ordering_programm=====\n"
          "The Programm will order all files from one dir to another dir")
    is_actual_dir_correct()
    list_of_content = get_list_of_content(get_directory_path())
    new_parent_dir = create_new_dir_structure(list_of_content)
    move_files_to_new_dir(new_parent_dir)


if __name__ == "__main__":
    main()