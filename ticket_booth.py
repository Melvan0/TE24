

price = 200
age = int(input("Hur gammal är du? "))

while age < 0:
    age = int(input("Är du helt dum i huvudet? Du kan ju inte vara mindre än 0 år! Försök igen eller stick härifrån! 😤 "))

if age < 18:
    price = price * 0.8
elif age > 64:
    price = price * 0.7
else:
    price = price

print("Din biljett kostar ", price, "KR! 😁")