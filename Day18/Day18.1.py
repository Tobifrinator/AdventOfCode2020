import re

"""
calculate the content of the innermost parantheses and replace the parantheses with the result
call it, until all parentheses levels are resolved and no parantheses remain
"""
def handle_parantheses(formula):
	deepest_parantheses=re.findall(r'\(\d+ [+* \d]* \d+\)',formula)
	if deepest_parantheses==[]:
		return formula

	for deep_par in deepest_parantheses:
		formula=formula.replace(deep_par, calculate_left_to_right(deep_par[1:-1]))
	formula=handle_parantheses(formula)
	return formula

"""
calculate from left-to-right, disregarding multiply-before-add
"""
def calculate_left_to_right(formula):
	calculation=formula.split()
	result=calculation[0]
	for i in range(1,len(calculation),2):
		operation=result+calculation[i]+calculation[i+1]
		result=str(eval(operation))
	return(result)

"""
calculate: resolve all parentheses, then calculate from left to right
"""
def calculate(formula):
	formula=handle_parantheses(formula)
	return int(calculate_left_to_right(formula))


def main():
	data=open('data.txt','r')
	formulas=data.read().split("\n")
	sum=0
	#calculate the result of every row and sum it up
	for formula in formulas:
		formula=handle_parantheses(formula)
		sum=sum+calculate(formula)
	print("The sum of the result of all rows when disregarding multiply-before-add is",sum)

if __name__ == "__main__":
	main()