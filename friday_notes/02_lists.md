Advanced Lists
===================

Indexing
--------------------
 * positive
     * [0], [5]
 * negative
     * [-2], [-1]
 * copying
     * [:]
     * wha...?
 * slicing
     * [1:] all but first
     * [-3:] last 3
     * [:-3] all but the last 3
     * [:3] first 3
     * [1:-1] all but first and last
     * copying is just a slice with everything
 * step
     * [::]...works too...
     * thrid number is step
     * [::2] = even numbers
 * negative step
     * [::-1] is a reversed list
     * [10::-1] is 10-0
     * [10:0:-1] is 10-1
 * sometimes there are cleaner ways to write it
     * range(30)[::-1] is a reversed range
     * reversed(range(30)) is the same thing

Chaining Slices
----------------------
 * can chain one after another
 * let's say you want every multiple of 4
     * range(100)[::4]
     * includes 0...
     * range(100)[::4][1:]

List Comprehensions
--------------------------
More complicated problems
  * square every number in a list
     `[ x**2 for x in range(30) ]`
  * rename files
     `[ n.replace(" ", "_") for s in os.listdir(".")`
  * multiple numbers
     `[int(n) for n in raw_input("Enter comma separated numbers: ").split(",") ]`

Can also be used to filter
 * only keep the numbers less than 10
   `[ x for x in ll if x<10 ]`
 * Keep names that contain a partial string
   **NOTE: build in class example around this...**
   `[ person for person in people if person.name.lower().find("ste") ]`

can be used to create combinations of things
 * find every combination of two numbers between 1-10
   `[x,y for x in range(1,11) for y in range(1,11)]`
 * find every combination with a unique draw
   `[ (x,y) 
      for x in range(1,11)
      for y in range(1,11)
      if x != y ]`
 * every possible dice roll for two dice
   `[ (x+1, y+1)
      for x in range(6)
      for y in range(6)
      if x <= y ]
    rolls = [ [a+b, [a,b]] for a,b in dice ]`

 * combs = [ [] for _ in range(13) ]
   `[ combs[k].append(v) for k,v in rolls ]`

 * pythagorean triples
   `[ (x,y,z) 
     for x in range(1,31)
     for y in range(x,31)
     for z in range(y,31)
     if x**2 + y**2 == z**2 ]`

problems: 
 * not the most readable things in the world but they are better than some other languages
 * 

Using with all, any, sum, or any other function which takes iterators/lists
  * you can leave out the square brackets
   `any(x < 3 for x in range(10))`
   `all(x < 3 for x in range(10))`

