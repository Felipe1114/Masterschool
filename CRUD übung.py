# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_list = list(range(1,20))
print(my_list)

new_list = []

for i in my_list:
    if i % 2 != 0:
        new_list.append(i)
    print(new_list)