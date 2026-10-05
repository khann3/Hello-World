# Kiersten Hannon
# Homework 2
# 10/01/2026

# Homework 2: Loan Amortization
print("Homework 2: Loan Amorization")
# User inputs
principal = float(input("Please enter the loan amount:"))
annual_interest_rate = float(input("Please enter the annual interest rate:"))
loan_length = int(input("Please enter the loan length"))

print("-"*20)

# Processing 
annual_interest_decimal = annual_interest_rate/100
monthly_interest_rate = annual_interest_decimal/12
num_payments = loan_length * 12
# Calculate monthly payment. Monthly payment formula = P * (r * (1 + r)**n) / ((1 + r)**(n - 1))
monthly_pmt = principal * (monthly_interest_rate * (1 + monthly_interest_rate)**num_payments)/(((1 + monthly_interest_rate)**num_payments)- 1)
print(f"Monthly Payment: ${monthly_pmt:.2f}")

print("-"*20)

# Print column headers
print(f"{'Month':>5} {'Payment':>10} {'Principal':>12} {'Interest':>10} {'Balance':>12}")
# Loop to print values for each month
balance = principal 
for month in range (1, num_payments + 1): # Repeat code for each month until you get to # of pmts inputted
    interest = balance * monthly_interest_rate
    principal_paid = monthly_pmt - interest
    balance = balance - principal_paid
    print(f"{month:>5} {monthly_pmt:>10,.2f} {principal_paid:>12,.2f} {interest:>10,.2f} {balance:>12,.2f}")
 
print("-"*20)
print("End of Homework 2.")
    
