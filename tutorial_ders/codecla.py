import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
for i in range(n):
    name = input()
    print('VALID' if len([k for k in name if k.isupper()]) == len(name) else "INVALID")

    print([k for k in name if k.isupper()])