# -*- coding: utf-8 -*-

"""Main module."""
import argparse 
import numpy as np
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
from os import path

testing_directory=path.join(path.dirname(__file__), r'tests')


def check_in_bounds(value):
    ivalue = float(value)
    if ivalue <= 0 or ivalue>=5:
        raise argparse.ArgumentTypeError("%s is an invalid starting position based on the size of the box" % value)
    else:
        return True 

def parse_arguments(): # pragma: no cover
    '''Get arguements from the command line'''
    parser=argparse.ArgumentParser(description='Langevin Dynamics in Python')
    parser.add_argument('--initial_position', type=check_in_bounds, default=0)
    parser.add_argument('--initial_velocity', type=float, default=0)
    parser.add_argument('--temperature', type=float, default=300)
    parser.add_argument('--damping_coefficient', type=float, default=.1)
    parser.add_argument('--time_step', type=float, default=.1)
    parser.add_argument('--total_time', type=float, default=1000)
    parser.add_argument('--output', type=str, default=testing_directory+ r'output_test')
    return parser.parse_args()
                           
def write_output(index,velocity,position,time,output_file):

    '''writes an output file
    
    
    index:  array of indices
    velocity:  array of velocities
    position:  array of positions
    time:  array of times
    output_file:  where to write the output to
    
    '''
    with open(output_file, 'w') as f:
        for i in range(len(index)):
            f.write('{0}, {1:0.06f}, {2:0.06f}, {3:0.06f}\n'.format(index[i], time[i], position[i], velocity[i]))
                       
def step(xi,vi,args,testing=False):
    '''calculate one timestep using eulers method
    xi: position value 
    vi:  velocity value
    args: command line arguments
    testing:  True if unit testing to avoid affects of random force'''
    
    
    
    drag=-1*args.damping_coefficient*vi
    random=np.random.normal(0, 2*args.temperature*args.damping_coefficient)
    if testing:
        force=drag
    else:
        force=drag+random
    vj=vi+(force*args.time_step)
    xj=xi+(vi*args.time_step)
    return xj,vj
def run(args):
    '''runs the simulation for number of timesteps based on totaltime/time_step
    args: command line arguments'''
    cycles=int(args.total_time/args.time_step)
    xi=args.initial_position
    vi=args.initial_velocity
    velocity_array=[vi]
    position_array=[xi]
    time_array=[0]
    index_array=[0]
    for i in range(cycles):
        xj,vj=step(position_array[-1], velocity_array[-1], args)
        velocity_array.append(vj)
        position_array.append(xj)
        time_array.append((i+1)*args.time_step)
        index_array.append(i+1)
        if position_array[-1]>=5:
            del position_array[-1] #dont want the point that's outside of the wall
            position_array.append(5) #fudge last point for graphing purposes
            break
        if position_array[-1]<0:
            del position_array[-1] #see above
            position_array.append(0) #for graphing
            break
    write_output(index_array,velocity_array,position_array,time_array,args.output)
    #print(velocity_array[-1],position_array[-1], args.output)
    
    
    figposition=plt.figure()
    position=figposition.add_subplot(111)
    position.plot(time_array, position_array, 'o')
    position.set_xlabel('Time')
    position.set_ylabel('Position')
    position.set_title('Position Graph of Brownian Motion Particle')
    figposition.savefig('trajectory.png')
    
    
    
    return [position_array, time_array, velocity_array]

def hist(args):
    '''calls run function until 100 runs that end with the particle hitting wallsize=5 are recorded.  Makes a histogram of times it took the particle to hit the wallsize, and plots the trajectory of the last run to hit the wall
    
    args:  command line arguments'''
    
  
    count=0
    times=[]
    while count<100:
        result=run(args)
        if result[0][-1]==5:
            times.append(result[1][-1])
            count+=1
        
    plt.plot(result[1], result[0], 'o')
    plt.xlabel('Time')
    plt.ylabel('Position')
    plt.title('Position Graph of Brownian Motion Particle')
    plt.savefig('trajectory.png')
    plt.clf()
    
    
    
    plt.hist(times)
    plt.xlabel('times')
    plt.ylabel('number of occurances')
    plt.title('histogram of wall times')
    plt.savefig('histogram.png')
    
    plt.clf()
    
    
    
    print(result[2][-1],result[0][-1], args.output)
    return times
def main(): #pragma: no cover
    args=parse_arguments()
    hist(args)
        
if __name__=='__main__':
    main() #pragma: no cover
        
        
    
                        
                       

