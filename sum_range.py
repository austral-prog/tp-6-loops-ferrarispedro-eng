# Replace the "ANSWER HERE" for your answer

def sum_to_n(n):
    total = 0

    for number in range(1, n + 1):
        total += number
    return total


def sum_evens(n):
    
    total = 0

    for number in range(1, n + 1):
        if number % 2 == 0:
            total += number

    return total


def factorial(n):
    total = 1
    for number in range(1, n + 1):
        total *= number
    return total
