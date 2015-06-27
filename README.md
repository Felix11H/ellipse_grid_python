
# Ellipse Grid Python

Ellipse Grid Python generates grid points inside an ellipse. This a program is a Python implementation of John Burkardt's ellipse_grid c++ code available at http://people.sc.fsu.edu/~jburkardt/c_src/ellipse_grid/ellipse_grid.html


### Licensing:
  
This code is distributed under the GNU LGPL license.


### Author:

Original Version: John Burkardt, Python Implementation: [Felix Hoffmann] 


### Discussion:

The ellipse is specified as

( ( X - C1 ) / R1 )^2 + ( ( Y - C2 ) / R2 )^2 = 1

The user supplies a number N.  There will be N+1 grid points along the shorter axis.


###  Parameters:

Input, N, the number of subintervals on the shorter half axis.

Input, r1, length of the first half axis.

Input, r2, length of the second half axis.

Input, c1, x-coordinate of the center of the ellipse.
  
Input, c2, y-coordinate of the center of the ellipse.
  
Output, xy, list of grid points.


[Felix Hoffmann]:http://felix11h.github.io/