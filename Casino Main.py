
first_name = input("Wat is je voornaam? ").strip().title()      #Deze functies gevonden in de lesstof BONUS onder werken met tekst
infix = input("Wat is het tussenvoegsel? (laat leeg als je er geen hebt) ").strip().lower()
last_name = input("Wat is je achternaam? ").strip().title()

while True:     #zorgen dat de invoer klopt (while)
    gender = input("Wat is je geslacht? (man/vrouw/anders): ").strip().lower()

    if gender == "man":
        salutation = "meneer"
        break
    elif gender == "vrouw":
        salutation = "mevrouw"
        break
    elif gender == "anders":
        salutation = ""
        break
    else:
        print("Ongeldige invoer, kies uit man, vrouw of anders")
#Inspringen toegevoegd omdat deze code zonder niet functioneert.
#Break toegevoegd omdat hij bleef rekenen. Zie hoofdstuk 5 (deze had ik al gelezen)

birthday = input("Wat je geboortedatum? (dd-mm-yyyy) ").strip()
from datetime import date
MIN_AGE = 18
birth_day, birth_month, birth_year = birthday.split("-")
birth_day = int(birth_day)
birth_month = int(birth_month)
birth_year = int(birth_year)

today = date.today()
age = today.year - birth_year
#wou het op de dag gelijk hebben, again (google is your best friend)
if today.month < birth_month:
    age = age -1
elif today.month == birth_month and today.day < birth_day:
    age = age -1

if age < 18:
    print("Je bent jonger dan 18 en mag niet spelen")
    exit(1) #afsluiten op de leeftijdscheck

if infix:
    full_name = f"{first_name} {infix} {last_name}"
else:
    full_name = f"{first_name} {last_name}"


initial_budget = float(input("Wat is je startbudget?: "))

ENTRANCE_FEE = 10.00
MANDATORY_DRINK= 5.00
GAMBLING_TAX= 2.00
#de punt geeft een float waarde

fixed_costs = ENTRANCE_FEE + MANDATORY_DRINK + GAMBLING_TAX
balance = initial_budget - fixed_costs

print("Casino de Gouden Driehoek")
print("-" * 25)

if salutation:
    print(f"Welkom, {salutation} {full_name}")
else:
    print(f"Welkom, {full_name}")
#gender aangepast naar salutation omdat hij anders man of vrouw toont

print ("")
print (f"{'Startbudget:':<15}€ {initial_budget:>4.2f} ")
print (f"{'Vaste kosten:':<15}€ {fixed_costs:>4.2f} ")
print (f"{'Saldo:':<15}€ {balance:>4.2f} ")
#.2 Notatie gebruikt om twee decimalen achter de punt te laten zien (google is your best friend)

print ("")
if balance > 0:
    print("Je hebt nog genoeg budget voor toegang tot het casino")
else:
    print ("Je hebt niet voldoende budget voor toegang tot het casino")

print ("_" * 25)
print ("Welkom bij de Roulettetafel")

#round_number = 1   deze moest uit de loop wegens de bonus

import random

COLOR_STAKE = 2
ODD_EVEN_STAKE = 1.5
GREEN_STAKE = 5
NUMBER_STAKE = 10

while True:
    print("Kies één van de volgende opties:")
    print ("1. Rood")
    print ("2. Zwart")
    print ("3. Even")
    print ("4. Oneven")
    print ("5. Groen")
    print ("6. Getal")
    print ("0. Stop")

    roulette_choice = int(input("Kies je gok (0 om te stoppen): ")) #aangepast naar roulette_choice om het visueel makkelijker te maken

    if roulette_choice == 0:
        break

    if roulette_choice not in (1, 2, 3, 4, 5, 6):
        print ("Ongeldige keuze, probeer opnieuw")
        continue

    #voor de bonus ingevoegd, bij zes zou namelijk wel een getal ingevoerd moeten worden
    chosen_number = -1
    if roulette_choice == 6:
        chosen_number = int(input("Op welk getal wil je inzetten (0 t/m 36) "))
        if chosen_number < 0 or chosen_number > 36:
            print ("Kies een getal van 0 t/m 36")
            continue


    stake = float(input("Hoeveel wil je inzetten? € "))

    if stake <=0:   #zonder inzet niet te spelen
        print("Je inzet moet hoger zijn dan 0.")
        continue

    if stake > balance:
        #bij te laag saldo moet je niet door kunnen spelen
        print ("Je hebt niet genoeg saldo. Pas je inzet aan of stop")
        continue

    #inzet van het saldo afhalen, punt 12
    balance -= stake

    #het spinnen, dus alle variabele keuzes
    spin = random.randint(0,36)
    #Deze aangepast voor de bonus, zodat deze echt random ging. Het advies was om random te importeren zie regel 85

    #stroomschema nabouwen
    if spin == 0:
        color = "groen"
        odd_even = "geen"
    elif spin <= 18:
        if spin % 2 == 0:
            color = "zwart"
            odd_even = "even"
        else:
            color = "rood"
            odd_even = "oneven"
    else:
        if spin % 2 == 0:
            color = "rood"
            odd_even = "even"
        else:
            color = "zwart"
            odd_even = "oneven"

    print (f"De bal valt op {color} ({spin}).")

    #Waarheidstabel. Wat heeft de speler gewonnen?
    win = False
    multiplier = 0  #bonusopdracht hierbij verschillende uitkomsten voor winst
    if roulette_choice == 1 and color == "rood":
        win = True
        multiplier = COLOR_STAKE
    elif roulette_choice == 2 and color == "zwart":
        win = True
        multiplier = COLOR_STAKE
    elif roulette_choice == 3 and odd_even == "even":
        win = True
        multiplier = ODD_EVEN_STAKE
    elif roulette_choice == 4 and odd_even == "oneven":
        win = True
        multiplier = ODD_EVEN_STAKE
    elif roulette_choice == 5 and color == "groen":
        win = True
        multiplier = GREEN_STAKE
    elif roulette_choice == 6 and spin == chosen_number:
        win = True
        multiplier = NUMBER_STAKE

    if win:
        payout = stake * multiplier #payout toegevoegd als variabele wegens de bonus, hierbij moet de mutliplier goed doorrekenen
        balance += payout
        print (f"Je wint € {payout - stake:.2f}") #.2f voor 2 decimalen #payout - stake anders is het niet de echte winst
    else:
        print (f"Je verliest € {stake:.2f}") #.2f voor 2 decimalen

    print(f"Nieuw Saldo: € {balance: .2f}") #.2f voor 2 decimalen
    print ()

    #round_number += 1
    #naar beneden verplaatst, deze ging bij het testen soms mee in een ongeldige invoer, dit is volgens google de oplossing, getest en lijkt te werken
    #Eruit gehaald voor de bonus

#Als we stoppen met het spel
print(f"Eindsaldo: € {balance:.2f}")
print("Bedankt voor het spelen, tot de volgende keer!")



