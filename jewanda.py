
print("Hello Python 1")

theFile = open("./raw/gardes_yde.csv", "r", encoding="utf-8")
#lines = tuple(theFile)
gardeur = 0
finalFile = ""
lespharma = ""
for ligne in theFile.__iter__():
    #Si "Garde" est dans la ligne, on trouve la date du jour de garde
    if "Garde" in ligne:
        #on coupe la ligne en 3 morceaux
        ligneSplit = ligne.split("   ")
        #On prend les deuxième morceau de la ligne coupée et on enlève l'espace qui est avant
        ligneSplitStrip = ligneSplit[1].strip()
        #On coupe le deuxième morceaux contenant les dates en deux morceaux
        lesDates = ligneSplitStrip.split("-")

        date1 = lesDates[0].strip()
        date2 = lesDates[1].strip()

        theDate = date1[5:-5]
        print("Date 1: " + theDate)
        gardeur = gardeur + 1

        if gardeur == 1:
            finalFile = theDate + ";"
        else:
            finalFile = finalFile +  lespharma + "\n" +  theDate.strip() + ";"

            lespharma = ""
    elif "Localisation" in str(ligne) or "Semaine" in str(ligne):
        #do nothing
        nothing= 0
    elif "Nombre de" in str(ligne):
        nothing = 0
    else:
        onePharma = str(ligne).split(";")
        lespharma = lespharma + " #" + onePharma[2]
       # print("les pharma: " + lespharma + "\n")
finalFile = finalFile + lespharma

#create a new file and save the date inside
formattedFile = open("./raw/gardes_yde_trans.csv", "w")
formattedFile.write(finalFile)
formattedFile.close()