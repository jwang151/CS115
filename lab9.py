'''
Created on Nov 2, 2017
Lab 9 
@author: jwang151@stevens.edu
pledge: I pledge my honor that  I have abided by the Stevens Honor System. 

# keep this import line...

# start your Lab 9 functions here:

'''
from cs5png import PNGImage

def mult(c, n):
    '''returns the product of c times n but without multiplication'''
    result = 0
    for x in range(n):
        result += c
    return result

def update(c, n):
    '''It starts a new value, z at zero, and then repeatedly updates the value of z using the assignment statement '''
    z = 0
    for x in range(n):
        z = z**2 + c
    return z
print(update(1,3))
def inMSet(c, n):
    '''that takes as input a complex number c and an integer n. '''
    z = 0 
    for x in range(n):
        z = z**2 + c
        if abs(z) > 2:
            return False
    return True
def weWantThisPixel( col, row ):
    '''  a function that returns True if we want, the pixel at col, row and False otherwise '''
    if col%10 == 0 and row%10 == 0:
        return True
    else:
        return False

def test():
    '''   a function to demonstrate how to create and save a png image  '''
    width = 300
    height = 200
    image = PNGImage(width, height)
     # create a loop in order to draw some pixels        
    for col in range(width):        
        for row in range(height):             
            if weWantThisPixel( col, row ) == True:                 
                image.plotPoint(col, row) 
     # we looped through every image pixel; we now write the file 
    image.saveFile() 

def scale(pix, pixMax, floatMin, floatMax):
    return (pix/pixMax) * (floatMax - floatMin) + floatMin
print(scale(100, 200, -1.5, 1.5))
         
def mset():     
    """ creates a 300x200 image of the Mandelbrot set     """    
    width = 300     
    height = 200     
    image = PNGImage(width, height) 
     # create a loop in order to draw some pixels          
    for col in range(width):         
        for row in range(height):  
            x = scale(col, width,-2,1)  
            y = scale(row, height,-2,1)        
            if inMSet(x+y*1j, 25) == True:               
                image.plotPoint(col, row) 
     # we looped through every image pixel; we now write the file 
    image.saveFile()
mset( )







