def sum_primary_diagonal(matrix: list[list[int]]) -> int:
            summ: int = 0
            summ2: int = 0
            counter = len(matrix)-1
            for i in range(len(matrix)):
                    summ += matrix[i][i]
                    summ2 += matrix[i][counter]
                    counter -= 1
                    