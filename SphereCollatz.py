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
    # assert i <= j
    
    # Set the range of numbers
    
    mclArray = []
    # endpt = max(i, j)
    
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
            
            #if cycleCheck > max_cycle_length:
             #   max_cycle_length = cycleCheck
        
        
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

# Testing individual methods
# def main():
  #  var1 = ""
    # range_gen tests
    #arr1 = range_gen(5, 10)
    #print (arr1)
    #arr2 = range_gen(10, 1)
    #print (arr2)
    #arr3 = range_gen(1, 1)
    #print (arr3)
    #arr4 = range_gen(4, 4)
    #print (arr4)
    
    # Collatz_eval tests
#    cycle1 = collatz_eval(666, 777)
#    print (cycle1)
#    cycle2 = collatz_eval(420, 666)
#    print (cycle2)
#    cycle3 = collatz_eval(69, 420)
#    print (cycle3)
    #cycle4 = collatz_eval(1000, 900)
    #print (cycle4)
   # cycle5 = collatz_eval (5, 10)
    #print(cycle5)
    #cycle6 = collatz_eval (1000, 900)
    #print(cycle6)
    #cycle7 = collatz_eval (10, 5)
    #print(cycle7)
    #cycle8 = (collatz_eval(4, 4))
    #print(cycle8)

collatz_solve(sys.stdin, sys.stdout)
# Tester!    
#main()