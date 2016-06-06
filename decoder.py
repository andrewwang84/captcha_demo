from PIL import Image
import os
import time

i=1
for num in range(1,6):
	tmp=str(i)
	path = '/home/yrwang/Downloads/downloaded-captcha/'+tmp+'.JPEG'
	img = Image.open(path)
	img = img.convert("RGBA")
	
	pixdata = img.load()
	
	for y in xrange(img.size[1]):
		for x in xrange(img.size[0]):
			if pixdata[x, y][0] < 90:
				pixdata[x, y] = (0, 0, 0, 255)
	for y in xrange(img.size[1]):
		for x in xrange(img.size[0]):
			if pixdata[x, y][1] < 136:                 
				pixdata[x, y] = (0, 0, 0, 255)
	for y in xrange(img.size[1]):
		for x in xrange(img.size[0]):             
			if pixdata[x, y][2] > 0:
				pixdata[x, y] = (255, 255, 255, 255)  
						  
	img.save("/home/yrwang/Downloads/cleaned_captcha/"+tmp +".gif", "GIF")

	#   Make the image bigger (needed for OCR)

	im_orig = Image.open("/home/yrwang/Downloads/cleaned_captcha/"+tmp +".gif")
	big = im_orig.resize((250*1, 62*1), Image.NEAREST)
	ext = ".tif"
	big.save("/home/yrwang/Downloads/cleaned_captcha/"+tmp + ext)
	
	command = "tesseract -psm 7 /home/yrwang/Downloads/cleaned_captcha/"+tmp + ".tif "+"/home/yrwang/Downloads/text"
	os.system(command)
	time.sleep(1)

	Text  = open ("/home/yrwang/Downloads/text.txt","r")
	decoded = Text.readline().strip('\n')
	if decoded.isdigit():
		print ('[+}CAPTCHA number are ' + decoded)
	else:
		print ('[-] Error : Not able to decode')
	i+=1
