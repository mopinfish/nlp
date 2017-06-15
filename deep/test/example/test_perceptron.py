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

##########################################
# below test cases
##########################################
def test_perceptron_AND1():
  x1, x2 = 1, 1
  expect = 1
  assert perceptron.AND(x1, x2) == expect
 
def test_perceptron_AND2():
  x1, x2 = 0, 0
  expect = 0
  assert perceptron.AND(x1, x2) == expect

def test_perceptron_AND3():
  x1, x2 = 1, 0
  expect = 0
  assert perceptron.AND(x1, x2) == expect
 
def test_perceptron_AND4():
  x1, x2 = 0, 1
  expect = 0
  assert perceptron.AND(x1, x2) == expect
