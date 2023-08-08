def kaprekar_iterations(num):
    # Helper function to perform the Kaprekar's operation
    def kaprekar_op(n):
        num_str = str(n).zfill(4)
        asc_digits = int(''.join(sorted(num_str)))
        desc_digits = int(''.join(sorted(num_str, reverse=True)))
        return desc_digits - asc_digits

    # Perform iterations until convergence or a maximum number of iterations
    max_iterations = 1000
    for i in range(max_iterations):
        num = kaprekar_op(num)
        if num == 6174:
            return True
    return False


def main():
    # Find 4-digit numbers that do not converge to Kaprekar's Constant (6174)
    numbers_not_converging = []
    for num in range(1000, 10000):
        if not kaprekar_iterations(num):
            numbers_not_converging.append(num)

    print("4-digit numbers that do not converge to Kaprekar's Constant (6174):")
    print(numbers_not_converging)


if __name__ == "__main__":
    main()