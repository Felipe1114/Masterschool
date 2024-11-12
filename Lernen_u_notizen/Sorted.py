"""numbers = [4, 2, 7, 1, 9]

result = sorted(numbers, reverse=True)

print(result)"""

# key -> braucht eine funktion, die sagt, wie sortiert wird.
def str_laenge(string:str):
    return len(string)


namen = ["Peter", "Hans", "Max", "Judith", "Stephan"]
sorted_names = sorted(namen, key=str_laenge)

print(sorted_names)