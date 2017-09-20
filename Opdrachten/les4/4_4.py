# Schrijf (en test) een functie new_password() die 2 parameters heeft: oldpassword en newpassword.
# De return-waarde is True als het nieuwe password voldoet aan de eisen. Het nieuwe password wordt
# alleen geaccepteerd als het verschilt van het oude password èn als het minimaal 6 tekens lang is. Als
# dat niet zo is, is de return-waarde False.
# Optioneel: zorg dat het nieuwe password minstens 1 cijfer moet bevatten!

import re

def new_password(oldpassword, newpassword):
    if oldpassword != newpassword and len(newpassword) >= 6 and re.search('[0-9]',newpassword):
        print('True')
    else:
        print('False')

new_password('henkkk', 'henkkq7')