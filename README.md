# Image-Processing-Project -- Finding-Rate-Of-corrosion-of-hexagonal-areas-on-metal-plates

The Project is about -
Detection of rate of corrosion of metal plates, given sample images master sample as well as images
acquired while undergoing chemical processing to remove material. Finding the surface area for which 
the material has been removed.

Solution -
Color image segmentation is used. 

The project coded in python and image processing is done using OpenCV library.
Multiprocessing is done through Pool class of multiprocessing library of Python.
PrettyTable package of Python used for representing the final result.

The challenges faced were -
1) Too large dimension of images.
      For fast processing switched from single threaded --> multithreaded --> multiprocessing.
      
2) Uneven illumination of image and orientation of plate not fixed.

The file Pool.py is the main program.

