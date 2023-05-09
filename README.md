# mirrormazeproblem

Approach for finding the path:
If the input laser is horizantal, it means laser travels in same row but column changes. Column number is increased or decreased based on mirror orientation.
If input laser is vertical, it works same as above but this time laser travels in same column but in different row.
If the next position of laser contains mirror, then orientation and direction are changed based on mirror.
This process is repeated until next position is outside the maze and that would be the exit position of laser.



Execution:
----------
I have used the Docker to run the application and below are the commands BUild the image and run it.

docker build . -t sparkhome
docker image ls
docker logs sparkhome
docker run -p 8888:8888 --name spark -d sparkhome

We Can run the python script dureclty using the below command by passing the input file as Argument.
Python  /mirrormaze.py input/sample.txt


I have created folder structures with all files 
input folder has the input txt files.
Output folder with output forom condole.
logs folder has debug file for logging the process we can add this in more places.
src folder has the main source code mirrormaze.py file 
utils folder has mirror and position logic which will be called inside the main script mirrormaze.py 
Included the docker file with docker logic and requirements file with required imports.


Mirror.py :

Mirror sciprt has 2 functions Onemirror and twomirror, which are used to find the Direction and side of the mirror based on the 
inputs direction and side right "R", Left "L".


Position.py :

Position mirror script is used to track position in the path
The directions of the mirror are "H" and "V", "H" is Horizontal directions and "V" is vertical dicrection.
The direction of movements are  "+": increase step and "-": decrease step.


Mirrormaze.py:

Maze path - To find the correct path, dimensions of the borad and the path of the laser.
Nextposition - To find next row and column where the laser travels and to check if the laser is trapped in the maze.

I have includeded the exception handling and Logging as well but not in the entire code and can be improved.



Execution output:
-----------------

Input file1:
-----------

5,4

-1

1,2RR

3,2L

-1

1,0V

-1


Output for file1:
-----------------

The dimensions of board: 4 x 5
Extry of laser position: 0x2 (H+) 
the path of the laser: 
position: 0x2 (H+) 
position: 1x2 (H+) 
position: 2x2 (H+) 
position: 3x2 (V-) 
position: 3x1 (V-) 
position: 3x0 (V-) 
Final exit of laser position: 3x0 (V-)



Inputfile2:
-----------

5,4

-1

1,2RR

3,2L

-1

0,2H

-1


Output for file2:
----------------

The dimensions of board: 4 x 5
Extry of laser position: 1x0 (V+) 
the path of the laser: 
position: 1x0 (V+) 
position: 1x1 (V+) 
position: 1x2 (H+) 
position: 2x2 (H+) 
position: 3x2 (V-) 
position: 3x1 (V-) 
position: 3x0 (V-) 
Final exit of laser position: 3x0 (V-)




I can improve this in a better way by adding more logging and exception handling but due to time constraint I have just added functionality in few places. Thanks for the oppurtunity.