import numpy as np


def read_example_a():
    example_a = open("a_example.txt")

    line = example_a.readline().strip().split(" ")
    number_of_books = int(line[0])
    number_of_libs = int(line[1])
    days = int(line[2])

    general_lib_data = {}

    book_scores = example_a.readline().strip().split(" ")

    book_matrix = np.zeros((number_of_libs, number_of_books), dtype=int)

    for lib_index in range(int(number_of_libs)):

        ## creation of general lib info

        line = example_a.readline()
        book_count = line[0]
        signup_process = line[2]
        ability = line[4]
        general_lib_data[lib_index] = [int(signup_process), int(ability)]

        ## creaton of matrix
        book_indexes = example_a.readline().strip().split(" ")

        for book in book_indexes:
            book_matrix[lib_index][int(book)]= 1

    return days, book_scores, general_lib_data, book_matrix,


def main():
    print("test")


if __name__ == '__main__':
    main()
