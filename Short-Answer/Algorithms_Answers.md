#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Answer: 0(n^3)

- The time complexity is 0(n^3) because on line 10 you have n^3.  On line 11 you have n^2.  The actual result is O(n^3 + n^2).  If you were to simplify this, the final result would be 0(n^3) because when you put n^3 and n^2 together, the worst case would always be 0(n^3).


b) Answer: 0(n)

- In this problem you have 4 operations and 2 constants.  This gives you a time complexity of 0(4n + 2).  Simplified, this would be 0(n).


c) Answer: 0(n)

- Like 26 & 27 are both constants.  However line 28 bunnyEars increase with the amount of bunnies which is n.  This leads to 0(2 + n), smplified, 0(n)

## Exercise II

1. Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. 

```
- Ok so we have x amount of eggs
- What is higher than floor f?  Does higher mean "g", "h", "i"... 

Or

- Could f be a variable? 

- "Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f." --This statement implies a conditional

If x > f return "eggs broken"
elif x < f return "no eggs broken"

- This statement also shows that a loop is needed because we're looping over each floor # (f)

n = How many stories are in the building  -constant because this is not in proportion to the number of eggs broken

f = floor # -n because as the floor number increases, so does the likelihood of eggs getting broken. 

```

2. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

```
- Ok now this part of the instruction states, "...the value of f" Therefore f is a variable.

- Here lies the question:  How do we determine which value of (f) causes eggs to break in an n-story building?  Does the value of f change with the value of n?  --No because in each case, n is constant.

```

3. Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

```
So here's my interpretation of what needs to be done.

A strategy or function needs to be developed to determine the value of f that causes eggs to break

- In reality, the only chance of an egg not breaking is if f=0.  Any higher and the eggs would definitely break. 


def is_eggs_broken(n):
    n = 10
    for f in range(10):
        if f = 0:
            return "eggs not broken"
        elif f > 0:
            return "eggs broken"

    return f


 ```     
 - No matter which way you look at this, any floor number bigger than zero would cause the eggs to break.  The size of the building plays no part in this either.  This problem has a time complexity of 0(1) because no matter what the floor number is after 0, the answer remains constant




