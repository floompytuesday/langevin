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

def runge_kutta(xi,vi,args,testing=False):
    drag=-1*args.damping_coefficient
    random=np.random.normal(0,2*args.temperature*args.damping_coefficient)
    k1=drag*vi+random
    k2=drag*(vi+1/2*k1)
    k3=drag*(vi+1/2*k2)
    k4=drag*(vi+*k3)
    vj=vi+1/6*(k1+2k2+2k3+k4)+random
    xj=xi+vi*args.time_step
    return vj,xj
    
                          
    


def step(xi,vi,args,testing=False):
    #calculate one timestep using eulers method
    drag=-1*args.damping_coefficient*vi
    random=np.random.normal(0, 2*args.temperature*args.damping_coefficient)
    if testing:
        force=drag
    else:
        force=drag+random
    vj=vi+force*args.time_step
    xj=xi+vi*args.time_step
    return xj,vj

