# coding: utf-8
from unittest import TestCase
from os import path
APP_ROOT = path.dirname( path.abspath( __file__ ) ) + "/../"
MODULE_PATH = APP_ROOT + 'src/examples'

##########################################
# resolve expamples path for import 
##########################################
import sys
sys.path.append(MODULE_PATH)
print  MODULE_PATH
import perceptron
