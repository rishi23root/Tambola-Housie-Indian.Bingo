import random
from playAudios import play_sound as play
from time import sleep as nap
# import time
import keyboard
import threading

from tkinter import *
import datetime
from time import sleep as nap
from threading import Thread
import argparse



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

	def start_playing_gui(self):
		num=[i for i in range(1,91)]
		for i in range(1,91):		
			# continiously waitly for the space key to pause the program
			while self.need_to_stop :
				# waiting for the user to press the hot key
				nap(0.1)

			if self.restart_thread and i != 90:
				self.restart_thread = False
				self.th = threading.Thread(target= lambda: self.key_waiting(),daemon = True)
				self.th.start()

			a = random.choice(num)			
			num.remove(a)
			yield a
			
			if i == 90 and self.th.is_alive() :
				# this break cause complete of the first thread and that cause end of all demon thread
				break

	@classmethod
	def player(cls,method,napTime=2.5):
		pla = cls(method,napTime)
		pla.start_playing_cmd()
		

class tambola_gui(tambola) :
	def __init__(self,root):
		super().__init__(method='nap',napTime=1.5)
		# hwight of the windows
		self.height = 825
		self.width = 1000

		# colours
		self.head_bar_colour = '#34495e'	
		self.head_bar_heigth = 100

		# creating window
		self.root = root
		self.root.title('TAMBOLA')
		self.root.geometry(f"{self.width}x{self.height}")
		
		self.last_tile = None

		# start creating the elements
		# creaing heading
		self.head()
		# starting the clock 
		Thread(target =lambda : self.clock() ,daemon=True).start()
		# creating the tile canvas and tiles
		self.create_tiles(self.root)

	def head(self):
		# head with status and time box
		self.head_bar = Label(self.root,bg=self.head_bar_colour)
		self.head_bar.place(height = self.head_bar_heigth, width = self.width)

		# status - running / pause
		status_label = Label(self.head_bar,fg='white',bg=self.head_bar_colour,padx=5,font=('arial',40,'bold'),text= 'Status :')
		status_label.pack(side=LEFT)

		self.status_value = Label(self.head_bar,font=('arial',30,'bold'),padx=5,text= 'RUNNING')
		self.status_value.pack(side=LEFT)

		# clock - time update every second 
		self.time_value = Label(self.head_bar,font=('arial',40,'bold'),padx=10,bg=self.head_bar_colour,fg='white',text=datetime.datetime.now().strftime('%I:%M:%S %p'))
		self.time_value.pack(side=RIGHT)

	def clock(self):
		# update every second 
		while True:
			# update the value here till the window exits it will run
			try :
				# time_value.set(datetime.datetime.now().strftime('%I:%M:%S %p'))
				self.time_value['text'] = datetime.datetime.now().strftime('%I:%M:%S %p')
				nap(1)

			except :
				# no exception to show 
				print('clock Ends')
				quit()
				break

	def create_tiles(self,master):
		canvas = Label(master,bg='#95a5a6')
		canvas.place(y= self. head_bar_heigth+5, width = self.width, height=self.height)

		# creating canvas to place the tiles
		tile_canvas_w = self.width-50
		tile_canvas_h = self.height - self.head_bar_heigth
		tile_canvas = Label(canvas,bg='#ecf0f1')
		tile_canvas.place(x=20,width=tile_canvas_w,height=tile_canvas_h)

		# creating grid
		for row in range(9):
			for col in range(10):
				tile_num = str(int(''.join([str(row),str(col)])) + 1).zfill(2)
				Label(master=tile_canvas,name=str(tile_num),font=('arial',31,'bold'),text = tile_num,borderwidth=5, highlightthickness=5, relief="solid",anchor= CENTER).grid(row=row,column=col,padx=13,pady=5)
				# print(row,col,tile_num)

		self.tile_list = tile_canvas.winfo_children()

	def update_tiles(self,num):
		num = str(num).zfill(2)
		# last tile info

		for i in self.tile_list:
			if i['text'] == num :
				# normalised the colour
				if self.last_tile != None :
					self.last_tile['bg'] = '#f1c40f'
					self.last_tile['fg'] = 'white'

				# update background and font colour for last element 
				i['bg'] = '#3de7c5'
				i['fg'] = 'white'
				self.last_tile = i
				break
		else :
			raise Exception('Unable to find the tile')

	def number_gen(self,clas):
		# wait for 2sec before painting 
		nap(2) 
		for i in clas.start_playing_gui():
			clas.update_tiles(i)
			play(f'sounds/{i}.mp3')    #################un comment it
			# print(self.napTime)
			nap(self.napTime)

	@classmethod
	def tam(cls):
		root = Tk()
		clas = cls(root)		
		Thread(target=clas.number_gen,args=[clas],daemon=True).start()
		# execution
		root.mainloop()


# example
# gui => 'python tambola.py'
# commend line nap version=> 'python tambola.py -c'
# commend line input version=> 'python tambola.py -c -i'

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-g','--gui' ,action="store_true",help = "gui version of the program !")
	parser.add_argument('-c',action="store_true",help = "commend line version of the program !")
	parser.add_argument('-n','--nap',action="store_true",help = "nap boolean - automatically give next number with in nap time!")
	parser.add_argument('-i','--input',action="store_true",help = "input boolean wait for user to enter for every next number!")
	parser.add_argument('-t','--time',default = 1.2,type=float,help = "wait time in program!")

	args = parser.parse_args()

	if args.c and not args.gui:
		# run when commend line is called
		print('commend line version',end=' -> ')
		# here is 2 ways input/nap nap is default run
		if args.input:
			print('input method\n\n')
			tambola.player(method='input',napTime=args.time)

		else:
			print('nap method\n\n')
			tambola.player(method='nap',napTime=args.time)

	else:
		# gui version is default
		print('Gui version called ')
		tambola_gui.tam()
