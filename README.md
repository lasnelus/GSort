#  Gsort Algorithm

**Gsort** is a humorous and intentionally broken sorting algorithm inspired by the "Stalin Sort" — a joke algorithm where any data that doesn't fit the desired order is simply discarded.

---

##  What Is This?

Gsort is based on a sarcastic interpretation of sorting:  
> *"I stop reading after the first error."* — A math teacher at USMB, France

This algorithm walks through a list and stops the moment a number fails to be smaller than the previous. It then returns only the part of the list that was "in line".

---

##  How It Works

- Start from the first element in the list.
- Compare each number to the next one using a comparison function.
- If the next number is smaller, continue.
- If it's equal to or larger, **stop immediately** and return what you've seen so far.

---

##  Functions

### `is_bigger_than(a: float, b: float) -> bool`

Returns `True` if `b` is greater than `a`.  
This is the comparison logic Gsort uses.

### `Gsort(list: list) -> list`

Implements the Gsort algorithm:

- Iterates over the list.
- Keeps numbers only as long as the next is **greater**.
- As soon as one number decrease, the function stops and returns what it has.

---

##  Example

```python
from gsort import Gsort

Gsort([9, 8, 7, 10, 5, 1])
# Output: [9]

Gsort([3, 4, 5, 2, 1])
# Output: [3, 4, 5]
```

---

## Do Not Use This Seriously

This is not a real sorting algorithm. It’s a parody of poor logic and overly strict systems. It doesn't preserve data, order, or sanity.

## Use Cases

- Teaching what not to do in algorithms.

- Making fun of bad logic in code reviews.

- Gag presentations at developer meetups.

- Trolling your colleagues with "new" sorting ideas.

## License

WTFPL – Do What the F*ck You Want to Public License.

## Author

Crafted with Python and sarcasm by someone who enjoys algorithm humor.
[@lasnelus](https://github.com/lasnelus)