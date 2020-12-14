# MU
Python implementation of the brilliant "MU" game by Douglas R. Hofstadter
All credits for this idea goes to Douglas R. Hofstadter and his beautiful book "Gödel, Escher, Bach: an Eternal Golden Braid" (buy it!)
This is just an implementation of the idea.

# Prerequisites
NumPy

Also uses modules:
sys
csv
re

# Usage

Goal: Starting from MI, find MU!

Run the code, then choose which law to apply ('1','2','3','4').
Laws 3 and 4 can have ambiguity if they can be applied to more than one sequence of the string.
To overcome this, also specify to which occurrence you want to apply the law.

E.g.
MUIIIUUIIIIUU
'32'
MUIIIUUUU
'41'
MUIIIU
...

Type 'h' for a reminder on the laws, should you forget them!
Type 'q' to quit the program and output a csv file with your chain of laws and strings found!

