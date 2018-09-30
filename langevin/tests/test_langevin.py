#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `langevin` package."""

import pytest

from click.testing import CliRunner

from langevin import langevin
from langevin import cli
from langevin import *
from os import path
test_dir = path.dirname(__file__)
import argparse
@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'langevin.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output
def test_step():
    '''tests the step function for a single timestep'''
    
    class args:
        def __init__():
            pass

        time_step = .1
        total_time = 100.0
        initial_position = 0
        initial_velocity = 10
        damping_coefficient = 1.0
        temperature = 1.0
    
    
    xi=0
    vi=10
    
    a,b=langevin.step(xi, vi, args, testing=True)
    assert a>xi
    assert b<vi
def test_write_output():
    '''tests that the output function can write a mock'''
    
    output_example=test_dir+r'\output_test'
    index=[0,1,2,3,4]
    time=[0,.2,.4,.6,.8]
    position=[0,.7,-.4,3,.3]
    velocity=[.7,2,6,2,6]
    
    langevin.write_output(index,velocity,position,time,output_example)
    
    with open(output_example,'r') as f:
        test=f.read()
    with open(test_dir+r'/output_test_correct.txt', 'r') as h:
        correct=h.read()
    assert(test==correct)

def test_run():
    '''tests that the run function performs correctly'''
    
    
    class args:
        def __init__():
            pass

        time_step = .1
        total_time = 100.0
        initial_position = 0
        initial_velocity = 10
        damping_coefficient = 1.0
        temperature = 1.0
        output=test_dir+r'output_test.txt'
        
    v=langevin.run(args)[0]
    assert v[-1]==5 or v[-1]==0

import unittest   
    
    
class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertRaises(argparse.ArgumentTypeError, langevin.check_in_bounds,6)
        self.assertRaises(argparse.ArgumentTypeError, langevin.check_in_bounds,-1)
        a=langevin.check_in_bounds(4)
        assert a is True
        