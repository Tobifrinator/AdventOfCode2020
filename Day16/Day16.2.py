import re


#remove the flawed tickets. if a ticket has a value that is not in valid_values, the ticket is invalid and removed
def remove_flawed_tickets(nearby_tickets, valid_values):
	valid_tickets=[]
	for nearby_ticket in nearby_tickets:
		valid=1
		for value in nearby_ticket.split(','):
			valid=valid*valid_values[int(value)]
		if valid==1:
			valid_tickets=valid_tickets+[nearby_ticket]
	return valid_tickets


#convert the rules in a better to use form using a dictionary
def create_rules_dict(ticket_rules):
	rules={}
	for ticket_rule in ticket_rules:
		rulename=ticket_rule.split(': ')[0]
		values=list(map(int,re.findall(r"\d+", ticket_rule)))
		rules[rulename]=values
	return rules

def create_validity_array(ticket_rules):
	"""
	the values range from 0 to 999
	if the value i appears in the range that is specified in one rule, it is valid -> valid_values[i]=1
	else it remains 0
	"""
	valid_values=[0]*1000
	rule_ranges=[]
	for ticket_rule in ticket_rules:
		rule_ranges=rule_ranges+re.findall(r"\d+-\d+", ticket_rule)
	for rule_range in rule_ranges:
		beginning=int(rule_range.split("-")[0])
		end=int(rule_range.split("-")[1])
		for i in range(beginning, end+1):
			valid_values[i]=1
	return valid_values

def make_into_two_dimensions(tickets):
	two_dimensional=[[]]
	for ticket in tickets:
		two_dimensional=two_dimensional+[list(map(int,ticket.split(",")))]
	return two_dimensional[1:]

def field_assignment(valid_tickets, rules):
	assingment={}
	for key in rules:
		assingment[key]=[]
	for key in rules:
		for j in range(len(valid_tickets[0])):
			possible=True
			for i in range(len(valid_tickets)):
				if( (valid_tickets[i][j] not in range(rules[key][0], rules[key][1]+1)) and (valid_tickets[i][j] not in range(rules[key][2], rules[key][3]+1)) ):
					possible=False
			if(possible):
				assingment[key]=assingment[key]+[j]

	maxlen=0
	applied_reduction={}
	for key in assingment:
		maxlen=max(maxlen, len(assingment[key]))
		applied_reduction[key]=False
	while(maxlen!=1):
		maxlen=1
		for key in assingment:
			if(len(assingment[key])==1 and applied_reduction[key]==False):
				reduction_value=assingment[key][0]
				applied_reduction[key]=True
				break
		for key in assingment:
			if (len(assingment[key])!=1 and reduction_value in assingment[key]):
				assingment[key].remove(reduction_value)
		for key in assingment:
			maxlen=max(maxlen, len(assingment[key]))
	return assingment


def main():
	#parse the input data and split it into rules, my_ticket and nearby_tickets
	data=open('data.txt','r')
	ticket_rules, my_ticket, nearby_tickets=data.read().split('\n\n')
	my_ticket=my_ticket.split('\n')[1]
	ticket_rules=ticket_rules.split("\n")
	nearby_tickets=nearby_tickets.split("\n")[1:]

	#create array of valid values, remove the invalid tickets, add own ticket to valid tickets
	valid_values=create_validity_array(ticket_rules)
	valid_tickets=[my_ticket]+remove_flawed_tickets(nearby_tickets, valid_values)

	#create rules dictionary for later use and convert the valid tickets into an two dimensional array
	rules=create_rules_dict(ticket_rules)
	valid_tickets=make_into_two_dimensions(valid_tickets)

	#work out the field assignment
	assignment=field_assignment(valid_tickets,rules)
	
	#calculate the product of all fields on my ticket related to departure
	product=1
	for key in assignment:
		if "departure" in key:
			product=product*int(my_ticket.split(',')[assignment[key][0]])
	print("The product of all the fields on my ticket related to departure is",product)

if __name__ == "__main__":
	main()