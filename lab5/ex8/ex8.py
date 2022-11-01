from utils import (
    print_arguments,
    multiply_by_two,
    add_numbers,
    multiply_output,
    multiply_by_three,
    augment_function,
)

if __name__ == "__main__":
    augmented_multiply_by_two = print_arguments(multiply_by_two)
    x = augmented_multiply_by_two(10)
    print(x)

    augmented_add_numbers = print_arguments(add_numbers)
    x = augmented_add_numbers(3, 4)
    print(x)

    augmented_multiply_by_three = multiply_output(multiply_by_three)

    x = augmented_multiply_by_three(10)
    print(x)

    decorated_function = augment_function(
        add_numbers, [print_arguments, multiply_output]
    )

    x = decorated_function(3, 4)
