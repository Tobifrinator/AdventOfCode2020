import re

data=open('data.txt','r')
#cid is unnecessary
fieldnames=["ecl","pid","eyr","hcl","byr","iyr","hgt"]

passports=data.read().split('\n\n')
total_valid=0
for passport in passports:
    #check if all necessary fields present
    all_fields_present=1
    for i in fieldnames:
        if i not in passport:
            all_fields_present=0
    valid=all_fields_present

    total_valid=total_valid+valid

print(total_valid)
