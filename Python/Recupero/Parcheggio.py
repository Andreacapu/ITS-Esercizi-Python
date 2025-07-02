import math
def CalculateChanges(ore:float) -> str:
    ore = 0
    totale = 0

    if ore <= 3:
        return "il totale sono 3.00 euro"
    elif ore == 24:
        return "Il totale sono 10.00 euro"
    elif ore > 3 and ore <24:
        ore_approssimate = math.floor(ore)
        totale = (2*(ore_approssimate - 3)* 0.5)


    print(f"{mat[r][c]:<5}", end="")

