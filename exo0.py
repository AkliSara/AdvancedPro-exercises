ppl=int(input("how many people are there?"))
cars=int(input("how many ppl can a car handle?"))
if ppl%cars==0 :
    print(f"le nobre de taxi est : {ppl//cars}")
else :
     print(f"le nobre de taxi est : {(ppl//cars)+1}")