def has_dot(string):
    if string.find(".") != -1:
        return True
    else:
        return False

def main():
    string = "halle."
    print(has_dot(string))


def is_all_dollar(string):
    for i in string:
        if i != "$":
            return False
    return True
string_dollar = "$$$$$"
string_dot = "halle"
print(is_all_dollar(string_dollar))
print(has_dot(string_dot))
