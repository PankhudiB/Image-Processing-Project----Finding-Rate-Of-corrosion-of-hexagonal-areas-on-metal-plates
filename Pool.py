#importing libraries
import cv2
import numpy as np
from matplotlib import pyplot as plt
import math
import threading
import thread
from multiprocessing import Pool
from prettytable import PrettyTable



#for blue color
img = cv2.imread('img_square_blue.png')
average_color_per_row = np.average(img,axis=0)
average_color_b = np.average(average_color_per_row,axis =0)
average_color_b = np.uint8(average_color_b) 
print average_color_b

#reading hexagon template
template = cv2.imread('h1use.jpeg',0)
h,w = template.shape
  

def multi_run_wrapper(args):
    return process_image(* args)


def process_image(main_img,x1,x2,y1, y2):
    pixel_cnt_1 = 0

    #for each row in the hexagon
    for i in range(y1,y2):
        
        #for each column in the hexagon
        for j in range(x1,x2):
            #print "i: " + str(i)  + " J " + str(j)
            point = np.array(main_img[i,j])

            #calculating euclidean distance 
            my_dist_b = math.sqrt(math.pow(((point[0]/255.0) - (average_color_b[0]/255.0)),2) + math.pow(((point[1]/255.0) - (average_color_b[1]/255.0)),2) + math.pow(((point[2]/255.0) - (average_color_b[2]/255.0)),2))
            
            
            if my_dist_b < 0.1 :                   #for blue
                pixel_cnt_1 = pixel_cnt_1 + 1
                           

    return pixel_cnt_1
    #print "blue : " + str(pixel_cnt_1)
    #print "=================="



if __name__ == '__main__':

    #for tabbular output
    t = PrettyTable(['Plate No','hex-1','hex-2','hex-3','hex-4','hex-5','hex-6','hex-7','hex-8','hex-9','hex-10','hex-11','hex-12','hex-13','hex-14','hex-15','hex-16'])

    #for all the samples
    for pic in range(1,19):

        #reading image of plate concerned
        main_img = cv2.imread('ss' + str(pic)+ '.jpeg')
        print "Currently working on plate no. " + str(pic)

        #for multiprocessing
        p = Pool(16)        
        res = p.map(multi_run_wrapper,[(main_img,0,w,0,h),(main_img,0,w,h+5,2*h - 10),(main_img,0,w,2*h +5 ,3*h -10),(main_img,0,w,3*h+5,4*h - 10),(main_img,0,w,4*h + 5,5*h - 10),(main_img,0,w,5*h+5,6*h - 10),(main_img,0,w,6*h +5,7*h-10),(main_img,0,w,7*h+5,8*h-10),(main_img,w,2*w,0+5,h -10),(main_img,w,2*w,h+5,2*h-10),(main_img,w,2*w,2*h+5,3*h-10),(main_img,w,2*w,3*h+5,4*h-10),(main_img,w,2*w,4*h+5,5*h-10),(main_img,w,2*w,5*h+5,6*h-10),(main_img,w,2*w,6*h+5,7*h-10),(main_img,w,2*w,7*h+5,8*h-10)])

        #for indicating the plate no.
        a = [pic]
        result = a + res

        #result added to table
        t.add_row(result)

    #final output
    print t
