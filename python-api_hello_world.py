#!/usr/bin/env python

from wolframclient.evaluation import WolframLanguage



# Connect to Wolfram Kernel

wl = WolframLanguageSession()



# Evaluate a simple Wolfram expression

result = wl.evaluate("2 + 2")

print(result)  # Output: 4



# Calculate a definite integral using Wolfram's Integrate function

integral_result = wl.evaluate("Integrate[x^2, {x, 0, 1}]")

print(integral_result)  # Output: 1/3
