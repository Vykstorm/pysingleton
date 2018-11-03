# pysingleton
This is a very basic implementation of singleton pattern in python using decorators feature.
This was an original idea of Chih-Chung Chang and I extracted it from this web page: https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html


With the code in the script singleton.py, you can mark a class as a singleton easily like this:

```python
from singleton import singleton

@singleton
class Foo:
  pass

A,B = Foo(), Foo()
print(A is B)

```
```
True
```

In the example, either A and B refers to the same object that is an instance of the class Foo
If you want to pass arguments to the constructor of Foo, you can do it by adding decorator arguments...

```python

@singleton(args = [1, 2, 3])
class Foo:
  def __init__(a, b, c):
    print('calling Foo __init__')
    self.value = a + b + c
    
A,B = Foo(), Foo()
print(A.value, B.value)

```
```
calling Foo __init__
6 6
```

args will send positional arguments to the constructor of Foo that is only called once (when singleton is created)
You can also use kwargs to send keyword arguments:

```python

@singleton(args = [1, 2], kwargs = {'c' : 3})
class Foo:
  def __init__(a, b, c):
    print('calling Foo __init__')
    self.value = a * b * c
    
A,B = Foo(), Foo()
print(A.value, B.value)

```
```
calling Foo __init__
6 6
```


The code below is an example of usage.

```python
@singleton(kwargs = {'limit': 900})
class PerfectSquares:
    def __init__(self, limit):
        self.index = 1
        self.current = 1
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            val = self.current
            self.index += 1
            self.current += (self.index << 1) - 1
            return val
        else:
            raise StopIteration()

A = iter(PerfectSquares())
B = iter(PerfectSquares())

print('Perfect square numbers: ')
try:
    while True:
        print('{:4d} {:4d} '.format(next(A), next(B)), end='')
except StopIteration:
    pass
```
```
Perfect square numbers: 
   1    4    9   16   25   36   49   64   81  100  121  144  169  196  225  256  289  324  361  400  441  484  529  576  625  676  729  784 
```
