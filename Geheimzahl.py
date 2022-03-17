    geheimzahl = 1337
    eingabe = 0
    zaehler = 0

    while eingabe != geheimzahl:
        eingabe = int(input("Bitte eine Ganzzahl eingeben: "))
        
	if eingabe < geheimzahl:
            print("Ihre Eingabe war zu klein")
        zaehler = zaehler +1

    print("Sie haben die Zahl erraten")
