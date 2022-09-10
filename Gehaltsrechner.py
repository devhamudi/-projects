stundenlohn = input('Bitte deinen Stundenlohn eingeben: ')
arbeitsstunden = input('Bitte Arbeitsstunden pro Tag eingeben: ')
tag = int(arbeitsstunden) * int(stundenlohn)
monatsstunden = input('Bitte Arbeitstage im Monat eingeben: ')
monat = tag * int(monatsstunden)
jahr = monat * 12

print('Dein Stundenlohn beträgt ' + str(stundenlohn) + ' Euro')
print('Du verdienst ' + str(tag) + ' Euro pro Tag')
print('Du verdienst pro Monat ' + str(monat) + ' Euro')
print('Du hast ein Jahresgehalt von ' + str(jahr) + ' Euro')
input('Bitte beliebige Taste zum beenden drücken...')