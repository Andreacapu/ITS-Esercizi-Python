def rotate_left(elements: list, k: int) -> list:
    k=k%len(elements)
    return elements[k:]+elements[:k]