# Python Style

Production code should be performant, easy to maintain, and easy to debug. Coding style and standards are a critical and often overlooked aspect of software development. Incorporating even a few best practices
can induce a ripple effect accross an engineering organization as, collectively, everyone writes and reviews code in a consistent, highly transferable, productive mindset, illimuniated by shared senses of style and arrangement.


#### Style List

In the following list, we document some broad programming concepts to be strongly considered in a consistent and balance team programming style. 

1. Consistent naming conventions (e.g. `my_func` or `MyClass`). This enables developers
to have higher velocity when switching between projects and leads to less bugs.

2. Using mutable default values for function parameters. In Python, default arguments are evaluated once: when the interpreter loads the module where the function is defined. If a default argument is mutable -- for example, an empty list `[]` -- then a single list is allocated and re-used in **all** inocations of the function. 

As an example, this implementation of an `append` to list function is buggy, due to incorrect assumption that default arguments are evaluated on _each_ indivudal function call:
```python
def append(num, num_lst=[]):
	"""Appends the number to the list. Defaults to empty list.
	"""
    num_lst.append(num)
    return num_lst

append(1)  # expected: [1], result: [1]
append(2)  # expected: [2], result: [1, 2]
append(3)  # expected: [3], result: [1, 2, 3] 
```

As indicated by the docstring, we wanted the case where calling `append(1)` meant "append 1 to the empty list." Instead, we have "append 1 to the global list." To fix this behavior, we need to re-interpret the parameter as either (a) "use this current list value" or (b) "create an empty list and use it." We apply a simple fix: use `None` and apply the `Optional` pattern:
```python
def append(num, num_list: Optional[List[int]] = None):
	if num_list is None:
		num_list = []
	num_lst.append(num)
    return num_lst
```

Here, `None` refers to the case where we want the `append` function to allocate a fresh `[]`. Otherwise, we have a specific `List` where we may append our value.



#### References

There are tons of wonderful, thorough style guides on Python. Here we call-out a few specific ones that we think are effective:

- The [Google Python Style Guide](http://google.github.io/styleguide/pyguide.html) is
a reference that includes an exhaustive list of python best practices that can be used
to improve the quality of production code.
