# Auxiliary functions
import numpy as np

def evolve(cond,time,a,d,L):
    x0,v0,t0 = cond[0], cond[1], cond[2]
    dt, tf = time[0], time[1]
    x_array = [x0]
    v_array = [v0]
    t_array = [t0]
    t = t0
    x = x0
    v = v0
    while(t<tf):
        if (x<d):
            t  = t+dt
            t_array.append(t)
            dv = a*dt
            v  = v+dv
            v_array.append(v)
            dx = v*dt
            x  = x+dx
            x_array.append(x)
        elif (x>d and x<L):
            t  = t+dt
            t_array.append(t)
            dv = 0
            v  = v+dv
            v_array.append(v)
            dx = v*dt
            x  = x+dx
            x_array.append(x)
        else:
            t  = t+dt
            t_array.append(t)
            v = 0
            v_array.append(v)
            dx = 0
            x  = x+dx
            x_array.append(x)
    return x_array, v_array, t_array
