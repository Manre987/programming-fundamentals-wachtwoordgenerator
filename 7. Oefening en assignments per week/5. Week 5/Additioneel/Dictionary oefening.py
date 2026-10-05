# Oefening 1 - Gemiddelde berekenen
def gemiddelde(getallen):
    totaal = sum(getallen)
    aantal = len(getallen)
    return totaal / aantal


getallen = [5, 7, 8, 10, 6]

resultaat = gemiddelde(getallen)

print("Het gemiddelde is:", resultaat)


# Oefening 2 - Woorden tellen

zin = input("Geef een zin: ")

woorden = zin.split()

print("Aantal woorden:", len(woorden))


# Oefening 3 - Palindroom

woord = input("Geef een woord: ")

woord = woord.lower()

if woord == woord[::-1]:
    print("Het is een palindroom")
else:
    print("Het is geen palindroom")


# Oefening 4 - Bibliotheek

boeken = {
"Harry Potter": "Fantasy",
"De Hobbit": "Fantasy",
"Pride and Prejudice": "Roman",
"De Da Vinci Code": "Thriller"
}

print("Alle boeken:")

for boek in boeken:
    print(boek, "-", boeken[boek])

genre = input("Welk genre wil je zoeken? ")

print("Boeken in dit genre:")

for boek in boeken:
    if boeken[boek].lower() == genre.lower():
        print(boek)