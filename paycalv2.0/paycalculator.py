THR= input("How many hours have you worked per week?:")
HR= input("What is the pay per hour?:")
FTHR= float(THR)
FHR= float(HR)
CH= input("How many hours per week are you meant to work, as per the contract?:")
FCH=float(CH)
if FTHR>FCH:
    print("You have worked overtime,")
else:
    print("You have regular pay,")
YOURPAY= FTHR*FHR
print("your employee should pay you:", YOURPAY)