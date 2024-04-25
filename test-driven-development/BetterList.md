# BetterList
* a class which extends the built-in list class and
  * ...overrides the following methods
    * __`.append()`__: should allow you to append an _iterable_, but act like __`.extend()`__ (that is, each item in the iterable should be added individually)
      * e.g., if __`mylist = [1, 2, 3]`__, then __`mylist.append([4, 5, 6])`__ should yield __`[1, 2, 3, 4, 5, 6]`__
    * __`.insert()`__: similar to above, you should be able to __`.insert()`__ a list at a given index and the items in the list should be inserted one at a time
      * e.g., if __`mylist = [1, 2, 3, 4]`__ then __`mylist.insert([5, 6])`__ should yield __`[1, 2, 5, 6, 3, 4]`__
  * ...and _adds_ the following methods:
    * __`.discard(item)`__: acts like __`list.remove(item)`__, but if the item to be removed isn't in the list it just returns
    * __`.removeall(item, limit=None)`__: removes all instances of item, rather than just the first one. If the limit argument is an int, then it represents the upper limit on the number of removals
    *  * e.g., __`[1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4].removeall(3, 3)`__ would remove the first three 3s, but none of the rest

  
