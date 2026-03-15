# TeleportSort
TeleportSort is a horrible and inefficient sorting algorithm. 

It works by repeatedly selecting a random element and "teleporting" it to a random position in the list. Eventually, through pure luck, the list may accidentally become sorted.

Occasionally an element is teleported to exactly the same position it already occupied. This contributes nothing to the sorting process but increases the iteration count, which helps maintain the algorithm's terrible performance characteristics.

## Time Complexity
Best case: `O(n)`

The list is already sorted, or a single misplaced element is teleported to the correct position on the first attempt.

Average case: `O(???)`

Who knows, but probably somewhere between terrible and catastrophic. The number of operations grow rapidly as the list size increases.

Worst case: `O(∞)`

Alright, you're not getting this list sorted buddy.

## Usage
Run the demo program and specify the length of the random list.

Example:
```
python3 teleport_sort_demo.py -n 10
```
This generates a random list with 10 elements and attempts to sort it using TeleportSort.  
Be aware that larger lists may run for a very long time.

### Example Output
```
python3 teleport_sort_demo.py -n 10
Initial list: [0, 25, 10, 23, 29, 20, 14, 19, 6, 8]
Sorted list: [0, 6, 8, 10, 14, 19, 20, 23, 25, 29]
It took 2.918 seconds to TeleportSort this list.
Elements were teleported 3 551 808 times.
```