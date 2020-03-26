def find_max(liste):
    max = liste[0]
    for number in liste:
        if number > max:
            max = number
    return max
