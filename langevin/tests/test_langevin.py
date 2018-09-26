#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `langevin` package."""

import pytest

from click.testing import CliRunner

from langevin import langevin
from langevin import cli
from langevin import *


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
