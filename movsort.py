import os
import json
import shutil
import sys
import time
import requests


def set_proxy():

	proxy_file = open("proxy.config","r")
	
	r = proxy_file.read()
	
	if 'http' in  r:
	
		http_proxy = r
		
		https_proxy = http_proxy.replace("http","https")
		
	elif 'https' in  r:
	
		https_proxy = r
		
		http_proxy = http_proxy.replace("https","http") 
	
	os.environ['http_proxy'] = http_proxy
	
	os.environ['https_proxy'] = https_proxy
	
	proxy_file.close()
	
def find_str(s, char):

    index = 0

    if char in s:
	
        c = char[0]
		
        for ch in s:
		
            if ch == c:
			
                if s[index:index+len(char)] == char:
				
                    return index

            index += 1

    return -1

def clear_names(x):
	
	ind=0
		
	x = x.lower()
		
	for y in range(1500,2100):
		
		if(str(y) in x):
			
			x=x.replace(str(y)," ")
				
	for z in values:
		
		if(str(z) in x):
			
			if((find_str(x, z) < ind and ind !=0) or ind ==0):
				
				ind = find_str(x, z)
		if("  " in x):
			
			x=x.replace("  "," ")
			
	if ind is not 0:
		
		x=x[:ind]
			
	x=x.replace("."," ")
		
	x=x.replace("-"," ")
		
	x=x.replace("_"," ")
		
	return x
	
def orderByRating(folder):
	
	delete = raw_input("\nDO YOU WANT TO DELETE MOVIES WITH RATINGS LESS THAN SPECIFIED VALUE (Y/N) ? \n>> ")
	
	if delete == 'y' or delete == 'Y':
		
		ratingCheck = raw_input("\nENTER THE RATING VALUE\n")
	
	print("\nSORTING YOUR MOVIES BASED ON RATINGS \n")
	
	for x in os.listdir(folder):
		
		moviename=os.path.join(folder, x)

		if(x[0].isdigit()and x[1]=='.'):
		
			continue
		
		x = clear_names(x)
		
		if x == "main" :
		
			continue
		
		url='http://www.omdbapi.com/?t='+str(x)
		
		response  = requests.get(url)
		
		
		jsonvalues = json.loads(response.text)
		
		if jsonvalues["Response"] == "True":
			
			imdbrating = jsonvalues['imdbRating']
			
			if delete == 'n' or imdbrating >ratingCheck or delete == 'N' :
			
				genres = jsonvalues['Genre'].split(',')
				
				if not os.path.exists(imdbrating):
			
					os.makedirs(imdbrating)
				
				destinationDir = os.path.join(folder, imdbrating)
				
				print(imdbrating+"(IMDB)\t"+x)
				
				shutil.move(moviename, destinationDir)
				
				time.sleep(1)
			
			else:
				
				print(imdbrating+"(IMDB)\t"+x+"\n")
				
				print("\n !! MOVIE RATING LOWER THAN SPECIFIED VALUE !!\n")
				
				time.sleep(1)
				
				confirm = raw_input("\nCONFIRM DELETION(y,n) ? ")
				
				if confirm == 'y' or confirm == 'Y':
				
					if  os.remove(moviename):
						
						print ("\nDELETION OF "+x+"FAILED\n")
						
					else:
						
						print ("\nSUCCESSFULLY DLETED "+x+"\n")
				else:
					
					print("\nDELETION ABORTED\n")
					
					if not os.path.exists(imdbrating):
			
						os.makedirs(imdbrating)
					
					destinationDir = os.path.join(folder, imdbrating)
				
					shutil.move(moviename, destinationDir)
					
					time.sleep(1)
					
					continue
		
		
if __name__ == "__main__":

	values=['[',']','(',')','m720p','480p','480','DVDSCR','BrRip','New Source','MP3','Mafiaking','1CD',
	'mkv','mSD','2CD','BRRip','BRrip','720p','BluRay','YIFY','mp4','XviD','x264','ETRG','avi','StyLishSaLH'
	,'DVD','dvd','DVDRip','RIP','rip','Rip','Back In Action','@','hindi','full','720p','1080p','web','bollywood','dvdrip','uncut',
	'unrated','hdrip','hq','brrip','bluray','dual','audio','dvdscr','camrip','hdts','hd-ts','bdrip','extended','tsrip']
	
	set_proxy()
	
	print ('\n##############################################################################\n')
	
	print ('\nMOVSORT VER 1.0 \n')
	
	time.sleep(2)
	
	orderByRating( os.getcwd())
	
	time.sleep(1)
	
	print ("\nMOVIES HAVE BEEN ARRANGED ENJOY !! \n")
	
	print ('\n##############################################################################\n')
	
	
