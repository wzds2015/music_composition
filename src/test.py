#! /usr/bin/env python

import numpy as np

a = np.arange(35)
b = np.arange(105, 105+34)
print np.argmax(a, axis=0) 
