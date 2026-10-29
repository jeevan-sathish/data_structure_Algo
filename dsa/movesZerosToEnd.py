
def moveZerosToEnd(numbers):
    position = 0

    for i in range(len(numbers)):
        if numbers[i] != 0:
            numbers[position], numbers[i] = numbers[i], numbers[position]
            position += 1

    return numbers


print(moveZerosToEnd([0, 1, 2, 0, 3, 0]))
