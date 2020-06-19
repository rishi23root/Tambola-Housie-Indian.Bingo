import random
from playAudios import play_sound as play
from time import sleep as nap
import threading 

def start_playing(method='nap',napTime=2.5):
	num=[i for i in range(1,91)]
	done=[]
	l10=[]
	l20=[]
	l30=[]
	l40=[]
	l50=[]
	l60=[]
	l70=[]
	l80=[]
	l90=[]

	for i in range(1,91):
		if method =='input':
			input("press enter to get num")
		else:
			nap(napTime)
		if num != [] :
			a = random.choice(num)			
			num.remove(a)
			# threading.Thread(target=play,args=(f'sounds/{a}.mp3',)).start()
			# print(a)
			print('\033[93m' + str(a) + '\033[0m')
			done.insert(0, a)
			done.sort()
			
			if a<=10 :
					l10.append(a)
					l10.sort()

			elif a<=20 :
					l20.append(a)
					l20.sort()

			elif a<=30 :
					l30.append(a)
					l30.sort()

			elif a<=40 :
					l40.append(a)
					l40.sort()

			elif a<=50 :
					l50.append(a)
					l50.sort()

			elif a<=60 :
					l60.append(a)
					l60.sort()

			elif a<=70 :
					l70.append(a)
					l70.sort()

			elif a<=80 :
					l80.append(a)
					l80.sort()

			elif a<=90 :
					l90.append(a)
					l90.sort()
	    		
			# print(done)
			print('line 0-1',l10)
			print('line 11-20',l20)
			print('line 21-30',l30)
			print('line 31-40',l40)
			print('line 41-50',l50)
			print('line 51-60',l60)
			print('line 61-70',l70)
			print('line 71-80',l80)
			print('line 81-90',l90)
			print()
			play(f'sounds/{a}.mp3')

		else :
			print('no num left')
		

start_playing(method='input')
# you have to press enter every single time to get new number
start_playing(method='input')
# you have to wait=(napTime) every single time to get new number

# for automate with time disadvantage is unable to pause with time inform me if you can help thanks
