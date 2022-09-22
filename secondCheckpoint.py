def reverse_name():

    first_name = input("Your first name")
    last_name = input("Yourlast name ")
    print(last_name + " " + first_name )

def computes_value():
    n = int(input("Enter a number:"))
    print(n + int(str(n) + str(n)) + int(str(n) + str(n) + str(n)))

def even_or_odd():
    n = int(input("Enter your number:"))
    if n % 2 == 0 : 
        print("Le nombre est pair")
    else:
        print("Le nombre est impair")
    
def divisible_by_seven():
    for i in range(2000,3201):
        if i % 7 == 0 and i % 5 != 0:
            print(i, end = ",")
    print("")

def factorielle():
    n = int(input("Entrer un nombre"))
    result = 1
    for i in range(1,n+1):
        result = result * i 
    print(result)


def remove_odd_index():
    string = input("Enter your string: ")
    result = ""
    for i in range(len(string)):
      if i % 2 == 0:
        print(string[i], end = "")
        result = result + string[i]
    print(result)

def discount():
    price = int(input("Enter the price: "))
    if price >= 500:
        print("The discount is " + str(price * 0.5))
    elif price >= 200 and price < 500:
        print("The discount is " + str(price * 0.3))
    else:
        print("The discount is " + str(price * 0.1))
