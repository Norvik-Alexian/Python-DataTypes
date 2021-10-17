# Summarization

## Tuple:
Tuple is immutable sequence of objects, and it's unmodifiable (immutable) list.
if tuple contains only one element we should place comma after it.

tuple.index(object) - find first object occurance.

tuple.count(object) - occurance number of object in tuple.

Object from list can be mutable.

## Sets:
Set is unordered collection of unique unmodifiable (immutable) object.
Set can also be created from other object using `set()` function.

Set support different operations unique for sets:
* x & y - intersection
* x | y - unite
* x - y - subtraction

Set can be considered as dictionary without values (only with keys).

We can add element to set or to remove an element, we can iterat over set and sets support comprehension expression.
We can create subsets using frozenset.

## Iterations:
Iteration is a step in the process of taking something item by item.

## Python Iterables:
An iterable is any Python object capable of returning its members one at a time, permitting it to be iterated over a for-loop.

Python Iterable object has __iter__ method which returns iterator.

List, Tuple, Strings are Iterable

Iterables can have __getitem__, method which allows getting item by index or key(set doesn't have that method)

Python iterator is object that has __next__ method which is used to get next item for iteration (automatically called in for).
We can also use next() function on Iterator objects.

StopIteration exception is generated if we try to call next on last item.

Not all iterable objects Iterators, for example list doesn't have __next__ method.

## For Details:
Python FOR first retrieves iterator of object, then uses __next__ assigning its value to FOR variable until StopIteration
exception is happening.

## Unpacking Iterables
Sometimes we should copy the items of iterable object into separate identifiers. Often this feature is also used in loops.

## Enumerating Iterables:
Enumerate(iterable) function allows iterating over iterable tracking iteration number (generates a new iterable each item 
of which is tuple containing iteration number and item from original iterable.)

## Generators:
Generator is an iterator that you can only iterate once.
Generator don't save values in memory they generate values on fly forgetting about previous value.

Generators can be declared using () with the comprehension expression style. Generator is inherited from iterator.

## Next() with generators:
next() function (uses iterator __next__) can be used with generators to move to next item.

## Generator Functions:
Generator function is a function that returns generator. It uses yield keyword for each item return.
Return operator return the control once to the calling part.
Yield operator returns the control multiple times. It can return control as many times. It can return control as many time
as it is used in function. Each control return can be organizzed with next().

## Generators vs Iterables:
Generators don't store all the values in memory. They generate an item on fly. Each time we use next() item is generated
and previous one is forgotten. Thus, Generator doesn't support len() function, doesn't have index access, but are memory 
efficient.

### When to use Generator:
Use if we work with big data sequences, that we don't know if we will need them all.
Generator can provide first results faster than classic function. Yield allows building interrupted functions.

## The range() function:
We can generate a sequence of numbers using range() function. We can also define the start, stop, and step as range(start, stop, step).
Step size defaults to 1 if not provided.

## range() object:
range() in Python 3 is creating a smart range type object that is like list, but is more memory efficient.

Sys.getsizeof() can sometimes be used to get object memory consumption.

## Break and Continue:
The break statement terminates the loop containing it.

The continue statement is used to skip the rest of the code inside a loop for the current iteration only.

## For loop with else:
A for loop can have an optional else block as well the else part is executed if the items in the sequence used in for loop
exhausts.
For loop's else part runs if no break occurs.

## While loop with else:
The else part is executed if the condition in the while loop evaluates to False. The while loop can be terminated with break
statement. In such case, the else part if ignored. Hence, a while loop's else part runs if no break occurs and the condition 
is False.