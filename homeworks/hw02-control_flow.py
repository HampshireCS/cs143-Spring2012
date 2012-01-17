#!/usr/bin/env python


Section 1:  If Statements
==============================

a = raw_input("Enter a number: ")

1) Get a number from the input, is it even?

2) If it it is not even, double it.

3) If it is divisible by 3, add four.

3) Determine the letter grade value. (eg. 90-100 is A)



Section 2:  Loops
==============================

1)  Get a multiple of three (n) from the input
2)  Print a countdown from n to 0 by threes 
    ex:  
       9...
       6...
       3...
       Done!
3) If it is not a multiple of three, and is even, countdown from n to 0 by twos.


Section 3:  Lists
==============================
nums = [ int(c.strip()) for c in raw_input("Enter a bunch of numbers, separated by commas").strip().split(",") ]


1)  How many numbers were entered?
2)  Append 3 and 5 to nums.
3)  Remove the last element from nums


Section 4:  For Loops
==============================

1) What is the sum of all the numbers in nums?
2) Print "all even" if nums only contains even numbers, otherwise print "not all even" 
3) Multiply each value in nums by its position in the list.


Section 5:  Everything
===============================

1) You have n slices of cake. Ask if they want cake or death. If they choose neither, ask again. When they ask for cake, give them one slice. When there are no slices left, upon choosing cake, ask again. On death, describe their demise.

2) Make an ascii christmas tree (or non-denominational decorate holiday festival shubbery).

Enter the height of the tree: 4
Enter the height of the trunk: 2
   *
   ^
  ^.^
 ^.^.^
^.^.^.^
   |
   | 
