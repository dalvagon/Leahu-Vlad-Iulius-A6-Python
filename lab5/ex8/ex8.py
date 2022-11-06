from functions import print_arguments, multiply_output, augment_function
from utils import multiply_by_two, multiply_by_three, add_numbers

if __name__ == "__main__":
    augmented_multiply_by_two = print_arguments(multiply_by_two)
    x = augmented_multiply_by_two(10)
    print(x, "\n")

    augmented_add_numbers = print_arguments(add_numbers)
    x = augmented_add_numbers(3, 4)
    print(x, "\n")

    augmented_multiply_by_three = multiply_output(multiply_by_three)
    x = augmented_multiply_by_three(10)
    print(x, "\n")

    decorated_function = augment_function(
        add_numbers, [print_arguments, multiply_output]
    )
    x = decorated_function(3, 4)
    print(x, "\n")
