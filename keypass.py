#Key pass , a simple python script  for generating passlist based on keywords of a profile , the difference with cupp is that , you just enter keywords and anything U know
#You don't have to enter unknown info like age , GF's name or ... . Feel free and enter known info to generate passlist
#N3T-RE4P3R
print (" Key-PASS")
print ("Welcome dear user ! pleas read the README.TXT file first")

def passwordgenerator() :
	list1 = list()
	#list2 = list() 
	name = input(" Enter target's name or username: ")
	while True :
		keywords1 = input("Enter any keyword or info related to target (enter 'done' to finish): ")
		if keywords1 == "done" :
			print ("you have made one keyword list")
			break
		else :
			list1.append(keywords1)
			print (list1)
	filename = name + ".txt"
	file = open(filename,'w')
	for word in list1 :
		#pass Style1
		pss = name + word + "\n"
		file.write(pss)
		print (" writing passwords ..." , pss)
		#pass style2
		pss2 = word + name + "\n"
		file.write(pss2)
		print ("writing passwords ..." , pss2)

	for word in list1 :
		#pass Style1
		pss = name + "-" + word + "\n"
		file.write(pss)
		print (" writing passwords ..." , pss)
		#pass style2
		pss2 = word + "-" + name + "\n"
		file.write(pss2)
		print ("writing passwords ..." , pss2)

	for word in list1 :
		#pass Style1
		pss = name + "_" + word + "\n"
		file.write(pss)
		print (" writing passwords ..." , pss)
		#pass style2
		pss2 = word + "_" + name + "\n"
		file.write(pss2)
		print ("writing passwords ..." , pss2)

	for word in list1 :
		#pass Style1
		pss = name + " " + word + "\n"
		file.write(pss)
		print (" writing passwords ..." , pss)
		#pass style2
		pss2 = word + " " + name + "\n"
		file.write(pss2)
		print ("writing passwords ..." , pss2)
	print ("all possible passwords with given words have been generated!")
	file.close()
	
passwordgenerator()