# Salary calc 

def calc(salary):
    amount = 0
    comparison = 0
    amount = salary * 35 * 52
    comparison = amount * 0.58
    return str(amount) + " | GDP " + str(comparison)

print calc(58)