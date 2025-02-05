def sum(numbers):
    if not numbers:
        return 0
    remaining_sum = sum(numbers[1:])
    return numbers[0] + sum(numbers[1:])