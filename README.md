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
