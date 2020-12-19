import re

def resolve_rules(rules):
	based={}
	change_necessary=False
	for i, rule in enumerate(rules):
		baserules=re.findall(r'^[^\d]*$',rule)
		if(baserules!=[]):
			based[i]=baserules[0]
		else:
			change_necessary=True

	for key in based:
		for i, rule in enumerate(rules):
			if str(key) in rule:
				rules[i]=rules[i].replace(str(key), '('+based[key]+')').replace('") ("', '').replace(' ','')
	if(change_necessary):
		rules=resolve_rules(rules)
	return rules

def main():
	data=open('example.txt','r')
	rules, messages=data.read().split("\n\n")
	rules=rules.split('\n')
	messages=messages.split('\n')
	for rulenumber in range(len(rules)):
		rules[rulenumber]=rules[rulenumber].split(": ")[1]
	raw_rule0="^"+resolve_rules(rules)[0].replace('"','')+"$"
	matches=0
	print(raw_rule0)
	for message in messages:
		if(re.findall(raw_rule0, message)!=[]):
			#print(message)
			matches=matches+1
	print(matches)

if __name__ == "__main__":
	main()