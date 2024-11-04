
def remove_spec_chars(read_file, spec_char_lst, write_file):
    for line in read_file:
        for char in spec_char_lst:
            line = line.replace(char, "")
        write_file.write(line)

def make_list_from_str(string: str) -> list:
    spec_char_lst = []
    for char in string:
        spec_char_lst.append(char)
    return spec_char_lst


def read_and_write_file(input_file, output_file):
    with open(input_file, "r") as read_file, open(output_file, "w") as write_file:
        spec_char_str = '@#$%^&*()[]{}<>|/~`+=;:,!1234567890😊'
        spec_char_lst = make_list_from_str(spec_char_str)
        remove_spec_chars(read_file, spec_char_lst, write_file)


def main():
    input_file = "uebungs_text.txt"
    output_file = "klar_text.txt"
    read_and_write_file(input_file, output_file)


if __name__ == "__main__":
    main()
