def myfunc():
    x = 3
    class MyClass(object):
        x = x
    return MyClass

myfunc().x