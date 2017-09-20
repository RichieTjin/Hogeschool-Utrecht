# Maak een nieuwe Python file aan voor deze opdracht (vanaf nu is dat standaard en zal dat niet steeds
# meer bij de opdracht staan). Schrijf (en test) de functie som() die 3 parameters heeft: getal1, getal2
# en getal3. De return-waarde van de functie moet de som (optelling) van deze parameters zijn!

def som(getal1, getal2, getal3):
    getallen = [getal1, getal2, getal3]
    total = sum(getallen)
    print(total)

som(1, 2, 3)
