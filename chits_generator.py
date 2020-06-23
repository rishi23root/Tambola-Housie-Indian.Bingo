import random

def random15Numbers():
	# create dic and numbers from 1 to 90
	num={}
	num['num10'] =[i for i in range(1,11)]
	num['num20'] =[i for i in range(11,21)]
	num['num30'] =[i for i in range(21,31)]
	num['num40'] =[i for i in range(31,41)]
	num['num50'] =[i for i in range(41,51)]
	num['num60'] =[i for i in range(51,61)]
	num['num70'] =[i for i in range(61,71)]
	num['num80'] =[i for i in range(71,81)]
	num['num90'] =[i for i in range(81,91)]

	# count variable to don't execede from more then 3 num in coloum and 15 in total  
	count={}
	count['num10'] = 0
	count['num20'] = 0
	count['num30'] = 0
	count['num40'] = 0
	count['num50'] = 0
	count['num60'] = 0
	count['num70'] = 0
	count['num80'] = 0
	count['num90'] = 0

	# all selected num save in selected
	selected=[]

	# step1
	# chose first 9 nums
	for j in range(1,10):
		ch=	random.choice(num[f'num{j}0']) 
		selected.append(ch)
		count[f'num{j}0'] += 1
		num[f'num{j}0'].remove(ch)


	# step2
	# next 6 remaining nums
	whole_list = [i for i in range(1,91)]
	# remove pre selected 9 for proceed
	for i in selected:
		whole_list.remove(i)

	# print(whole_list)
	while len(selected) < 15:
		numlist = ['num10','num20','num30','num40','num50','num60','num70','num80','num90' ]

		n = random.choice(whole_list)
		# print(n)

		for i in numlist:
			if (n in num[i]) and (n in whole_list):
				count[i] += 1
				selected.append(n)
			else:
				pass 
		

		for i in numlist:
			if count[i] == 3:
				for k in num[i]:
					if k in whole_list:
						whole_list.remove(k)
			else:
				pass

	selected.sort()

	sum=0
	for i in count:
		sum += count[i]

	if sum != 15:
		# print(selected)
		# print(count)
		chit()
	else:
		pass
		# print(selected)



	# count ,selected=chit()
	value={}
	value['num10']=[]
	value['num20']=[]
	value['num30']=[]
	value['num40']=[]
	value['num50']=[]
	value['num60']=[]
	value['num70']=[]
	value['num80']=[]
	value['num90']=[]

	for i in count:
		for j in range(count[i]):
			value[i].append(selected[0])
			selected.remove(selected[0])
		
	# print(value)

	return numlist,value

	


# for i in range(1):

def arrangementsOfNums():

	numlist,value =	random15Numbers()

	# print(numlist)
	# print(value)

	final1=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
	final2=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
	final3=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
	count1 = 0
	count2 = 0
	numlist1 = []
	numlist2 = []

	# FOR FIRST ROW
	# first check if any number list len == 3 
	# if true count+1 and add it to final1 of its index 
	# and remove it from value
	# chose randomly from the numlist and append them in their possitions then 
	# if count > 5 break

	# similar for final2 and final3 just len == 2 and all remainings respectively
	# then save data in file with random ticket number 

	# loop for row 1
	while count1 < 5:
		for i in numlist:
			if len(value[i]) == 3:
				numlist1.append(i)
				a = value[i][0]
				value[i].remove(a)
				index = numlist.index(i)
				final1[index] = a
				count1+=1

		foo = random.choice(numlist)
		if foo not in numlist1:
			# save that its done
			numlist1.append(foo)
			a = value[foo][0]
			value[foo].remove(a)
			index = numlist.index(foo)
			final1[index] = a
			count1+=1

	# loop for row 2
	while count2 < 5:
		for i in numlist:
			if len(value[i]) == 2:
				numlist2.append(i)
				a = value[i][0]
				value[i].remove(a)
				index = numlist.index(i)
				final2[index] = a
				count2+=1

		foo = random.choice(numlist)
		if foo not in numlist2:
			numlist2.append(foo)
			if len(value[foo]) != 0:
				# save that its done
				a = value[foo][0]
				value[foo].remove(a)
				index = numlist.index(foo)
				final2[index] = a
				count2 += 1

	# for third and final row there is two methods

	# for i in numlist:
	# 	index = numlist.index(i)
	# 	if len(value[i]) != 0:
	# 		final3[index] = value[i][0]

	for index,number in enumerate(numlist):
		if len(value[number]) != 0:
			final3[index] = value[number][0]


	# convert into 2 digit numbers
	for i,n in enumerate(final1):
		if type(final1[i]) == int:
			final1[i] = str(n).zfill(2)

	for i,n in enumerate(final2):
		if type(final2[i]) == int:
			final2[i] = str(n).zfill(2)
		
	for i,n in enumerate(final3):
		if type(final3[i]) == int:
			final3[i] = str(n).zfill(2)
				
	return [final1,final2,final3]


def save_chits_in_file(how_many_chits=1,number_to_start=0):
	for i,nu in enumerate([x for x in range(how_many_chits)],number_to_start):
		head = f'  	 lottery ticket by Rishi - {i + 1}'
		line1,line2,line3 = arrangementsOfNums()
		with open("Tambola tickets.txt",'a') as file:
			file.writelines(str(head)+'\n')
			file.writelines(str(line1)+'\n')
			file.writelines(str(line2)+'\n')
			file.writelines(str(line3)+'\n')
			file.writelines('\n')

re=int(input('Enter the number of chits require :'))
save_chits_in_file(how_many_chits=re)