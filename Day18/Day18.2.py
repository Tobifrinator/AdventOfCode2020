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
		formula=formula.replace(deep_par, plus_before_multiply(deep_par[1:-1]))
	formula=handle_parantheses(formula)
	return formula

"""
calculate all subsums and multiply them: -> + before *
"""
def plus_before_multiply(formula):
	sums=formula.split(' * ')
	formula=str(eval(sums[0]))
	for sum in sums[1:]:
		formula=formula+" * "+str(eval(sum))
	return str(eval(formula))

"""
calculate: resolve all parentheses, then calculate from left to right
"""
def calculate(formula):
	formula=handle_parantheses(formula)
	return int(plus_before_multiply(formula))


def main():
	data=open('data.txt','r')
	formulas=data.read().split("\n")
	sum=0
	#calculate the result of every row and sum it up
	for formula in formulas:
		formula=handle_parantheses(formula)
		sum=sum+calculate(formula)
	print("The sum of the result of all rows when using add-before-multiply is",sum)

if __name__ == "__main__":
	main()