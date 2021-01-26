from expences import all_expences

budget = 0

total_expences = sum(all_expences.values())

def set_budget():
    global budget
    budget = int(input("Set a budget for this month: "))

def monthly_statement():
    print("Your expences this month were total", total_expences, ".")

    for category, total in all_expences.items():
        print("You spent {:.2f} on {} this month.".format(total, category))
    
    if budget < total_expences:
        print("Your expences exceeded your budget by {:.2f}.".format(abs(budget-total_expences)), end="\n\n")
    else:
        print("You managed to fall below your budget and saved {:.2f}.".format(abs(budget-total_expences)), end="\n\n")


def main():
    print("Welcome to your monthly expence tracker.", end="\n\n")
    set_budget()
    monthly_statement()
    print("Thanks for using monthly expence tracker.")


main()
