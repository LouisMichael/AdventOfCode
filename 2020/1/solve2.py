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
            for num3 in input:
                if (num1 + num2 + num3 == 2020):
                    print('The three numbers are: ' + str(num1) + ' , ' + str(num2) + ' and ' + str(num3) + ' multiplied they are ' + str(num1 *  num2 * num3))
parser = argparse.ArgumentParser(description='Advent of code day one')

parser.add_argument('--input-file','-i', type=str, help='what file would you like to use as input?', required=True,
  dest='inputFile')

args = parser.parse_args()
# Here we go!
main(args.inputFile)