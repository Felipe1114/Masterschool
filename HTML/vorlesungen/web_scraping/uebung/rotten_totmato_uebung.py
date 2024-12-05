from bs4 import BeautifulSoup

DATAPATH = "../data/data.html"

def get_data(filepath):
  with open(filepath, "r") as htmlfile:
    data = htmlfile.read()
    return data


def find_cirital_consensus(html):
  data = BeautifulSoup(html, features="html.parser")
  critics = data.findAll(name="div", attrs={"class":"consensus"})
  print(len(critics))
  print(type(critics))

  """for critic in critics:
    print(critic.text.strip())"""

find_cirital_consensus(get_data(DATAPATH))


