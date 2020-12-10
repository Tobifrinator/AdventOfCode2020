import numpy as np


def count(contains, row):
    """

    Args:
        contains: array of our bags in a bag
        row: row of bag we examine
        nesting: for visualization purposes

    Returns:
        [type]: [description]
    """
    counter=1
    #print(contains[row])
    for i in range(len_bags):
        if (contains[row,i])!=0:
            occurence=contains[row,i]
            subcount=count(contains, i)
            counter=counter+occurence*subcount
    return counter

data=open('data.txt','r')
bags=data.read().split("\n")
bagNum={}
NumBag=[]
len_bags=len(bags)
contains=np.zeros((len_bags, len_bags))
"""
Create dictionary for the bags, we want the color: -> Before contain, last 5 characters are always _bags -> remove them too
Example:
pale turquoise bags contain 3 bright cyan bags, 3 posh blue bags, 3 dark olive bags -> pale turquoise
Every bag gets its own Number
"""

for i,bag in enumerate(bags):
    bag=bag.split(" contain ")
    if("shiny gold" in bag[0]):
        row_of_shiny_gold=i
    bagNum[bag[0][:-5]]=i

"""
Initialize the matrix of number of bags contained in a bag
"""
for bag in bags:
    bag=bag.split(" contain ")
    containees=bag[1].replace(".","").split(", ")
    for containee in containees:
        bag_number=containee.split()[0]
        for key in bagNum:
            if key in containee:
                contains[bagNum[bag[0][:-5]]][bagNum[key]]=bag_number

"""
Aufruf von Count, count zählt aber eigenen Bag mit, also -1
"""
print("One Shiny gold bag contains",str(int(count(contains,[bagNum["shiny gold"]],)[0])-1),"other bags")


