#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2014
# Glenn P. Downing
# ---------------------------

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
    numRange = range_gen(i, j)
    
    # endpt = max(i, j)
    for a in numRange:
        cycleCheck = collatz_help(a, 1)
        if cycleCheck > max_cycle_length:
            max_cycle_length = cycleCheck
        
        
    # <your code>
    v = max_cycle_length
    assert(v > 0)
    return v

# Array-defining Helper

def range_gen (num1, num2):
    numRange = []
    firstNum = num1
    if (num1 < num2):
        while (firstNum <= num2):
            numRange.append(int(firstNum))
            firstNum += 1
    
    else:
        while (firstNum >= num2):
            numRange.append(int(firstNum))
            firstNum -= 1
    
    return numRange


# Below is a helper method for collatz_eval


def collatz_help (num, length):
    if num == 1:
        return length

    elif (num % 2 != 0):
        length += 1
        num = int( ( 3*num ) + 1 )
        length += 1
        num = int(num / 2)
        # Odd numbers go through operations, hence the extra increment
        return collatz_help (num, length)

    else:
        length += 1
        num = int(num / 2)
        return collatz_help (num, length)


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
def main():
    var1 = ""
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
    cycle5 = collatz_eval (5, 10)
    print(cycle5)
    cycle6 = collatz_eval (1000, 900)
    print(cycle6)
    cycle7 = collatz_eval (10, 5)
    print(cycle7)
    cycle8 = (collatz_eval(4, 4))
    print(cycle8)

# Tester!    
main()