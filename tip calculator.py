#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Write your code below this line 👇
print("welcome to tip calculator")
bill=float(input("What was the total bill? $"))
tip=int(input("What percentage tip would you like to give? "))
tip_amount=(bill*tip)/100
split_amt=int(input("how many people to split the bill? "))
divided_amt=(bill+float(tip_amount))/split_amt
final_amt_each=round((float(divided_amt)),2)
final_amt_each="{:.2f}".format(final_amt_each)    #we changed float value to sting inorder to fill the space with 0's
print(f"each person should pay: ${final_amt_each}")
