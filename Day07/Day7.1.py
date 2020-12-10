import numpy as np

data=open('data.txt','r')
bags=data.read().split("\n")
bagNum={}
len_bags=len(bags)
contains=np.zeros((len_bags, len_bags))
"""
Create dictionary for the bags, we want the color: -> Before contain, last 5 characters are always _bags -> remove them too
Example:
pale turquoise bags contain 3 bright cyan bags, 3 posh blue bags, 3 dark olive bags -> pale turquoise
Every bagtype gets its own Number
"""

for i,bag in enumerate(bags):
    bag=bag.split(" contain ")
    if("shiny gold" in bag[0]):
        row_of_shiny_gold=i
    bagNum[bag[0][:-5]]=i

"""
initialize an reachability matrix by creating an adjacency matrix
the dictionary gives the indices of the colors
"""
for bag in bags:
    bag=bag.split(" contain ")
    containees=bag[1].replace(".","").split(", ")
    for containee in containees:
        for key in bagNum:
            if key in containee:
                contains[bagNum[bag[0][:-5]]][bagNum[key]]=1

"""
Create the reachability matrix: Iterate over every row, add reachability to of current row to rows that can reach current row:
pseudo:

before blue         after blue
blue: red green     blue:red green
red: green          red: green
green: blue         green: blue red green
yellow: green       yellow: green

continue for every row
"""
for key in bagNum:
    for i in (contains):
        if(i[bagNum[key]]==1):
            for j in range(0,len_bags):
                i[j]=contains[bagNum[key]][j] or i[j]

print("Shiny gold bags are contained in",str(contains.sum(axis=0)[row_of_shiny_gold]),"other bags")
