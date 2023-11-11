print ("Welcome to the Tip Calculator!")

Total_Bill = int(input ("Please enter the total amount of the bill: $"))

Tip = int(input ("How much percentage of tip would you like to give?: "))

People = int(input ("Amongst how many people is the bill expected to be split?: "))


Bill_With_Tip = ((Tip * Total_Bill) / 100) + Total_Bill

Split_Share = Bill_With_Tip / People

print (f"Each person's share is: $ {Split_Share: .2f}")