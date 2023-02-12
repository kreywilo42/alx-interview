#!/usr/bin/python3
"""Log Parsing: reads stdin line by line and computes metrics"""
import sys


lines = sys.stdin.readlines()
fileSize = 0
statusCodes = {}

if len(lines) == 0:
    print('File size: {}'.format(fileSize))
try:
    for count, line in enumerate(lines, start=1):

        words = line.split()
        if not words[-1].isdigit():
            continue
        fileSize += int(words[-1])

        if words[-2].isdigit():
            value = statusCodes.setdefault(words[-2], 0)
            statusCodes[words[-2]] = value + 1

        if count == len(lines) or (count % 10) == 0:
            print("File size: {}".format(fileSize))
            [print('{}: {}'.format(k, v))
             for k, v in sorted(statusCodes.items()) if v != 0]

except KeyboardInterrupt:
    print("File size: {}".format(fileSize))
    [print('{}: {}'.format(k, v))
     for k, v in sorted(statusCodes.items())
     if v != 0]
