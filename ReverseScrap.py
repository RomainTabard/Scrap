import sys
import os

file = open("test.txt", "r")
resultat = open("resultat.txt", "w")

for line in file : 
    print (line)
    resultat.write(line)
resultat.close()
file.close()