#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
   Life's short, Python more.   
   bug report to guoxin_min@126.com.
"""

import os
import sys
import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("result_path", help="where to save the result")
parser.add_argument("column_num", help="how many column U want", type=int)
parser.add_argument("row_num", help="how many row U want", type=int)
parser.add_argument("up_bound", help="maxiumn value", type=int)

def generate_one (up_bound): 
    random.seed()
    num1 = random.randint(0, up_bound)
    num2 = random.randint(0, up_bound)
    op = ' + ' if random.random() > 0.5 else ' - '
    if op == ' - ' and num1 < num2 :
        num1,num2 = num2,num1
    if op == ' + ' and num1 + num2 > up_bound:
        return generate_one(up_bound)
    return str(num1) + op + str(num2) + ' = '

def generate_many(up_bound, num):
    result = []
    for i in range(0,num):
        result.append(generate_one(up_bound))
    random.seed()
    random.shuffle(result)
    return result

def generate_format(result_path, column_num, row_num, up_bound):
    f = open(result_path, 'w')
    num = column_num * row_num
    calcs = generate_many(up_bound, num)
    for i in range(0, row_num):
        tmp = calcs[0 + i*column_num:column_num + i*column_num]
        line = ','.join(tmp)
        print >> f, '%s' %(line)

def main():
    args = parser.parse_args()
    print args    
    generate_format(args.result_path, args.column_num, args.row_num, args.up_bound)

if __name__ == '__main__':
    main()
    
