    The source code of Project A: Raytracer, source code could also be found
on my github. Link was shown below:
(https://github.com/Parlin-Galanodel/PythonComputingProject-2ndYr/tree/master/PyProject)

    Tips: The source code was carefully tested and was guaranted that it could be 
	run on my own laptoppython 2.7.9, anaconda distribution, windows 7 professional
	version). But it(Singlesurface.py & Planocovex.py to be exactly) sometimes 
	failed on computers in computing suite when running in ipython or qtconsole.

	  Considering about the fact that Enthought distribution was used in college, it
	might because the internal difference between two different distributions and I
	could not solve it.
	  
	  If the code failed, just run it in a pure python environment(use python
	command to run that file from terminal). All the code worked fine in pure 
	python environment.

	  Also, the 5 files must be placed in the same directory.


    The source code was divided into 5 files. raytracer.py & functions.py are the two
main part and genpolar.py is jsut a function from task 15 in worksheet 1 while it is
base part in implementing functions.py module.



  raytracer.py:
	This module contains all the basic blocks in this project. They are definitions
of Ray class, OpticalElement class and its two subclasses SphericalRefraction and 
Planoconvex. I believe these classes were documented and commented properly.



  functions.py:
	This module is all the function would be used to operate the rays and lens
classes defined in raytracer module. It provide a convinent way to simulate rays
through different kinds of surfaces or lens and do related ploting work.



  Singlesurface.py & Planocovex.py

	All the simulation works could be done by these two module if functions and
objects were used properly and in some reasonable order. 

	To make this process easier, I made singlesurface.py module and it is used to
do test on single surface, some tips would be printed on screen when running that
module. 

	planoconvex.py is a module twisted from singlesurface.py. Its code is nearly
same as singlesurface.py and the name gave a good discription that it is used to do 
testing on planoconvex lens.

	These two module would make the experiment much easier.