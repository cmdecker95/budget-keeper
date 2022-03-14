import sys
import classes
import functions


def main():
    """Docstring: `main`
    Updates budget file, given arguments passed from Shortcut.

    Shortcut will encode and pass a string for function selection.
    Script reaches for budget file via relative pathing, reads it, and writes over it.
    - Reading is done by creating objects out of the budget file.
    - Writing paradigm is defined by the function."""

    # Shortcut splits user input by line break, then passes each line as an argument.
    args = sys.argv[1:]

    # Finds the budget file, and converts it to a Budget object
    budget_path = functions.get_most_recent_budget()
    my_budget = classes.Budget(budget_path)

    # Call selected function to manipulate the Budget object
    if args[0] == 'expense':
        functions.exp_cred(my_budget, '-', '+', *args)

    elif args[0] == 'expenseh':
        functions.exp_cred_h(my_budget, '+', *args)

    elif args[0] == 'credit':
        functions.exp_cred(my_budget, '+', '-', *args)

    elif args[0] == 'credith':
        functions.exp_cred_h(my_budget, '-', *args)

    elif args[0] == 'deposit':
        functions.deposit(my_budget, *args)

    elif args[0] == 'withdrawal':
        functions.withdrawal(my_budget, *args)

    elif args[0] == 'combine':
        my_budget.calculate_budget()
        functions.combine(my_budget, *args)

    else:
        print('Invalid function')

    # Polish up the budget file, then calculate and output final values
    my_budget.calculate_budget()
    my_budget.current_budget()


if __name__ == '__main__':
    main()
