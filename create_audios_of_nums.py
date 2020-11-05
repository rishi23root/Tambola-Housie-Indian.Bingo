from gtts import gTTS
import os
import time

'''AIM : This SCRIPT will form all the audio files for the game and 
needed to execute only once'''

# change dir to sounds to save all data there
try:
	# check if directory is already there if not then execute 
	os.mkdir("sounds")
	os.chdir(os.getcwd()+'/'+'sounds')
except:
	os.chdir(os.getcwd()+'/'+'sounds')


def convert_text_to_audio(text,name):
	# converting here from text given and save as name given
	print(f"creating a new audio file {name} with text {text}")
	try:
		sound=gTTS(text)
		sound.save(f'{name}.mp3')
	except :
		time.sleep(1)
		print('sleep for 1 sec')
		sound=gTTS(text)
		sound.save(f'{name}.mp3')
	

# to make files of all numbers 1 to 90 as pre requirement
for i in range(0,91):
	convert_text_to_audio(f"  {i}  ",f'{i}')

convert_text_to_audio(' only ','only')

quit()