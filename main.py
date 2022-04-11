funcs = set()

def add_route(path):
    return lambda func: funcs.add((func, path))

@add_route('/foo')
def example():
    print("bar")

print(funcs)
