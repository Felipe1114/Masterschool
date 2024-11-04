# # data = "test text"
# # file_to_write = open("file.txt", "w")
# # file_to_write.write(data)
# # file_to_write.close()
#
#
#
# list = ["alex", "peter", "felipe"]
# list_str =
# data = str(list)
# with open("file.txt", "w") as file_to_write:
#     file_to_write.write(data)
# print("written over file")

input_file = "test_writing_file.txt"
output_file = "klartext.txt"
with open(input_file, "r") as read_file, open(output_file, "w") as write_file:
    spec_list = ["@", "#", "%", "$", "!"]
    for line in read_file:
        for char in spec_list:
            line = line.replace(char, "")
            print(line)
    write_file.write(line)

    



