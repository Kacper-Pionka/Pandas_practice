# -*- coding: utf-8 -*-
import pandas as pd

x = {
    "day" : ['day1','day2','day3','day4'],
    "calories" : [420, 370, 430, 400]
                                        }

myvar = pd.DataFrame(x, index = [i for i in range(1,5)])

print(myvar)
