#snippet for creating the rule11:
#11: ( 42 31 )| ( 42 31 )| ( 42 42 31 31 )| ( 42 42 42 31 31 31 )| ( 42 42 42 42 31 31 31 31 )| ( 42 42 42 42 42 31 31 31 31 31 )| ( 42 42 42 42 42 42 31 31 31 31 31 31 )| ( 42 42 42 42 42 42 42 31 31 31 31 31 31 31 )| ( 42 42 42 42 42 42 42 42 31 31 31 31 31 31 31 31 )| ( 42 42 42 42 42 42 42 42 42 31 31 31 31 31 31 31 31 31 )
rule11="( 42 31 )"
for i in range(1,10):
    rule11=rule11+"| ( "+"42 "*i +  "31 "*i +")"
print(rule11)