def sumInrange(a:int, b:int) ->int:
    if a > b:
        temp:int = a
        a = b
        b = temp

        sum:int = 0
        while b >= a:
            sum = sum +b
            b = b-1
            return int(sum)
    
sumInrange(a = 5)
sumInrange(b = 10)
sumInrange(a = 10)
sumInrange(b = 5)