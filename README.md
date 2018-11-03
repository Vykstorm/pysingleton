# pysingleton
This is a very basic implementation of singleton pattern in python using decorators feature.
This was an original idea of Chih-Chung Chang and I extracted it from this web page: https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html


With the code in the script singleton.py, you can mark a class as a singleton easily like this:

```
from singleton import singleton

@singleton
class Foo:
  pass
```
