#simple if and else
applePrice=210
budget=200
if(applePrice<=budget):
    print("Add to cart")
else:
    print("Not under the budget")

#if,elif and else
applePrice=int(input("Enter the apple price(in $):"))
budget=int(input("Enter your budget(in $):"))
if(budget-applePrice>50):
    print("$",budget,"-","$",applePrice,"=","$",budget-applePrice)
    print("Add to cart")
elif(budget-applePrice<50 and budget-applePrice>0 ):
    print("$",budget,"-","$",applePrice,"=","$",budget-applePrice)
    print("You need to save atleast $50")
elif(budget-applePrice<0):
    print("$",budget,"-","$",applePrice,"=","$",budget-applePrice)
    print("Not under the budget")
else:
    print("$",budget,"-","$",applePrice,"=","$",budget-applePrice)
    print("Now, don't buy anything you have only $50")

#Nested elif
applePrice=int(input("Enter the apple price(in $):"))
budget=int(input("Enter your budget(in $):"))
if(budget-applePrice>50):
    print("Add to cart..")
elif(budget-applePrice<50):
    if(budget-applePrice>0):
        print("$",budget,"-","$",applePrice,"=","$",budget-applePrice)
        print("You have less than $50")
    elif(budget-applePrice<0):
        print("$",budget,"-","$",applePrice,"=","$",budget-applePrice)
        print("Not under the budget")
else:
    print("$",budget,"-","$",applePrice,"=","$",budget-applePrice)
    print("Now, don't buy anything you have only $50")