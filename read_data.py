import numpy as np


def read_example(example_name):
    if (example_name == "a"):
        file = open("a_example.txt")
    elif (example_name == "b"):
        file = open("b_example.txt")
    elif (example_name == "c"):
        file = open("c_example.txt")
    elif (example_name == "d"):
        file = open("d_example.txt")
    elif (example_name == "e"):
        file = open("e_example.txt")
    else:
        file = open("f_example.txt")

    line = file.readline().strip().split(" ")
    number_of_books = int(line[0])
    number_of_libs = int(line[1])
    days = int(line[2])

    general_lib_data = {}

    book_scores = file.readline().strip().split(" ")

    book_matrix = np.zeros((number_of_libs, number_of_books), dtype=int)

    for lib_index in range(int(number_of_libs)):

        ## creation of general lib info

        line = file.readline()
        book_count = line[0]
        signup_process = line[2]
        ability = line[4]
        general_lib_data[lib_index] = [int(signup_process), int(ability)]

        ## creaton of matrix
        book_indexes = file.readline().strip().split(" ")

        for book in book_indexes:
            book_matrix[lib_index][int(book)] = 1

    return days, book_scores, general_lib_data, book_matrix



def main():
    # example
    days, book_scores, general_lib_data, book_matrix = read_example("a")



if __name__ == '__main__':
    main()
