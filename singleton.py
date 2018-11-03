
'''
This script shows an easy way to implement singleton pattern using decorators python feature.
Extracted from: https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html
Original idea by Chih-Chung Chang modifified by Vykstorm
'''

from inspect import isclass

class Singleton:
    def __init__(self, cls, *args, **kwargs):
        self.cls = cls
        self.instance = None
        self.args = args
        self.kwargs = kwargs

    def __call__(self):
        if self.instance is None:
            self.instance = self.cls(*self.args, **self.kwargs)
        return self.instance

def singleton(*args, **kwargs):
    if len(args) == 1 and len(kwargs) == 0:
        cls = args[0]
        if not isclass(cls):
            raise TypeError('Expected class at argument 1, got {}'.format(type(cls).__name__))
        return Singleton(cls)

    if len(args) > 0:
        raise ValueError('Invalid decorator syntax. It must be: @singleton, @singleton() or @singleton([args = (...)], [kwargs = {...}])')

    if len(kwargs) == 0 or any([kwarg not in ('args', 'kwargs') for kwarg in kwargs]):
        invalid_args = [kwarg for kwarg in kwargs if kwarg not in ('args', 'kwargs')]
        raise TypeError('Unexpected decorator argument{}: "{}"'.format(
            's' if len(invalid_args) > 1 else '', ', '.join(invalid_args)))

    _args = tuple(kwargs['args']) if 'args' in kwargs else ()
    _kwargs = dict(kwargs['kwargs']) if 'kwargs' in kwargs else {}

    def _singleton(cls):
        return Singleton(cls, *_args, **_kwargs)
    return _singleton


if __name__ == '__main__':
    '''
    This example illustrates the usage of singleton decorator
    '''
    @singleton(kwargs = {'limit': 900})
    class PerfectSquares:
        def __init__(self, limit=577):
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

