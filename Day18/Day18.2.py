import re

def handle_parantheses(formula):
	deepest_parantheses=re.findall(r'\(\d+ [+* \d]* \d+\)',formula)
	if deepest_parantheses==[]:
		return formula

	for deep_par in deepest_parantheses:
		#print(deep_par)
		formula=formula.replace(deep_par, plus_before_multiply(deep_par[1:-1]))
	formula=handle_parantheses(formula)
	return formula

def plus_before_multiply(formula):
	sums=formula.split(' * ')
	formula=str(eval(sums[0]))
	for sum in sums[1:]:
		formula=formula+" * "+str(eval(sum))
	return str(eval(formula))


def calculate(formula):
	formula=handle_parantheses(formula)
	return int(plus_before_multiply(formula))


def main():
	data=open('data.txt','r')
	formulas=data.read().split("\n")
	sum=0
	for formula in formulas:
		formula=handle_parantheses(formula)
		sum=sum+calculate(formula)
	print(sum)

if __name__ == "__main__":
	main()