def reverse_name():

    first_name = input("Your first name")
    last_name = input("Yourlast name ")
    print(last_name + " " + first_name )

def computes_value():
    n = int(input("Enter a number:"))
    print(n + int(str(n) + str(n)) + int(str(n) + str(n) + str(n)))

def even_or_odd():
    n = int(input("Enter your number:"))
    if n %2 == 0 : 
        print("Le nombre est pair")
    else:
        print("Le nombre est impair")
    
def factorielle():
    n = int(input("Entrer un nombre"))
    result = 1
    for i in range(1,n+1):
        result = result * i 
    print(result)

def replace():
    n = int(input("Supprimer les caractères à valeurs impaires"))
    for i in range(0,n):
        if (i%2 == 0):
            result = result
    print(result)
    
def odd_index_value():
    print("Bonjour")
    value = int(input("Entre votre valeur"))
    remaining_value = ""
    for i, c in enumerate(value):
        if i%2 == 1:
            remaining_value = remaining_value + c
    print(remaining_value)


def challenge():
    print("Bienvenue :")
    prix = int(input("Entrez un nombre"))
    if prix == 500:
            print("La remise est de" + str(prix*0.5))
    if prix < 500 and prix >= 200:
            print("La remise est de" + str(prix*0.3))
    if prix < 200:
            print("La remise est de" + str(prix*0.1))




    


