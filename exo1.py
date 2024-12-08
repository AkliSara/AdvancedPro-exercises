prixT=15.50
name=input("Please enter your name:")
if name!='VIP':
    nb=int(input("combien de tickets?"))
    prix=prixT*nb
    print(f"le prix total est : {prix}")
    print("Enjoy your tickets!")
else :
    print("enjoy the show for free")