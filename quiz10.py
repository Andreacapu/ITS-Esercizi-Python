merged = dict1.copy() 
    for key, value in dict2.items():
        if key in merged:
            merged[key] += value  
        else:
            merged[key] = value  
    return merged
