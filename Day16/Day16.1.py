import re

def create_rule_array(ticket_rules):
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

def main():
	#parse the input data and split it into rules, my_ticket and nearby_tickets
	data=open('data.txt','r')
	ticket_rules, my_ticket, nearby_tickets=data.read().split('\n\n')
	my_ticket=my_ticket.split('\n')[1]
	ticket_rules=ticket_rules.split("\n")
	nearby_tickets=nearby_tickets.split("\n")[1:]

	#create array of valid values
	valid_values=create_rule_array(ticket_rules)
	"""
	calculate ticket_scanning_error_rate:
	if value is not in valid_values, add value to ticket_scanning_error_rate
	"""
	ticket_scanning_error_rate=0
	for nearby_ticket in nearby_tickets:
		for value in nearby_ticket.split(','):
			value=int(value)
			ticket_scanning_error_rate=ticket_scanning_error_rate+(1-valid_values[value])*value
	print("The ticket scanning error rate is",ticket_scanning_error_rate)

if __name__ == "__main__":
	main()