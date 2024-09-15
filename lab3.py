#Gather inputs
print ('Enter your income:')
income = float(input())

print ('Enter your marital status. True or False:')
marital_status = input()

#Do the if-thens
if marital_status == "False" and income <= 11000 :
	print ('Your Tax Rate is 10%')
	
elif marital_status == "True" and income <= 22000 :
	print ('Your Tax Rate is 10%')
	
elif marital_status == "False" and income >= 11001 and income <= 44725 :
	print ('Your Tax Rate is 12%')
	
elif marital_status == "True" and income >= 22001 and income <= 89451 :
	print ('Your Tax Rate is 12%')
	
elif marital_status == "False" and income >= 44726 and income <= 95375 :
	print ('Your Tax Rate is 22%')
	
elif marital_status == "True" and income >= 89451 and income <= 190750 :
	print ('Your Tax Rate is 22%')
	
elif marital_status == "False" and income > 95375 :
	print ('Please insert a lower income') #Please be less rich
	
elif marital_status == "True" and income > 190750 :
	print ('Please insert a lower income')
