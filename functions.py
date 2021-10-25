
import os
import platform
import classes

def getMostRecentBudget(*args):

		# /private/var/mobile/Library/Mobile Documents/iCloud~com~omz-software~Pythonista3/Documents/budget-keeper/main.py
    script_dir = os.path.dirname(os.path.realpath(__file__))
    higher_dir = '/'.join(script_dir.split('/')[:-1]) # how many dirs to go up
    budget_dir = higher_dir + '/budgets'
    budget_list = os.listdir(budget_dir)
    budget_name = sorted(budget_list, reverse=True)[0]
    budget_path = budget_dir + '/' + budget_name
    # /private/var/mobile/Library/Mobile Documents/iCloud~com~omz-software~Pythonista3/Documents/budgets/<latest budget>.txt

    return budget_path

def expense(budget, *args):
    
    value = float(args[1])
    name = args[2].title()
    section = budget.buy_sections[args[3].title()]

    item = f'{value:.2f} {name}'

    expense = classes.Item(f'- {item}')
    section.items.append(expense)

    charge = classes.Item(f'+ {item}')
    budget.credit_sections['Charges'].items.append(charge)

def expenseh(budget, *args):

    value = float(args[1])
    name = args[2].title()

    if '(H)' not in name:
        name = ' '.join(name.split() + ['(H)'])

    item = f'{value:.2f} {name}'
    
    charge = classes.Item(f'+ {item}')
    budget.credit_sections['Charges'].items.append(charge)

def credit(budget, *args):

    value = float(args[1])
    name = args[2].title()
    section = budget.buy_sections[args[3].title()]

    item = f'{value:.2f} {name}'
    
    expense = classes.Item(f'+ {item}')
    section.items.append(expense)

    charge = classes.Item(f'- {item}')
    budget.credit_sections['Charges'].items.append(charge)

def credith(budget, *args):
    
    value = float(args[1])
    name = args[2].title()

    if '(H)' not in name:
        name = ' '.join(name.split() + ['(H)'])

    item = f'{value:.2f} {name}'
    
    charge = classes.Item(f'- {item}')
    budget.credit_sections['Charges'].items.append(charge)

def deposit(budget, *args):

    value = float(args[1])
    name = args[2].title()

    item = f'{value:.2f} {name}'
    
    expense = classes.Item(f'+ {item}')
    budget.buy_sections['Spend'].items.append(expense)

def withdrawal(budget, *args):
    
    value = float(args[1])
    name = args[2].title()

    item = f'{value:.2f} {name}'
    
    expense = classes.Item(f'- {item}')
    budget.buy_sections['Spend'].items.append(expense)

def combine(budget, *args):

    section = budget.buy_sections[args[1].title()]

    if not section.done:

        value = section.remainder
        name = 'Combine'
        
        combine_from = classes.Item(f'- {value:.2f} {name}')
        combine_from.remainder = 0.00
        combine_from.done = True

        combine_to = classes.Item(f'+ {value:.2f} {name}')

        section.items.append(combine_from)
        budget.buy_sections['Spend'].items.append(combine_to)

        section.done = True
