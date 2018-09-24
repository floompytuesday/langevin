# -*- coding: utf-8 -*-

"""Main module."""
import argparse 
import numpy as np


def parse_arguments():
    '''Get arguements from the command line'''
    parser=argparse.ArgumentParser(description='Langevin Dynamics in Python')
    parser.add_argument('--initial_position', type=float, default=1)
    parser.add_argument('--initial_velocity', type=float, default=1)
    parser.add_argument('--temperature', type=float, default=10)
    parser.add_argument('--damping_coefficient', type=float, default=1)
    parser.add_argument('--time_step', type=float, default=1)
    parser.add_argument('--total_time', type=float, default=10)
    
    return parser.parse_args()

args=parse_arguments()

velocity_array=[args.initial_velocity]
position_array=[args.initial_position]
time_array=[0]



def step(xi,vi,args,testing=False):
    #calculate one timestep using eulers method
    drag=-1*args.damping_coefficient*args.initial_velocity
    random=np.random.normal(0, 2*args.temperature*args.damping_coefficient)
    if testing:
        force=drag
    else:
        force=drag+random
    vj=vi+force*args.time_step
    xj=xi+vi*args.time_step
    return xj,vj

