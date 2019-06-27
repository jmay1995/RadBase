import logging
import click

from logging import debug, info

from program.utils import FindAndReadInputFile
from program.model import RadClass

#Enable default values for the command line
@click.command()
@click.option('--filename', default=None, help='Name of file in `inputs` folder to read data from')
def runner(filename):

    RadInput = FindAndReadInputFile(filename)

    RadObject = RadClass('RadBase', RadInput.df)
