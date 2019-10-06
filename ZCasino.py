import random
import math

while 1:
    wallet = input("De combien nous créditons votre porte-feuille :\n")
    
    if wallet.isdigit():
        wallet = int(wallet)
        break
    
    else :
        print ("ce n'est pas une somme !")

win_number = random.randrange(50) 
parti = "o"

while not parti in "nN" :
    choice_number = input("Sur quel numéro miser entre 0 et 49 ? \n")
    mise = input("Quel somme miser dessus ? \n")
    
    if choice_number.isdigit() and mise.isdigit() :
        choice_number = int (choice_number)
        mise = int (mise)
        
        if choice_number in range (50) :
            
            if choice_number == win_number :
                mise *= 3
                wallet += mise 
                win_number = random.randrange(50)
                print(f"Jackpot , vous avez gagné {mise}$ votre porte-feuille est de {wallet}$")
                parti = input("Rejouer ? (o/n) : ")
            
            elif (choice_number % 2 == 0 and win_number % 2 == 0) or (choice_number % 2 == 1 and win_number % 2 == 1):
                mise += math.ceil(mise/2)
                wallet += mise 
                win_number = random.randrange(50)
                print(f"Bravo les 2 numero sont de la meme couleur, vous avez gagné {mise}$ votre porte-feuille est de {wallet}$")
                parti = input("Rejouer ? (o/n) : ")
                
            else :
                wallet -= mise
                print (f"Dommage , votre porte-feuille est à {wallet}$ ")
                parti = input("Rejouer ? (o/n) : ")
                win_number = random.randrange(50)
        else :
            print("Entrer un numero svp entre 0 et 49")
    
    else :
        print("Entrer que des nombres svp ")

if wallet < 0 :
    print (f"merci d'avoir jouer votre porte-feuille est negatif vous nous devez {wallet}$ ")
else:
    print(f"merci d'avoir jouer votre porte-feuille est de : {wallet}$")
     
    

