import os
'''completeing all of the requirements with os scripts needs internet connection'''
with open('requirements.txt') as requirements:
	require = requirements.readlines()
	for i in require :
		print()
		i=i.replace('\n','') 
		if ('pip' in i) or ('python' in i):
			if ('python' in i):
				print()
				print('This will take some time about 2 to 2.5 min')

			print(i)
			os.system(i)
