def sum_list(nums: list[int]) -> int:
    if len(nums)<=0:
        return 0
    
    total = 0
    for n in nums:
        total = total + n
    return (total)
