import numpy as np
import cv2

image = cv2.imread("a.jpeg")
ImageSize = image.shape

height = ImageSize[0]
width = ImageSize[1]

print(height)
print(width)

f= open("generator.html","w+")

f.write("<!DOCTYPE html>\n")
f.write("<html>\n")
f.write("<title>CSS generator by python</title>\n")
f.write("</head>\n")

count=0
f.write("<div style=\"width: 100%; display: table;\">")
f.write("<div style=\"display: table-row; height: 1px;\">")

for x in range (0,height):
    for y in range (0,width):
    	count=count+1
    	pixel = image[x,y]
    	f.write("<div style=\"display:table-cell;background-color:rgba("+str(pixel[0])+","+str(pixel[1])+","+str(pixel[2])+");\"></div>\n")
    	if count%width==0:
    		f.write("</div>")
    		f.write("</div>")
    		f.write("<div style=\"width: 100%; display: table;\">")
    		f.write("<div style=\"display: table-row; height: 1px;\">")

f.write("</body>\n")
f.write("</html>\n")

