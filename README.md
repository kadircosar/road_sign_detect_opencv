# Road sign detector and classifier 
İn this project we will detect and classify the signs below by using opencv.



   <img width="200" src=images/1.jpg></a>
   <img width="200" src=images/2.jpg></a>
   <img width="200" src=images/3.jpg></a>
   <img width="200" src=images/4.jpg></a>
   <img width="135" src=images/5.png></a>
   
   # Opencv
OpenCV (Open Source Computer Vision Library) is an open source computer vision and machine learning software library. OpenCV was built to provide a common infrastructure for computer vision applications and to accelerate the use of machine perception in the commercial products. Being a BSD-licensed product, OpenCV makes it easy for businesses to utilize and modify the code.

The library has more than 2500 optimized algorithms, which includes a comprehensive set of both classic and state-of-the-art computer vision and machine learning algorithms. These algorithms can be used to detect and recognize faces, identify objects, classify human actions in videos, track camera movements, track moving objects, extract 3D models of objects, produce 3D point clouds from stereo cameras, stitch images together to produce a high resolution image of an entire scene, find similar images from an image database, remove red eyes from images taken using flash, follow eye movements, recognize scenery and establish markers to overlay it with augmented reality, etc. OpenCV has more than 47 thousand people of user community and estimated number of downloads exceeding 18 million. The library is used extensively in companies, research groups and by governmental bodies.

Along with well-established companies like Google, Yahoo, Microsoft, Intel, IBM, Sony, Honda, Toyota that employ the library, there are many startups such as Applied Minds, VideoSurf, and Zeitera, that make extensive use of OpenCV. OpenCV’s deployed uses span the range from stitching streetview images together, detecting intrusions in surveillance video in Israel, monitoring mine equipment in China, helping robots navigate and pick up objects at Willow Garage, detection of swimming pool drowning accidents in Europe, running interactive art in Spain and New York, checking runways for debris in Turkey, inspecting labels on products in factories around the world on to rapid face detection in Japan.

It has C++, Python, Java and MATLAB interfaces and supports Windows, Linux, Android and Mac OS. OpenCV leans mostly towards real-time vision applications and takes advantage of MMX and SSE instructions when available. A full-featured CUDAand OpenCL interfaces are being actively developed right now. There are over 500 algorithms and about 10 times as many functions that compose or support those algorithms. OpenCV is written natively in C++ and has a templated interface that works seamlessly with STL containers.


                                                                                                                                                                                                                                                                                                                                                   






We will use the HoughCircles() function of OpenCV to detect circles present in an image.
# Circle Hough Transform
The circle Hough Transform (CHT) is a basic feature extraction technique used in digital image processing for detecting circles in imperfect images. The circle candidates are produced by “voting” in the Hough parameter space and then selecting local maxima in an accumulator matrix.
It is a specialization of Hough transform.

If you want to learn more information about Hough transfrom you can check link below.
https://en.wikipedia.org/wiki/Circle_Hough_Transform#:~:text=The%20circle%20Hough%20Transform%20(CHT,maxima%20in%20an%20accumulator%20matrix.
# cv2.KMEANS_RANDOM_CENTERS
After circle detection we will use cv2.KMEANS_RANDOM_CENTERS.
This function allows us to obtain the dominant colors in a certain area.
We will use three frames in the detected circle to classify signs by required if statements.
The key is decide best frames to classify signs.
The following frames on forward sign is  the positions of the frames that i chose.

   <img width="300" src=images/key.jpg></a>
   
The last part is tuning if statements by dominant colors. 
And that's it :)
# Detected Signs
Here the examples of detected signs.



 <img width="300" src=images/speed_limit.png></a>
   <img width="300" src=images/forward.png></a>
   <img width="300" src=images/right.png></a>
   <img width="300" src=images/stop.png></a>
   <img width="300" src=images/yolyok.png></a>
# How to use 
We begin by cloning the road_sign_detect_opencv repository.
In a terminal, type:

```bash
git clone https://github.com/kadircosar/road_sign_detect_opencv.git
```

Then we just run script in terminal:

```bash
python3 road_sign_classifier.py
```
















