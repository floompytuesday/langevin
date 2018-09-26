# -*- coding: utf-8 -*-

"""Main module."""
import argparse 
import numpy as np
from os import path
np.random.seed(42)
testing_directory=path.join(path.dirname(__file__), 'tests')

def parse_arguments():
    '''Get arguements from the command line'''
    parser=argparse.ArgumentParser(description='Langevin Dynamics in Python')
    parser.add_argument('--initial_position', type=float, default=1)
    parser.add_argument('--initial_velocity', type=float, default=1)
    parser.add_argument('--temperature', type=float, default=10)
    parser.add_argument('--damping_coefficient', type=float, default=1)
    parser.add_argument('--time_step', type=float, default=.1)
    parser.add_argument('--total_time', type=float, default=10)
    parser.add_argument('--output', type=str, default=testing_directory+r'output_test.txt')
    return parser.parse_args()

args=parse_arguments()




def runge_kutta(xi,vi,args,testing=False):
    drag=-1*args.damping_coefficient
    random=np.random.normal(0,2*args.temperature*args.damping_coefficient)
    k1=drag*vi+random
    k2=drag*(vi+1/2*k1)
    k3=drag*(vi+1/2*k2)
    k4=drag*(vi+k3)
    vj=vi+1/6*(k1+2*k2+2*k3+k4)+random
    xj=xi+vi*args.time_step
    return vj,xj
    
                          
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
    vj=vi+force*args.time_step
    xj=xi+vi*args.time_step
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
    write_output(index_array,velocity_array,position_array,time_array,args.output)
    return velocity_array
run(args)
        
        
    
                        
                       

