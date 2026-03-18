priser = [100, 500, 20, 150, 120000000, 56, 7, 15]

def uträkning():
    totalsumma = 0
    for index, pris in enumerate(priser):
        if (index + 1) % 5 == 0:
            pris = 0
        print(index, pris)
        totalsumma += pris
    if 1000 > totalsumma > 500:
        totalsumma *= 0.9
    elif totalsumma > 1000:
        totalsumma *= 0.8
    print("\n", totalsumma, "kr")

uträkning()