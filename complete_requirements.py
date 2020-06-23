import os
'''completeing all of the requirements with os scripts needs internet connection'''
with open('requirements.txt') as requirements:
	require = requirements.readlines()
	for i in require :
		i=i.replace('\n','') 
		if ('pip' in i) or ('python' in i):
			if ('create_audios_of_nums' in i):
				
				print('This will take some time about 2 to 2.5 min \ngenerating sound for game')

			print(i)
			print()
			os.system(i)

		print()
		print()
