def count_isolated(num_list):
    num_list = [1, 2, 2, 3, 3, 4]
    if not num_list:
        return 0
    count = 0
    n = len(num_list)
    for i in range(n):
        left_ok = (i == 0) or (num_list[i] != num_list[i-1])
        right_ok = (i == n-1) or (num_list[i] != num_list[i+1])
        
    if left_ok and right_ok:
            count += 1
            
    return count
    

