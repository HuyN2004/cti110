red = int(input())
green = int(input())
blue = int(input())
gray = 50

if (red < green) and (red <blue): 
    gray = red
    
elif (green < blue): 
    gray = green
    
else: 
    gray = blue
    
red = red - gray
green = green - gray
blue = blue - gray

print (red, green, blue)
    