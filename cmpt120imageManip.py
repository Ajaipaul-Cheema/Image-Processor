# CMPT 120 Yet Another Image Processer
# Starter code for cmpt120imageManip.py
# Author(s): Mohammad Haris Ahmad, Ajaipaul Cheema
# Date: December 7, 2020.
# Description: This file contains all the manipulations that appear on the interface.

# import module
import cmpt120imageProj


# get the image of the project and its width and height
image = cmpt120imageProj.getImage("project-photo.jpg")
width = len(image)
height = len(image[0])


def invert(pixels):
  '''
  Input: pixels - 2d array of RGB values
  Output: the image is inverted 
  '''
  # loop through the width and height of the image
  for w in range(len(pixels)):
    for h in range(len(pixels[0])):

      # get the rgb values and find the inverted pixels 
      pixel = pixels[w][h]
      r = pixel[0]
      g = pixel[1]
      b = pixel[2]

      new_r = 255 - r
      new_g = 255 - g
      new_b = 255 - b

      # set new rgb values to the pixels
      pixels[w][h] = [new_r, new_g, new_b]

  return pixels


def flipHorizontal(pixels):
  '''
  Input: pixels - 2d array of RGB values
  Output: flips image horizontally 
  '''
  # create a new image
  newImage = cmpt120imageProj.createBlackImage(len(pixels),(len(pixels[0])))

  # loop through the new image width and height
  for w in range(len(newImage)):
    for h in range(len(newImage[0])):
      
      # flip the width pixels horizontally 
      newImage[w][h] = pixels[w][h]
      newImage[w][h] = pixels[-w-1][h]
    
  return newImage    

 
def flipVertical(pixels):
  '''
  Input: pixels - 2d array of RGB values
  Output: flips image vertically 
  '''  
  # create a new image 
  newImage = cmpt120imageProj.createBlackImage(len(pixels),(len(pixels[0])))

  #loop through the new image width and height
  for w in range(len(pixels)):
    for h in range(len(pixels[0])):
      
      # flip the height pixels vertically 
      newImage[w][h] = pixels[w][h]
      newImage[w][h] = pixels[w][-h-1]
 
  return newImage


def noRed(pixels):
  '''
  Input:  pixels - 2d array of RGB values
  Output: removes red channels from image
  '''   
  # loop through the width and height of the image
  for w in range(len(pixels)):
    for h in range(len(pixels[0])):
      
      # find the rgb values and remove the red channel
      pix = pixels[w][h]
      r = pix[0]
      g = pix[1]
      b = pix[2]
                          
      no_r = r
      no_r = 0
      
      # set the rgb values to the pixels
      pixels[w][h] = [no_r, g, b]

  return pixels


def noGreen(pixels):
  '''
  Input:  pixels - 2d array of RGB values
  Output: removes green channels from image
  '''   
  # loop through the width and height of the image
  for w in range(len(pixels)):
    for h in range(len(pixels[0])):
      
      # find the rgb values and remove green channel
      pix = pixels[w][h]
      r = pix[0]
      g = pix[1]
      b = pix[2]

      no_g = g
      no_g = 0

      # set the rgb values to the pixels
      pixels[w][h] = [r, no_g, b]

  return pixels


def noBlue(pixels):
  '''
  Input:  pixels - 2d array of RGB values
  Output: removes blue channels from image
  '''   
  # loop through the width and height of the image
  for w in range(len(pixels)):
    for h in range(len(pixels[0])):
      
      #find the rgb values and remove blue channel
      pix = pixels[w][h]
      r = pix[0]
      g = pix[1]
      b = pix[2]

      no_b = b
      no_b = 0

      # set the rgb values to the pixels
      pixels[w][h] = [r, g, no_b]

  return pixels


def grayScale(pixels):
  '''
  Input: pixels - 2d array of RGB values
  Output: converts image into grayScale
  '''   
  # loop through the width and height of the image
  for w in range(len(pixels)):
    for h in range(len(pixels[0])):
      
      # find rgb values 
      pix = pixels[w][h]
      r = pix[0]
      g = pix[1]
      b = pix[2]

      gScale = 0
      
      # determine the average of the original rgb values
      gScale += r + g + b
      newGray = (gScale / 3)

      # set the average rgb values to the pixels
      pixels[w][h] = [newGray, newGray, newGray]

  return pixels


def sepia(pixels):
  '''
  Input: pixels - 2d array of RGB values
  Output: applies sepia filter upon image
  '''   
  # loop through the width and height of the image
  for w in range(len(pixels)):
    for h in range(len(pixels[0])):

      # find the rgb values    
      pix = pixels[w][h]
      r = pix[0]
      g = pix[1]
      b = pix[2]

      # get weighted average of rgb values
      sepiaRed = int((r * .393 + g * .769 + b * .189))
      sepiaGreen = int((r * .349 + g * .686 + b * .168))
      sepiaBlue = int((r * .272 + g * .534 + b * .131))

      # if rgb values are greater than 255, set those to 255     
      if sepiaRed > 255:
        sepiaRed = 255

      if sepiaGreen > 255:
        sepiaGreen = 255

      if sepiaBlue > 255:
        sepiaBlue = 255

      # set the weighted average rgb values to the pixels
      pixels[w][h] = [sepiaRed, sepiaGreen, sepiaBlue]

    
  return pixels


