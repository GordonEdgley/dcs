# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 23:53:19 2021

@author: fatih
"""
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O 
file=pd.read_csv("ML Sample Data.csv",delimiter=";",error_bad_lines=False)

x = file.values #returns a numpy array