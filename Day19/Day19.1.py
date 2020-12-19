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
	data=open('data.txt','r')
	rulemess, messages=data.read().split("\n\n")
	rulemess=rulemess.split('\n')
	messages=messages.split('\n')
	rules={}
	for rule in rulemess:
		rules[int(rule.split(":")[0])]=rule.split(":")[1]+" "
	raw_rule0="^"+resolve_rules(rules)[0].replace('"','').replace(' ','')+"$"
	matches=0
	for message in messages:
		if(re.findall(raw_rule0, message)!=[]):
			matches=matches+1
	print("The number of messages that match Rule 0 is",str(matches)+". \n\nRule 0 is:\n"+raw_rule0)
if __name__ == "__main__":
	main()