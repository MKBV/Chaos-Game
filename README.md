# Chaos Game
One day on youtube there was a video which name contains Chaos Game, 
and my love of superior math was amazed by [the video](https://youtu.be/IGlGvSXkRGI).

Processes mentioned on video:
 1. Draw a shape.  
 2. Pick a random point from the inside of the shape  
 3. Pick a random corner and put a dot at the midpoint of these two points.  
 4. Do the 3rd process for the new dot.  


## Writing the Script
When writing these operations to the code, we need to define certain algorithms.  
 - How do we understand the random point was in the shape?  
 - When our shape has 4 or more corners, we need to dismiss some corners.* How?  

First of all, I use the turtle module for the graphical interface.  
It's really simple and I can draw shapes by just use some coordinates.  

To pick a random point from inside of the shape, I use that algorithm:  

![Areas](/Img/Area_exmp.jpg)

If we draw triangles with a random point and 2 corners, the area of triangles must be equal to the area of the shape.  
Nor the point isn't inside of the shape.  

`1+2+3+4 == Area of Squere`

Then we chose a random corner and find the midpoint between the corner and the point.  
That is the easiest part of the code. Because has a simple math formula.  
And when we put dots to midpoints, the script must be finished.  

After a while of this progression, I got shapes like these.  

![Images](/Img/Images.jpg)

## 4+ Corner Problem
That algorithm is perfectly run at the triangle, but if the shape has 4 or more corners we'll see a miscorrect pattern.  

![unchanged algorithm with sqruare](/Img/Faulty.png)

You can change the pattern by changing the corner order.  
If we chose a different corner from the last process there won't appear a misspattern. **(Example 2nd )**  
Or you can dismiss the next corner (Example 3rd) or the next 2nd corner **(Example 4th)**.  
