#!/usr/bin/env python3

# ------------------------------
# projects/collatz/RunCollatz.py
# Copyright (C) 2014
# Glenn P. Downing
# -------------------------------

"""
To run the program
    % python RunCollatz.py < RunCollatz.in > RunCollatz.out
    % chmod ugo+x RunCollatz.py
    % RunCollatz.py < RunCollatz.in > RunCollatz.out

To document the program
    % pydoc -w Collatz
"""

# -------
# imports
# -------

import sys

from Collatz import collatz_solve

# ----
# main
# ----

#def main():
 #   fileNails = open('RunCollatz.txt', 'r')
  #  fileJony = open('RunCollatz.out', 'w')
    
   # for nails in fileNails:
        # nails = str(nails, encoding = 'utf8')
    #    nails = nails.rstrip("\n")
     #   print (nails)
    
    
    #jony = fileJony.read()
    
    
    #fileNails.close()
    #fileJony.close()

collatz_solve('RunCollatz.txt', 'RunCollatz.out')

#main()