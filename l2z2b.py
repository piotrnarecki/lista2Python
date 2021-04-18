from vector2d import Vector2d


def main():
    print ("correct vector:")
    correct_vector = Vector2d(-6.9, 42)
    correct_vector.print_vector()
    print ("length:", correct_vector.vector_length())
    print()

    print ("multiplied vector:")
    multiplied_vector1 = correct_vector.multiply_vector(5)
    multiplied_vector1.print_vector()
    print()

    print ("vector multiplied by wrong factor:")
    multiplied_vector2 = correct_vector.multiply_vector('f')
    multiplied_vector2.print_vector()
    print()

    print ("vector multiplied by nothing:")
    multiplied_vector2 = correct_vector.multiply_vector()
    multiplied_vector2.print_vector()
    print()

    print ("wrong argument vector:")
    wrong_argument_vector = Vector2d(-6.9, 'f')
    wrong_argument_vector.print_vector()
    print (wrong_argument_vector.vector_length())
    print

    print ("not enough arguments vector:")
    not_enough_arguments_vector = Vector2d(65)
    not_enough_arguments_vector.print_vector()
    print (not_enough_arguments_vector.vector_length())
    print()

    print ("no arguments vector:")
    no_arguments_vector = Vector2d()
    no_arguments_vector.print_vector()
    print no_arguments_vector.vector_length()
    print()

    print ("to much arguments vector:")
    to_much_arguments_vector = Vector2d(2, 3, 4)
    to_much_arguments_vector.print_vector()
    print (to_much_arguments_vector.vector_length())
    print()


if __name__ == '__main__':
    main()
