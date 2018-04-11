#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 11:37:18 2018

@author: kathy
"""

import numpy as np
from scipy.io import loadmat
import matplotlib.pyplot as plt

def load():
    """
    load the data
    """
    load_data = loadmat('spam_data.mat')
    test_x, test_y = load_data['test_x'], load_data['test_y']
    train_x, train_y = load_data['train_x'], load_data['train_y']
    
    return test_x, test_y, train_x, train_y
    
if __name__ == '__main__':
    # loading data
    test_x, test_y, train_x, train_y = load()
