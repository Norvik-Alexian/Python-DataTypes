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
as it is used in function. Each control return can be organizzed with next()