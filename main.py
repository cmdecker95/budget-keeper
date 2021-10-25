
import platform
import sys
import classes
import functions

def main():

	system = platform.system()

	if system == 'Windows':
		function = input("Which function shall we run?")
		values = input("Enter your values separated by commas:")
		args = [function] + list(map(lambda x: x.strip(), values.split(',')))

	elif system == 'Darwin':
		args = sys.argv[1:]

	budget_path = functions.getMostRecentBudget(system, *args)
	
	my_budget = classes.Budget(budget_path)

	if args[0] == 'expense':
		functions.expense(my_budget, *args)

	elif args[0] == 'expenseh':
		functions.expenseh(my_budget, *args)
	
	elif args[0] == 'credit':
		functions.credit(my_budget, *args)
	
	elif args[0] == 'credith':
		functions.credith(my_budget, *args)

	elif args[0] == 'deposit':
		functions.deposit(my_budget, *args)

	elif args[0] == 'withdrawal':
		functions.withdrawal(my_budget, *args)

	elif args[0] == 'combine':
		my_budget.calculate_budget()
		functions.combine(my_budget, *args)

	else:
		print('Invalid function')

	my_budget.calculate_budget()

	my_budget.current_budget()

if __name__ == '__main__':
	main()
