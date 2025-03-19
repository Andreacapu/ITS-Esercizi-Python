'''

3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
• Store the locations in a list. Make sure the list is not in alphabetical order.
• Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
• Use sorted() to print your list in alphabetical order without modifying the actual list.
• Show that your list is still in its original order by printing it.
• Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
• Show that your list is still in its original order by printing it again.
• Use reverse()  to change the order of your list. Print the list to show that its order has changed.
• Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
• Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
• Use sort() to change your list so it’s stored in reverse-alphabetical order.
Print the list to show that its order has changed.

'''


lista_località = ["vienna", "tokyo", "andorra", "pechino", "zurigo"]
print("lista originale", lista_località)

# lista stampata in ordine alfabetico senza modificare la lista originale
print(f"lista in ordine alfabetico {sorted(lista_località)} ")
print("lista originale", lista_località)

#lista_località=sorted(lista_località)

#print("lista sovrascritta", lista_località)

print("lista in ordine originale dopo la modifica",sorted(lista_località, reverse = True))

# lista originale
print(f"lista originale {lista_località}")

# reverse() modifica la lista originale invertendo l'oridne dei suoi elementi
lista_località.reverse()
print("lista originale dopo reverse():", lista_località)

lista_località.reverse()
print("lista dopo secondo reverse():", lista_località)

# modifica la lista in modo che gli elementi della lista siano ordinati in ordine alfabetico (A-Z)
lista_località.sort()
print(f"Lista dopo sort(): {lista_località}")

# modifica la lista in modo che gli elementi della lista siano ordinati in ordine alfabetico inverso (Z-A)
lista_località.sort(reverse=True)
print(f"Lista dopo il secondo sort(): {lista_località}")