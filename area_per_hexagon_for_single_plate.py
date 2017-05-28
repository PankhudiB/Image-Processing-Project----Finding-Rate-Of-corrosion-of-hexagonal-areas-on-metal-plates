#importing libraries
import cv2
import numpy as np
from matplotlib import pyplot as plt
import math


#reading main image of concern
main_img = cv2.imread('s1.png')
#main_img = cv2.resize(main_img,None,fx= 0.1, fy= 0.1, interpolation = cv2.INTER_CUBIC)

cv2.imwrite('hm.png',main_img)

img_gray = cv2.cvtColor(main_img, cv2.COLOR_BGR2GRAY)


#calulating average colors

#for blue color
img = cv2.imread('img_square_blue.png')
average_color_per_row = np.average(img,axis=0)
average_color_b = np.average(average_color_per_row,axis =0)
average_color_b = np.uint8(average_color_b)

#for gray color
img2 = cv2.imread('img_square_gray.png')
average_color_per_row = np.average(img2,axis=0)
average_color_g = np.average(average_color_per_row,axis =0)
print average_color_g
average_color_g = np.uint8(average_color_g)
print average_color_g



#reading hexagon template
template = cv2.imread('hexagon.png',0)

h,w = template.shape
print "h : " + str(h) + "w : "+ str(w)


"""
print "top"
print top_left[0]
print top_left[1]
print "bottom"
print bottom_right[0]
print bottom_right[1]
"""

x1 = 0
y1 = 0


x2 = w
y2 = h



blank_img = cv2.imread('initial.png');

blank_img[:,:,0] = 0
blank_img[:,:,1] = 0
blank_img[:,:,2] = 0

i = 0
j = 0


# 0 - 8 

for cntr in range(0,16):
    pixel_cnt_1 = 0
    pixel_cnt_2 = 0
    pixel_cnt_3 = 0
    
    #print "total" + str(w*h)
    print str(x1) + " " + str(y1)
    blank_img[:,:,0] = 0
    blank_img[:,:,1] = 0
    blank_img[:,:,2] = 0
    

    #print "y1 : " + str(y1)
    #print "y2 : " + str(y2)

    print "cntr : " + str(cntr + 1)
        
    for i in range(y1,y2):
        
        #print "i : " + str(i)
        for j in range(x1,x2):
            #print "j : " + str(j)
        
            point = np.array(main_img[i,j])
            
            my_dist_b = math.sqrt(math.pow(((point[0]/255.0) - (average_color_b[0]/255.0)),2) + math.pow(((point[1]/255.0) - (average_color_b[1]/255.0)),2) + math.pow(((point[2]/255.0) - (average_color_b[2]/255.0)),2))
            my_dist_g = math.sqrt(math.pow(((point[0]/255.0) - (average_color_g[0]/255.0)),2) + math.pow(((point[1]/255.0) - (average_color_g[1]/255.0)),2) + math.pow(((point[2]/255.0) - (average_color_g[2]/255.0)),2))
            
            #blank_img[i,j] = main_img[i,j]
            
            #print my_dist
            
            if my_dist_b < 0.15 :
               pixel_cnt_1 = pixel_cnt_1 + 1
               
            elif my_dist_g < 0.25 :
                pixel_cnt_2 = pixel_cnt_2 + 1

       
            
        #print "j : " + str(j)

    
    #print "i : " + str(i)
    if cntr == 7:
        x1 = w + 4
        y1 = 0
        x2 = 2 * w 
        y2 = h
        print "now : y: " + str(y1) + "," + str(y2)
        print "now : x: " + str(x1) + "," + str(x2)        
    else:
        y1 = y2 + 7
        y2 = y2 + h + 7
        
        
    print "blue : " + str(pixel_cnt_1)
    print "gray : " + str(pixel_cnt_2)
    print "white : " + str(pixel_cnt_3)
    print "=================="
    
cv2.imwrite('hi2.png',blank_img)

print "-------------------------------------------------------------------"
