import inspect


### inspect signature:
def add(a, b, c=1):
    """Add a, b, c"""
    return a + b + c

sig = inspect.signature(example)
print(sig)  # 输出: (a, b, c=1)


### Get docstring
doc_string = inspect.getdoc(example)
print(doc_string)  # 输出: "Add a, b, c"


