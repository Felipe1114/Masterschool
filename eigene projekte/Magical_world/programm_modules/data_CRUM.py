
DATAPATH = "./programm_data/"

def get_data(file_name):
  with open(DATAPATH + file_name, "r") as objfile:
    data = objfile.readlines()
  return data


def save_data(data,file_name):
  with open(DATAPATH + file_name, "w") as objfile:
    for line in data:
      objfile.write(line)


def print_data(data):
  for line in data:
    print(line)


def add_data(new_data, file_name):
  data = get_data(file_name)
  for line in new_data:
    data.append(line)
  save_data(data, file_name)


  return data
