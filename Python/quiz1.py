def sum_above_threshold(numbers, threshold):
    total = 0
    for num in numbers:
        if num > threshold:
            total += num
    return total
    