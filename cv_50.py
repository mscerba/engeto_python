"""
Naším úkolem je vytvořit program, který vezme vstup v 24hodinovém formátu a převede jej do anglického času, který bude zahrnovat zkratky PM a AM.

Tvé úkoly:

Získej vstup uživatele do proměnné time
Rozděl do listu vstup od uživatele do proměnné hours a mins.
Uprav proměnou 'hours' tak, aby se do proměnné adjusted_hours místo 24 hodinového formátu (např.: 17) uložil formát anglický (např.: 5).
Do proměnné daytime vyber odpovídající string z dvojčlenného listu ['AM', 'PM']

Vytiskni převedený čas.
"""

hours = []
mins = []
adjusted_hours = []
daytime = []

time = input("Please enter your time: ")
hours = int(time[0:2])
mins = time[3:5]



if hours < 12:
    adjusted_hours = hours
    daytime.append("AM")
elif hours == 12:
    adjusted_hours = 12
    daytime.append("PM")
elif hours > 12 and hours <= 24:
    adjusted_hours = hours - 12
    daytime.append("PM")


print(f'Converted to English format: {adjusted_hours}:{mins} {daytime[0]}')
