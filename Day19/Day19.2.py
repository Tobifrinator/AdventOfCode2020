import re
def resolve_rules(rules):
	#based will be the dict where all our baserules are stored, meaning that these rules only contain characters, not numbers / references to other rules
	based={}
	# if a rule still contains references to other rules, this will become True and another round is will be done
	change_necessary=False
	for rule_nr in rules:
		baserules=re.findall(r'^[^\d]*$',rules[rule_nr])
		if(baserules!=[]):
			based[rule_nr]=baserules[0]
		else:
			change_necessary=True

	#replace references to other rules that are baserules with the string of this baserule
	for key in based:
		for rule_nr in rules:
			if (' '+str(key)+' ') in rules[rule_nr]:
				rules[rule_nr]=rules[rule_nr].replace(' '+str(key)+' ', ' (' + based[key] + ') ').replace('") ("', '')
	if(change_necessary):
		rules=resolve_rules(rules)
	return rules

def main():
	#parsing input, the only changes that have to be done for day 2 is the recursion of rule 8 and 11, we do this directly in the input file
	#
	#rule 8: 42 | 42 8 -> as many 42 as we want -> rule 8 is now 8: 42 +
	#rule 11: 42 31 | 42 11 31 -> has to match something like 42 42 42 42 31 31 31 31 , or, 42*n 31*n, we just hardcode it for all 0<n<10 , if the puzzle solution fails, we could just increase the maximum
	#11: ( 42 31 )| ( 42 31 )| ( 42 42 31 31 )| ( 42 42 42 31 31 31 )| ( 42 42 42 42 31 31 31 31 )| ( 42 42 42 42 42 31 31 31 31 31 )| ( 42 42 42 42 42 42 31 31 31 31 31 31 )| ( 42 42 42 42 42 42 42 31 31 31 31 31 31 31 )| ( 42 42 42 42 42 42 42 42 31 31 31 31 31 31 31 31 )| ( 42 42 42 42 42 42 42 42 42 31 31 31 31 31 31 31 31 31 )
	data=open('data2.txt','r')
	rulemess, messages=data.read().split("\n\n")
	rulemess=rulemess.split('\n')
	messages=messages.split('\n')
	#order the rules in a dictionary
	rules={}
	for rule in rulemess:
		rules[int(rule.split(":")[0])]=rule.split(":")[1]+" "
	#we want to see how many messages match rule0, we resolve the rules, take rule 0 and remove all the " and spaces so that we can use this rule as a regex
	#after that, count the messages that match our regex
	raw_rule0="^"+resolve_rules(rules)[0].replace('"','').replace(' ','')+"$"
	matches=0
	for message in messages:
		if(re.findall(raw_rule0, message)!=[]):
			matches=matches+1
	print("The number of messages that match Rule 0 is",str(matches)+". \n\nRule 0 is:\n"+raw_rule0)
if __name__ == "__main__":
	main()