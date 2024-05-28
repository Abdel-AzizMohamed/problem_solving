####### Solution 1
def find_average(numbers):
    if not numbers:
        return 0

    sum = 0
    count = 0

    for item in numbers:
        count += 1
        sum += item

    return sum / count


####### Solution 2
def find_average(numbers):
    return 0 if not numbers else sum(numbers) / len(numbers)
