#!/usr/bin/env python

import argparse
import os

def main(inputFilePath):
    input = []
    with open(inputFilePath, 'r') as inputFile:
        for line in inputFile:
            input.append(int(line))
    for i in range(len(input)):
        num1 = input.pop()
        for num2 in input:
            if (num1 + num2 == 2020):
                print('The two numbers are: ' + str(num1) + ' and ' + str(num2) + ' multiplied they are ' + str(num1 *  num2))
parser = argparse.ArgumentParser(description='Advent of code day one')

parser.add_argument('--input-file','-i', type=str, help='what file would you like to use as input?', required=True,
  dest='inputFile')

args = parser.parse_args()
# Here we go!
main(args.inputFile)