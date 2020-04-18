#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Answer: 0(n)

```

- The time complexity is 0(n) because (a) grows in proportion to n as long as (a) is less than n^3.

```

b) 0(log n)
In this case, the first for loop says as long as the index is in range of n, j stays proportionate at 1. But even though the while loop is nested in the for loop, which would imply a time complexity of n^2, it isn't executing the same operation as it's parent.  Under the while loop, j is growing twice as fast as it's parent.  That would make it 0(log n)
 ```
  sum = 0  1
    for i in range(n)  -n
      j = 1   1
      while j < n:  
        j *= 2    another way to say this is j = j * 2 (statement says as long as )
        sum += 1  -n
```


c) Answer: 0(n)

- Line 26 & 27 are both constants.  However line 28 bunnyEars increase with the amount of bunnies which is n.  This leads to 0(2 + n), simplified, 0(n)

## Exercise II
Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

```

The answer is to complete a binary search through the building.

 In researching the proper strategy to determine the value of f. First I realized that n-story building had no bearing on whether or not the eggs get broken. We are simply searching for which floor would cause the eggs to break.  Now normally we would go through each floor and drop an egg to see if it breaks.  That would take way too much time.  However, if we did a binary search through the building, we could eliminate searching through half of the building that would likely break the egg.  If we go halfway, and the egg doesn't break, we can eliminate the bottom half as we know the bottom half wouldn't cause breakage.  Then we go to the midpoint of the upper half of the building and if the egg breaks there, then we know the right floor is no higher than the midpoint here. So that eliminates having to complete the search through the rest of the floors in the top level of the building.  This process is to be repeated until there are no more options for (f)

 The algorithm in this case would be 
 Example: 
 Suppose n = 10
 f= [ 1,2,3,4,5,6,7,8,9,10]

We start at floor 5 // The egg doesn't break
- This eliminates the bottom 4 floors.

Now we have
f= [6,7,8,9,10]
Start at floor 8// The egg breaks
- Now we know the starting point of where the eggs break.  If f > 8, the eggs will break

But to make certain that is the right floor, we now only have to test 2 floors which is 6 & 7.

The time complexity here would be 0(log n)
 
```








