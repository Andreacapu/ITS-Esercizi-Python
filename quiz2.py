def rounded_average(numeri):
    somma = 0
    for n in numeri:
        somma += n
    media = somma / len(numeri)
    return round(media) 

media = rounded_average([1, 1, 2, 2])
print(media)  