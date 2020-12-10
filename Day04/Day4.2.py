import re

data=open('data.txt','r')
#cid is unnecessary
fieldnames=["ecl","pid","eyr","hcl","byr","iyr","hgt"]
total_valid=0

passports=data.read().split('\n\n')


for passport in passports:
    #check if all necessary fields present
    all_fields_present=1
    for i in fieldnames:
        if i not in passport:
            all_fields_present=0
    valid=all_fields_present

    #ckeck if every field is valid
    fields=passport.split()
    for field in fields:

        [key,value]=field.split(":")

        """
        Check if all fields are valid:

        -byr (Birth Year) - four digits; at least 1920 and at most 2002.
        -iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        -eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        -hgt (Height) - a number followed by either cm or in:
            -If cm, the number must be at least 150 and at most 193.
            -If in, the number must be at least 59 and at most 76.
        -hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        -ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        -pid (Passport ID) - a nine-digit number, including leading zeroes.
        -cid (Country ID) - ignored, missing or not.
        """

        if key=="byr":
            if(int(value)<1920 or int(value)>2002):
                valid=0

        if key=="iyr":
            if(int(value)<2010 or int(value)>2020):
                valid=0

        if key=="eyr":
            if(int(value)<2020 or int(value)>2030):
                valid=0

        if key=="hgt":
            if(value[-2:]=="cm"):
                if(int(value[:-2])<150 or int(value[:-2])>193):
                    valid=0
            elif value[-2:]=="in":
                if(int(value[:-2])<59 or int(value[:-2])>76):
                    valid=0
            else:
                valid=0

        if key=="hcl":
            if(re.findall(r'#[0-9a-f]{6}',value)==[]):
                valid=0

        if key=="ecl":
            if(re.findall(r'^(amb|blu|brn|gry|grn|hzl|oth)$',value)==[]):
                valid=0

        if key=="pid":
            if(re.findall(r'^[0-9]{9}$',value)==[]):
                valid=0

    total_valid=total_valid+valid

print(total_valid)
