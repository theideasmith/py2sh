import os
import sys
import clipy
import unittest
from scipy.constants import mu_0, pi

class clipyTests(unittest.TestCase):
  def test_collectsKwargNumbers(self):
    string = "hello=4  world=3.3  zen=.4"
    args = clipy.collectkwargs(string)
    self.assertEqual(args["hello"], 4)
    self.assertEqual(args["world"], 3.3)
    self.assertEqual(args["zen"], .4)

  def test_collectsKwargStrings(self):
    string = 'hello=world joke="Chicken crosses road"'
    args = clipy.collectkwargs(string)
    self.assertEqual(args["hello"], "world")
    self.assertEqual(args["joke"], "Chicken crosses road")

  def test_collectsKwargsKeyHasIntegral(self):
    from scipy.constants import mu_0
    string = "mu_0=1.2566370614359173e-06 pi=3.14 zeta=.4"
    args = clipy.collectkwargs(string)
    self.assertEqual(args["mu_0"], mu_0)
    self.assertEqual(args["pi"], 3.14)
    self.assertEqual(args["zeta"], .4)

  def test_collectsIntegralAndStrings(self):
    string='mu_0=1.2566370614359173e-06  joke="Chicken on road"'
    args = clipy.collectkwargs(string)
    self.assertEqual(args["mu_0"], 1.2566370614359173e-06)
    self.assertEqual(args["joke"], "Chicken on road")

  def test_collectsArgs(self):

    string=[
        "1.25663706144e-06" + " ",
        'android1234.45&234'
    ]
    string = ''.join(string)
    matches = clipy.collectargs(string)
    should = [1.25663706144e-06,"android1234.45&234"]
    self.assertEqual(matches[0], should[0])
    self.assertEqual(matches[1], should[1])
    
  def test_collectsKwargsAndArgs(self):
    args=[
        "1.25663706144e-06" + " ",
         'android1234.45&234'
    ]
    kwargs_string='DarthVader =An evil sith, GibbsSampling=A sampling algorithm'
    string = ''.join(args)
    string += "  " + kwargs_string
    kwargs, args= clipy.parseargs(string)
    self.assertEqual(kwargs["DarthVader"],"An evil sith")
    self.assertEqual(kwargs["GibbsSampling"], "A sampling algorithm")

    self.assertEqual(args[0], 1.25663706144e-06)
    self.assertEqual(args[1], "android1234.45&234")

def main():
  unittest.main()

if __name__=="__main__":
  main()
