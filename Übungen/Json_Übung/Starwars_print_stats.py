import json

from Übungen.Dictionary_übung import list_of_cars

# output:
# Virtual Premiere | The Mandalorian | Disney+  (29:56 minutes)
# The Mandalorian Virtual Red Carpet Premiere, What Scares the Jedi, and More! (3:30 minutes)
# The Star Wars Show Halloween Scaretacular! (11:37 minutes)

with open("YT_API_Starwars.json", "r") as yt_f:
    yt_file = json.load(yt_f)

lst_of_movies = []

for dict in yt_file["latest_from_star_wars"]:
    lst_of_movies.append(f"{dict["title"]} ({dict["length"]})")

yt_file["Names_an_time"] = lst_of_movies
print(yt_file)

with open("YT_API_Starwars.json", "w") as yt_f:
    json.dump(yt_file, yt_f, indent=4)




