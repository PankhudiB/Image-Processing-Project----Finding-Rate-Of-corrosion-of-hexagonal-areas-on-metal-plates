#importing libraries
import cv2
import numpy as np
from matplotlib import pyplot as plt
import math


#for each plate i.e. from 1 to 18
for pic in range(1,19):

    #reading image of plate concerned
    main_img = cv2.imread('s' + str(pic)+ '.png')
    print "plate no. " + str(pic)

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
    average_color_g = np.uint8(average_color_g)
    print average_color_g

    #reading hexagon template
    template = cv2.imread('hexagon.png',0)
    h,w = template.shape

    #setting the x and y co-ordinates    
    x1 = 0
    y1 = 0

    x2 = w
    y2 = h

    i = 0
    j = 0

    #for each hexagon in the plate image
    for cntr in range(0,16):

        #initializing pixel counts of blue and gray
        pixel_cnt_1 = 0
        pixel_cnt_2 = 0
    
        #print str(x1) + " " + str(y1)
        
        print "Hexagon number : " + str(cntr + 1)

        #for each row in the hexagon
        for i in range(y1,y2):
        
            #for each column in the hexagon
            for j in range(x1,x2):
                
                point = np.array(main_img[i,j])

                #calculating euclidean distance 
                my_dist_b = math.sqrt(math.pow(((point[0]/255.0) - (average_color_b[0]/255.0)),2) + math.pow(((point[1]/255.0) - (average_color_b[1]/255.0)),2) + math.pow(((point[2]/255.0) - (average_color_b[2]/255.0)),2))
                my_dist_g = math.sqrt(math.pow(((point[0]/255.0) - (average_color_g[0]/255.0)),2) + math.pow(((point[1]/255.0) - (average_color_g[1]/255.0)),2) + math.pow(((point[2]/255.0) - (average_color_g[2]/255.0)),2))
            
                if my_dist_b < 0.15 :                   #for blue
                    pixel_cnt_1 = pixel_cnt_1 + 1
               
                elif my_dist_g < 0.25 :                 #for gray
                    pixel_cnt_2 = pixel_cnt_2 + 1

       
            
        if cntr == 7:       
            x1 = w + 4
            y1 = 0
            x2 = 2 * w 
            y2 = h            
        else:
            y1 = y2 + 7
            y2 = y2 + h + 7
        
        
        print "blue : " + str(pixel_cnt_1)
        print "gray : " + str(pixel_cnt_2)        
        print "=================="
        
    print "-------------------------------------------------------------------"
