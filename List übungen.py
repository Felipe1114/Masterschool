'''adresses = [
    'Heinestraße 45, zartstsraße 45',
    'volkerstarß3 45, sssdafsd 45', ]

for adress in adresses:
    adress.count(".", ",")'''


def no_punctuation(word):
    word_list = [word.count('.'), word.count(',')]
    if word_list == [0, 0]:
        print(word)


print(no_punctuation("Hello world."))
print(no_punctuation("Hello world"))
print(no_punctuation("Hello, world!"))

def is_divisible(x, y):
    if x %y == 0:
       return True
    else:
       return False

if is_divisible(10, 5):
    print("Divisible!")
