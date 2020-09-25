# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 21:53:56 2020

@author: Binary Beast
"""
import numpy as np
def gradient_descent(x,y):
    m_curr = b_curr = 0
    learning_rate = 0.08
    num_of_iterations = 10000
    n = len(x)
    
    for i in range(num_of_iterations):
        y_prediction = m_curr*x + b_curr
        cost = (1/n)*sum([val**2 for val in (y-y_prediction)])
        md = -(2/n)*sum(x*(y-y_prediction))
        bd = -(2/n)*sum(y-y_prediction)
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd
        print("m {}, b {}, cost {}, iteration {}".format(m_curr, b_curr, cost, i))
        
x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])
gradient_descent(x,y)