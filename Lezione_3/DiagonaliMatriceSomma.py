def sum_primary_diagonal(matrix: list[list[int]]):  
    return sum(matrix[i][i] for i in range(len(matrix)))

def 