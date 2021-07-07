import random

def rand_row_gen(num_rows):
    """
    creates a generator for rows of five numbers

    Parameters:
        num_rows (int): number of rows to generate

    Returns:
        generator: row generator
    """
    for row in range(num_rows):

        newrow = []

        for column in range(5):
            newrow.append(random.randint(1,3))

        yield newrow


