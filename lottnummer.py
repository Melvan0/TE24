lottnummer = [15, 8, 22, 1, 8, 45, 8, 19]

lottnummer = sorted(lottnummer)
print(lottnummer)

mindre_tal = lottnummer[:3]
print(mindre_tal)

antal_åttor = lottnummer.count(8)
print(antal_åttor)

for index, mindre_tal in enumerate(mindre_tal):
    print(f"På index {index} finns talet {mindre_tal}")