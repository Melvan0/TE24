frukter = ["äpple", "banan", "äpple", "apelsin", "banan", "äpple"]

antal_frukter = {}

for index, frukt in enumerate (frukter):
    if frukt not in antal_frukter:
        antal_frukter[frukt] = frukter.count(frukt)

print(antal_frukter)