def decreaseB(pixels):
  '''
  Input:  pixels - 2d array of RGB values
  Output: decreases brightness of image
  '''
  # loop through the width and height of the image
  for w in range(len(pixels)):
    for h in range(len(pixels[0])):

      # find the rgb values & decrease channels by 10
      pix = pixels[w][h]
      r = pix[0]
      g = pix[1]
      b = pix[2]

         
      new_r = r - 10
      new_g = g - 10
      new_b = b - 10

      # if new rgb values are less than 0, set them to 0
      if new_r < 0:
        new_r = 0

      if new_g < 0:
        new_g = 0

      if new_b < 0:
        new_b = 0

      # set the new rgb values to the pixels
      pixels[w][h] = [new_r, new_g, new_b]

    
  return pixels


def increaseB(pixels):
  '''
  Input:  pixels - 2d array of RGB values
  Output: increases brightness of image
  '''
  # loop through the width and height of the image
  for w in range(len(pixels)):
    for h in range(len(pixels[0])):

      # find the rgb values & increase the channels by 10           
      pix = pixels[w][h]
      r = pix[0]
      g = pix[1]
      b = pix[2]
    
      new_r = r + 10
      new_g = g + 10
      new_b = b + 10

      # if rgb values are greater than 255, set those to 255  
      if new_r > 255:
        new_r = 255

      if new_g > 255:
        new_g = 255

      if new_b > 255:
        new_b = 255

      # set the rgb values to pixels
      pixels[w][h] = [new_r, new_g, new_b]

  
  return pixels


def rotateLeft(pixels):
  '''
  Input:  pixels - 2d array of RGB values
  Output: rotates image to the left
  '''    
  # create a new image
  new_black = cmpt120imageProj.createBlackImage(len(pixels[0]), (len(pixels)))
  
  # find width and height of the new image
  widthN = len(new_black)
  heightN = len(new_black[0])

  # loop through the new image 
  for w in range(widthN):
    for h in range(heightN):

      # set the original height to the width of the new image
      new_black[w][h] = pixels[h][w]
      
      # turn the new image left
      new_black[w][h] = pixels[-h - 1][w]

  return new_black


def rotateRight(pixels):
  '''
  Input:  pixels - 2d array of RGB values
  Output: rotates image to the right
  '''
  # create new image
  new_black = cmpt120imageProj.createBlackImage(len(pixels[0]), (len(pixels)))
  
  # find width and height of the new image
  widthN = len(new_black)
  heightN = len(new_black[0])
  
  # loop through the new image 
  for w in range(widthN):
    for h in range(heightN):
      
      # set the original height to the width of the new image
      new_black[w][h] = pixels[h][w]
      
      # turn the new image right
      new_black[w][h] = pixels[h][-w - 1]

  return new_black
    

def pixelate(pixels):
  '''
  Input:  pixels - 2d array of RGB values
  Output: pixelates the image
  '''
  # loop through the 4x4 pixels of the image 
  for w in range(0, (len(pixels)), 4):
    for h in range(0, (len(pixels[0])), 4):
        
      averageR = 0
      averageG = 0
      averageB = 0
      
      # loop through each pixel within the 4x4
      for x in range(4):
        for y in range(4):
          
          # determine the value of each pixel
          averageR += pixels[w + x][h + y][0]
          averageG += pixels[w + x][h + y][1]
          averageB += pixels[w + x][h + y][2]

      # convert to integer and find the average of each channel 
      averageR = int(averageR / 16)
      averageG = int(averageG / 16)
      averageB = int(averageB / 16)

      # loop through each pixel within the 4x4
      for a in range(4):
        for b in range(4):

          # set the 4x4 averaged rgb values to all pixels
          pixels[w + a][h + b] = [averageR, averageG, averageB]

  return pixels

def binarize(pixels):
  '''
  Input:  pixels - 2d array of RGB values
  Output: binarizes the image(black & white)
  '''
  totalPix = 0
  image1Total = 0
  image2Total = 0

  # create a new image for a background and duplicate it for a foreground
  image1 = cmpt120imageProj.createBlackImage(len(pixels),len(pixels[0]))
  image2 = cmpt120imageProj.createBlackImage(len(image1),len(image1[0]))

  # loop through the pixels
  for w in range(len(pixels)):
    for h in range(len(pixels[0])):

            # find rgb values
            pix = pixels[w][h]
            r = pix[0]
            g = pix[1]
            b = pix[2]

            # convert image into grayScale
            gScale = 0
            gScale += r + g + b
            newGray =  (gScale / 3)
            pixels[w][h] = [newGray, newGray, newGray]

            # accumalate the red channel pixels of the grayScale
            totalPix += pixels[w][h][0] 

  # determine average threshold of the red channel
  averageThreshold = totalPix/(len(pixels) * len(pixels[0]))

  # loop through width and height 
  for w in range(len(pixels)):
    for h in range(len(pixels[0])):

      # set the background equal to the pixels if it is greater than the average threshold 
      if pixels[w][h][0] > averageThreshold:
        image1[w][h] = pixels[w][h]

      # set the foreground equal to the pixels if it is less than the average threshold 
      elif pixels[w][h][0] < averageThreshold:
        image2[w][h] = pixels[w][h]

      image1Total += image1[w][h][0]
      image2Total += image2[w][h][0]

  # determine the threshold of the background and foreground 
  image1Threshold = image1Total / (len(pixels) * (len(pixels[0])))
  image2Threshold = image2Total / (len(pixels) * (len(pixels[0])))

  # find the total threshold of the background and foreground
  totalThreshold = (image1Threshold + image2Threshold) / 2

  # loop through the width and height 
  for w in range(len(pixels)):
    for h in range(len(pixels[0])):

      # set the pixels to 255 if it is greater than the total threshold
      if pixels[w][h][0] >= totalThreshold:
        pixels[w][h] = [255,255,255]
        
      # set the pixels to 0 if it is less than the total threshold
      elif pixels[w][h][0] <= totalThreshold:
        pixels[w][h] = [0,0,0]
  
  return pixels 

