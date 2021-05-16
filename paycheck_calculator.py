#This program can be used by employees of a clothing store to calculate their take home pay after sales commissions or wages with any purchases deducted. 

def get_user_input(message):
  while True:
    try:
      value = float(input(message))
      break
    except ValueError:
      print("Please enter a number instead")
  return value

employee_sales = get_user_input("Total Sales for 2 week period: ")
hours_worked = get_user_input("Number of hours worked in 2 week: ")
price_sweater = get_user_input("Enter price of Sweater: ")
price_shirt = get_user_input("Enter price of Shirt: ")
price_pants = get_user_input("Enter price of Pants: ")
price_gift = get_user_input("Enter price of Gift: ")

discount_sweater = 0.35 * price_sweater   #Employee uniform gets 65% discount
discount_shirt = 0.35 * price_shirt   #Employee uniform gets 65% discount
discount_pants = 0.35 * price_pants   #Employee uniform gets 65% discount
discount_gift = 0.60 * price_gift   #Gifts get 40% discount

if discount_sweater >= 110:       #Sales tax for items >= 110, items less than 110 have no sales tax
  discount_sweater = discount_sweater * 1.04

if discount_shirt >= 110:       
  discount_shirt = discount_shirt * 1.04

if discount_pants >= 110:       
  discount_pants = discount_pants * 1.04

if discount_gift >= 110:      
  discount_gift = discount_gift * 1.04

cost_purchases = discount_sweater + discount_shirt + discount_pants + discount_gift  #Sum of Purchases          
print("Total purchases including sales tax (if needed) and discount: ${:.2f} ".format(cost_purchases))

commission = 0.095 * employee_sales   #Commission is 9.5% on sales
print("commission: ${:.2f} ".format(commission))

wage = 12.5 * hours_worked  #Wage is $12.50 an hour or 9.5% commission on sales, whichever is higher

if wage < commission:
  wage = commission

take_home_pay = 0.7 * wage    #take home pay is calculated by deducting 30% tax/benefits
print("Take Home Pay: ${:.2f} ".format(take_home_pay)) 

paycheck = take_home_pay - cost_purchases
print("Paycheck including purchases: ${:.2f} ".format(paycheck))

