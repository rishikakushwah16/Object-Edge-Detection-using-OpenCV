# Object-Edge-Detection-using-OpenCV

In this project, we will be automatically detecting the edges of the object along with making a GUI using the Tkinter module in python. This user interface module will enable us to click a select button, thereby showing a file choosing dialog box to choose a file from the disk. We will load the chosen image using OpenCV, implementing the edge detection and moreover, showcasing the original image and edge detected image in our GUI. 
The edge detection method that we are going to use is known as canny edge detection offered by Open CV. This popular edge detection method was developed by John F. Canny in 1986. 
First, we will be installing the OpenCV package in our PyCharm, First open your PyCharm and create a new project then click on the file in PyCharm editor then click on the project: project name, followed by project interpreter, then click on '+', search OpenCV-python, finally click install package, we will also be requiring Tkinter module so run pip install tk command on your PyCharm’s Terminal. Now you are good to go.


There are five steps that are followed for canny edge detection.
1.	First is, noise detection, since edges are prone to have noise in the image. So here the aim is to remove the noise with the help of a 5×5 Gaussian filter.
2.	The second step involves the estimation of gradients.
3.	The third step involves Non-maximum suppression, which is after preparing the gradient magnitude and direction, a full scanning of the image is carried out to remove the unwanted pixels which may not include the edge. For the same purpose, at every pixel, the pixel is checked if it is a local maximum in its neighborhood in the direction of the gradient.
4.	The fourth step includes a double threshold on all the detected edges.
5.	Finally, the last step includes, analysis of all the edges and their associations.
All five steps can be performed using a just function known as cv2.canny().

We will use Tkinter to access our GUI functions with other packages like Image and ImageTk modules from PIL/Pillow to show the picture in our GUI. The filedialog allows us to navigate through our file system and select an image to perform edge detection. import the package cv2, and then we will read our image by using the imread function. Make sure the image is in the same directory as your project. Then we will be using the canny function.
Make a choose_image function. In this, we will catch a global reference to panel A and Panel B. These are our image panels, which means it will seize an image and showcase it in our GUI. Panel A will show us the original image and Panel B will how us the edge detected image.


Now we will ensure that file is selected and we did not click the 'cancel' button if the path is selected, we will upload the image from the disk and convert the image to grayscale. In our canny function, we have our input image, minValue, and maxValue. So, in all five steps, OpenCV encompasses all the above single functions, first, the parameter is our input image. The second and third parameters are our minValue and maxValue respectively. The third parameter is the aperture size. It is the size of the Sobel kernel used to find the image gradients. By default, it is three. The last parameter is the L2 gradient which tells the equation to find the gradient magnitude. If it is true, it uses the equation mentioned earlier otherwise it uses the function Edge_Gradient (G)= |GX| +|GY|, by default it is false.
Since OpenCV shows images in BGR order but PIL represents images in RGB order, so we need to change the channels and convert the image to PIL format and then to ImageTk format.
Now without reference, our image will be erased and we won't be able to show them on the screen so we need to make an instance for each image.
Now we will make a create button and add it to our interface. When we will click the button, it will open a file dialog box which will allow us to choose an image from the disk.
Now, run python edge_detection.py on PyCharm terminal. 

Click on Select an image button and you can select as many images as you want.
