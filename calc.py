# Salary calc 

def calc(salary, hours):
    amount = 0
    comparison = []
    amount = int(salary) * hours * 52
    for i in [int(amount * 0.58), int(amount * 1.18), int(amount * 0.79)]:
        comparison.append(i)
    return "CAD " + str(amount) + " | GBP " + str(comparison[0]) + " | NZD " + str(comparison[1]) + " | USD " + str(comparison[2])

print calc(56.23, 35)