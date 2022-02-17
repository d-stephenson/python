# Salary calc 

def calc(salary, hours):
    amount = 0
    comparison = []
    amount = salary * hours * 52
    for i in [int(amount * 0.58), int(amount * 1.18)]:
        comparison.append(i)
    return str(amount) + " " + str(comparison)

print calc(56.23, 35)