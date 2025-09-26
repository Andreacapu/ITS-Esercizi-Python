def dedup_stable(nums: list[int]) -> list[int]:
    seen = set()
    result = []
    for n in nums:
        if n not in seen:  # Più veloce con set
            seen.add(n)
            result.append(n)
    return result