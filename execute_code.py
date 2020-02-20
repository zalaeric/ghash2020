import read_data
import numpy as np

test_dict = {
    #  su, ab
    0: [2, 2],
    1: [3, 1]
}

test_matrix = [
    [1, 1, 1, 1, 1, 0],
    [1, 0, 1, 1, 0, 1],
]

book_score = [1, 2, 3, 6, 5, 4]


def create_output():
    with open('somefile.txt', 'w') as the_file:
        the_file.write('Hello\n')


def get_best_library():
    for i, row in enumerate(test_matrix):
        if not test_dict[i]:
            continue

        # if signup time is too long
        if row[0] > days_left:
            test_dict.pop(i, None)
            continue


if __name__ == '__main__':
    a = [1, 2, 3]
    test_matrix = np.matrix(test_matrix)

    res_num_of_lib = 0
    res_signed_libs = []

    days_left = 10

    while days_left > 0:
        lib_id = get_best_library()
        break





    # while
    # lib_id =
    # print(b)

    create_output()
