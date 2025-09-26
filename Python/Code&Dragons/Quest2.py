def max_or_none(nums: list[int]) -> int | None:
    if not nums:  # Controlla se la lista è vuota
        return None
    
    massimo = nums[0]  # Inizia con il primo elemento
    for n in nums:
        if n > massimo:
            massimo = n
    return massimo