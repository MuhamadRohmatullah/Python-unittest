import unittest

def Grade(nilai):

    if nilai >= 90 :
       print("A")

    elif nilai >= 80 and nilai <=  89:
        print("B")

    elif nilai >= 70 and nilai <= 79 :
        print("C")

    elif nilai >= 60 and nilai <= 69 :
        print("D")

    elif nilai <= 59:
        print("E")


Grade(79)