def calculate_simple_interest(principal, time, senior):
    if senior:
        rate = 12
    else:
        rate = 10
        si = (principal * rate * time) / 100
        return si
print(" == simple interest calculator ===")
principal = float(input("enter the principal amount:"))
time = float(input("enter the time in years: "))
senior_input = input("Is the customer a senior citizen? (yes/no): ").lower()
senior = senior_input == "yes"
interest = calculate_simple_interest(principal,time, senior)
print(f"\nsimple interest = {interest:.2f}")
