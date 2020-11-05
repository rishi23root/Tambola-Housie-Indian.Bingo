import random
from playAudios import play_sound as play
from time import sleep as nap
import keyboard
import threading
  
class tambola :
	def __init__(self,method,napTime):
		self.need_to_stop = False
		self.restart_thread = False
		self.method= method
		self.napTime= napTime
		if self.method == 'nap':
			self.th = threading.Thread(target=self.key_waiting,daemon = True)
			self.th.start()

	def key_waiting(self):
		# global self.need_to_stop,self.restart_thread
		keyboard.wait('Space')

		self.need_to_stop = True
		print('\t\tprogram is Paused')
		print('press \'SPACE bar\' to continue with Program\n')
		keyboard.wait('Space')
		self.need_to_stop = False
		self.restart_thread = True

	def start_playing_cmd(self):
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
			if self.method =='input':
				input("press enter to get num")
			else:
				# waiting for naptime 
				nap(self.napTime)				
				# continiously waitly for the space key to pause the program
				while self.need_to_stop :
					# waiting for the user to press the hot key
					nap(1)

				if self.restart_thread and i != 90:
					self.restart_thread = False
					self.th = threading.Thread(target=self.key_waiting,daemon = True)
					self.th.start()

			if num != [] :
				print(i)

				a = random.choice(num)			
				num.remove(a)
				# threading.Thread(target=play,args=(f'sounds/{a}.mp3',)).start()
				# print(a)
	 			# print('\033[93m' + str(a) + '\033[0m')
				print()
				print(a)
				print()
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
				print('line 0-1  ',l10)
				print('line 11-20',l20)
				print('line 21-30',l30)
				print('line 31-40',l40)
				print('line 41-50',l50)
				print('line 51-60',l60)
				print('line 61-70',l70)
				print('line 71-80',l80)
				print('line 81-90',l90)
				print()
				play(f'sounds/{a}.mp3')  #######################
				
				if i==90:
					# '''to sea all the all number ^__^'''
					nap(5)

			else :
				print('no num left')

			if self.method != 'input' and i == 90 and self.th.is_alive() :
				# this break cause complete of the first thread and that cause end of all demon thread
				break

	@classmethod
	def player(cls,method,napTime=1.5):
		pla = cls(method,napTime)
		pla.start_playing_cmd()


tambola.player(method='nap',napTime=0.1)
