# Modul random importieren
import random

# Programm im Endlosmodus laufen lassen
while True:

# Zufallsgenerator initialisieren
   random.seed()

# Zufallswerte und Berechnung
   a=random.randint(0,100)
   b=random.randint(1,100)
   c=a+b
   print("Die Aufgabe:",a,"+",b)

# Eingabe
   print("Bitte Ihre Antwort eingeben:")
   z=input()
   zahl=int(z)

# Ausgabe
   print("Ihre Eingabe:",z)
   print("Das Ergebnis:",c)

# Antworten vergleichen
   if(int(z)==int(c)):
      print("THE ANSWER IS CORRECT")
      break
   else:
      print("THE ANSWER IS WRONG")
   print("----------------------------------------")

   pass
