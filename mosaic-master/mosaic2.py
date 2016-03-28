from PIL import Image
from collections import Counter 
im = Image.open("/home/michael/Documents/spring16/cst205/project2/spongeBob.jpg")

#CREATED LISTS TO KEEP TRACK OF THE VALUES OF EACH PIXEL
redPixelList = []
greenPixelList = []
bluePixelList = []

#finds the width and height of the image.
width, height = im.size
#print width
#print height

tileHeight = height /3
tileWidth = width

beginWidth = 0
beginHeight = 0


#CREATES A NEW EMPTY CANVAS IMAGE
finalImg = Image.new("RGB",(width,height),"Black")


"""
-------------------------------------------------------------------
BEGINNING TO FINDING THE COLORS OF OUR TILES 
-------------------------------------------------------------------
"""

for times in range(0,3):
	for xPos in range(beginWidth,tileWidth):
		for yPos in range(beginHeight,tileHeight):
		
			rgb_im = im.convert('RGB')
			r,g,b, = rgb_im.getpixel((xPos,yPos))

	    	redPixelList.append(r)
	    	greenPixelList.append(g)
	    	bluePixelList.append(b)
	
		mostRed = Counter(redPixelList)
		mostGreen = Counter(greenPixelList)
		mostBlue = Counter(bluePixelList)

		myRed = max(mostRed.values())
		modeRed = [k for k, v in mostRed.items() if v == myRed]
		myGreen = max(mostGreen.values())
		modeGreen = [k for k, v in mostGreen.items() if v == myGreen]
		myBlue = max(mostBlue.values())
		modeBlue = [k for k, v in mostBlue.items() if v == myBlue]



	#PRINTS THE MODES OF EVERY COLOR IN TILE PARTS 
	#print modeRed[0]
	#print modeGreen[0]
	#print modeBlue[0]
   
	del redPixelList[:]
	del greenPixelList[:]
	del bluePixelList[:]

	for imgX in range(beginWidth,tileWidth):
		for imgY in range(beginHeight,tileHeight):
			finalImg.putpixel((imgX,imgY),(modeRed[0],modeGreen[0],modeBlue[0]))

	if(times < 1):
		beginHeight += tileHeight
		beginWidth = 0
		tileHeight += tileHeight
	else :
		tileHeight += beginHeight
		beginHeight += beginHeight
		beginWidth = 0

	#GRABING THE MODE OF EVERY COLOR IN THE LIST	
	if(times == 0):
		firstRedMode = modeRed[0]
		firstGreenMode = modeGreen[0]
		firstBlueMode = modeBlue[0]
	elif(times == 1):
		secondRedMode = modeRed[0]
		secondGreenMode = modeGreen[0]
		secondBlueMode = modeBlue[0]
	else: 
		thirdRedMode = modeRed[0]
		thirdGreenMode = modeGreen[0]
		thirdBlueMode = modeBlue[0]

#finalImg.show() 

"""
-----------------------------------------------------------------------
END TO FINDING THE COLORS
-----------------------------------------------------------------------
"""

"""
-----------------------------------------------------------------------
CODE BELOW IS FOR TESTING PURPOSE, TRYING TO FIND A SOLUTION TO THE BLENDING OF BOTH IMAGES
-----------------------------------------------------------------------
"""

bw_im = im.convert("1")
new_im = bw_im.convert("RGB")
pixels = new_im.getdata()

finalPixels = []
for bwX in range(0,height):
	for bwY in range(0,width):
		r,g,b = new_im.getpixel((bwY,bwX))
		print r,g,b
		#print list(im.getdata())
		
		if (r == 255 and bwX < (height / 3) ):
			print "First", bwX , bwY
			finalPixels.append((66,255,255,0))
		elif(r == 255 and (bwX > height/3) and (bwX < (height/3) *2)):
			print "second", bwX, bwY
			finalPixels.append((255,48,17,0))
		elif(r == 255 and bwX <= height):
			print "third" , bwX, bwY
			finalPixels.append((84,50,35,0))
		else:
			print "Black"
			finalPixels.append((0,0,0,0))

"""
----------------------------------------------------------------------
END OF TESTING CODE.
----------------------------------------------------------------------
"""

"""
FIXED THE INFINITE LOOP IT HAD.

------------------------------------------------------------------------

WORKS ALREADY, HOWEVER MUST FIND A WAY TO PLACE THE THE COLOR IMAGE INTO THE BLACK AND WHITE IMAGE

bw_im = im.convert("1")
new_im = bw_im.convert("RGB")
pixels = new_im.getdata()

for bwX in range(0,height):
	for bwY in range(0,width):
		r,g,b = new_im.getpixel((bwY,bwX))
		print r,g,b
		#print list(im.getdata())
		
		if (r == 255 and bwX < (height / 3) ):
			print "First", bwX , bwY
			finalPixels.append((66,255,255,0))
		elif(r == 255 and (bwX > height/3) and (bwX < (height/3) *2)):
			print "second", bwX, bwY
			finalPixels.append((255,48,17,0))
		elif(r == 255 and bwX <= height):
			print "third" , bwX, bwY
			finalPixels.append((84,50,35,0))
		else:
			print "Black"
			finalPixels.append(0,0,0,0)
----------------------------------------------------------------------

"""
finalImg.putdata(finalPixels)
finalImg.show()			
print("Image Displayed.")
