#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wap
import ambientMethods

server = 'http://api.wolframalpha.com/v2/query.jsp'
appid = '26GLXH-Y5WJW8A96R'
arr = [-1,3,-3]
equation = ambientMethods.createEquation(arr)
input = ambientMethods.displayInput(equation)
# print 'Equation String: ' + equation
# print 'Actual Input: ' + input

answer = ambientMethods.displaySolution(input)
print 'RECOMMENDED AMBIENT TEMPERATURE CHANGE: ' + answer