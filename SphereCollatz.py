#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2014
# Glenn P. Downing
# ---------------------------

import sys

# ------------
# collatz_read
# ------------

def collatz_read (r, a) :
    """
    reads two ints into a[0] and a[1]
    r is a  reader
    a is an array of int
    return true if that succeeds, false otherwise
    """
    s = r.readline()
    if s == "" :
        return False
    l = s.split()
    a[0] = int(l[0])
    a[1] = int(l[1])
    return True

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    return the max cycle length in the range [i, j]
    """
    assert(i > 0)
    assert(j > 0)
    max_cycle_length = 0
    newI = i
    newJ = j
    
    if i > j:
        newI = j
        newJ = i
    
    
    k = (newJ >> 1)
    if newI < k:
        newI = k
        
    
    if newI != newJ:
        for a in range(newI, newJ + 1):
            val = collatz_help(a, 1)
            if (val > max_cycle_length):
                max_cycle_length = val
        
    else:
        cycleCheck = collatz_help(newI, 1)
        max_cycle_length = cycleCheck    
        
    # <your code>
    v = max_cycle_length
    assert(v > 0)
    return v



# Below is a helper method for collatz_eval


def collatz_help (num, length):
    assert (num > 0)
    assert (length > 0)
    
    while (num > 1):
        if (num % 2 != 0):
            num = num + (num >> 1) + 1
            length += 2
        else:
            num = (num >> 1)
            length += 1
    
    return length
    

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    prints the values of i, j, and v
    w is a writer
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    v is the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    read, eval, print loop
    r is a reader
    w is a writer
    """
    a = [0, 0]
    while collatz_read(r, a) :
        i, j = a
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)

collatz_solve(sys.stdin, sys.stdout)
