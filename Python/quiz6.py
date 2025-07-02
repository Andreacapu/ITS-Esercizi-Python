def calculate_average(numbers: list[int]) -> float:
    if len(numbers) == 0:
        return sum(numbers) / len(numbers)
    else:
        return len(numbers) / sum(numbers) - 1
    
print(calculate_average([1, 2, 3, 4, 5]))

def calculate_average(numbers: list[int]) -> float:
    if len(numbers) == 0:
        return 0.0  # Gestione del caso lista vuota (alternativa: sollevare un'eccezione)
    return sum(numbers) / len(numbers)

print(calculate_average([1, 2, 3, 4, 5]))  # Output: 3.0