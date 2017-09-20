# Pas de uitwerking van exercise 3_2 aan en geef ook een melding als de gebruiker niet mag stemmen!

leeftijd = int(input("wat is je leeftijd? "))
paspoort = str(input("heb je een nederlands paspoort? "))

if leeftijd >= 18 and paspoort == "ja":
    text = "ja je mag stemmen!"
    print(text)

else:
    text1 = "je mag niet stemmen"
    print(text1)