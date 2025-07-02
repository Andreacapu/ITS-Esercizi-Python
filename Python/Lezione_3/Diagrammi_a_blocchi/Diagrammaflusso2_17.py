t_media = 0
t_max = 0
t_min = 0
day_max = 0
day_min = 0

for giorno in range(7):
    temp = int(input(f"inserire la temperatura {giorno+1}: "))
    t_media = t_media / 7
    if temp > t_media:
        t_max = temp
        day_max = giorno
    else:
        t_min = temp
        day_min = giorno
    
    if temp >= 10 and temp <= 30:
        print("temperatura nella norma")
    else:
        print("allerta temperatura")

print(f"temperatura media: {t_media}, temperatura massima: {t_max}, temperatura minima: {t_min}, Giornata più calda: {day_max}, giornata più fredda: {day_min}")