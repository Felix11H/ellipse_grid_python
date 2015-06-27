import matplotlib.pyplot as plt

'''

  PYTHON_ELLIPSE_GRID generates grid points inside an ellipse.

    This a python implementation of John Burkardt's ellipse_grid c++ code available at http://people.sc.fsu.edu/~jburkardt/c_src/ellipse_grid/ellipse_grid.html


  Licensing:
    
    This code is distributed under the GNU LGPL license.


  Author:

    Original Version: John Burkardt, Python Implementation: Felix Hoffmann, http://felix11h.github.io/


  Discussion:

    The ellipse is specified as

      ( ( X - C1 ) / R1 )^2 + ( ( Y - C2 ) / R2 )^2 = 1

    The user supplies a number N.  There will be N+1 grid points along
    the shorter axis.


  Parameters:

    Input, N, the number of subintervals on the shorter half axis.

    Input, r1, length of the first half axis.

    Input, r2, length of the second half axis.

    Input, c1, x-coordinate of the center of the ellipse.
    
    Input, c2, y-coordinate of the center of the ellipse.
    
    Output, xy, list of grid points.


'''





def i4_ceiling(x):

    int_x = int(x)

    if int_x < x:
        int_x += 1

    return int_x


def plot_the_ellipse(xy, r1, r2):

    from matplotlib.patches import Ellipse

    xy_x = [x for k,x in enumerate(xy) if k%2==0]
    xy_y = [y for k,y in enumerate(xy) if k%2==1]

    
    fig = plt.figure(facecolor='white')
    ax = fig.add_subplot(111, aspect='equal')
    E = Ellipse([0,0], 2*r1, 2*r2)
    E.set_alpha(0.1)
    ax.add_artist(E)

    ax.scatter(xy_x, xy_y)

    fig.show()
    

def generate_ellispe_grid(N, r1, r2, c1 = 0, c2 = 0, plot_ellipse = True):

    xy = []

    if r1 < r2:
    
        h = 2.0 * r1/(float(2*N+1))
        ni = N
        nj = i4_ceiling(float(r2)/float(r1)) * N        
    
    else:

        h = 2.0 * r2/(float(2*N+1))
        nj = N
        ni = i4_ceiling(float(r1)/float(r2)) * N   
    


    p = 0
    j = 0

    while j <= nj:

        i = 0
        x = c1
        y = c2 + j*h

        xy.append(x)
        xy.append(y)
    
        p += 1

        if 0 < j:

          xy.append(x)
          xy.append(2.0 * c2 - y)
          p += 1

        while True:

            i += 1
            x = c1 + i*h

            if 1.0 < ((x - c1)/float(r1))**2 + ((y - c2)/float(r2))**2:
                break

            xy.append(x)
            xy.append(y)
            p += 1
            xy.append(2.0 *c1 - x)
            xy.append(y)
            p += 1
        
            if 0 < j:

                xy.append(x)
                xy.append(2.0 * c2 - y)
                p += 1
                xy.append(2.0 * c1 - x)
                xy.append(2.0 * c2 - y) 
                p += 1

        j += 1
   
  
    if plot_ellipse:
        plot_the_ellipse(xy, r1, r2)

    print len(xy)/2.
    return xy



    


