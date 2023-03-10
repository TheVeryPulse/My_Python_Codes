#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
# Example Input
#```
#Welcome to the tip calculator!
#What was the total bill? $124.56
#How much tip would you like to give? 10, 12, or 15? 12
#How many people to split the bill? 7
#```

# Example Output

#```
#Each person should pay: $19.93
#```
print ("Welcome to the tip calculator!")
total_bill = float (input ("What was the total bill? "))
tip = int (input ("How much tip would you like to give? 10, 12, ir 15? "))
num_people = int (input ("How many people to split the bill? "))
bill_each = (total_bill * (1 + tip / 100)) / num_people
print ("Each person should pay: " + str(round(bill_each, 2)))