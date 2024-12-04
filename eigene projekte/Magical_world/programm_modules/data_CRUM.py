from Übungen.create_files_übungen import read_file

DATAPATH = "./eigene projekte/Magical_world/programm_data/"

def get_data(file_name):
  with open(DATAPATH + file_name, "r") as objfile:
    data = objfile.readlines()
  return data


def save_data(data,file_name):
  with open(DATAPATH + file_name, "w") as objfile:
    objfile.write(data)


def print_data(data):
  for line in data:
    print(line)


def change_data(data, new_data):
  for line in new_data:
    data.append(line)

  return data
