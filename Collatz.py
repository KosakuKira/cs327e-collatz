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
    assert i < j
    
    for a in range(i, j + 1):
        cycleCheck = collatz_help(a, 1)
        if cycleCheck > max_cycle_length:
            max_cycle_length = cycleCheck
        
        
    # <your code>
    v = max_cycle_length
    assert(v > 0)
    return v

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
        return collatz_helper (num, length)

    else:
        length += 1
        num = int(num / 2)
        return collatz_helper (num, length)


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

def main():
    print (collatz_help(9, 1))
    print (collatz_eval(1, 2))

main()