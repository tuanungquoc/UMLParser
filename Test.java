class Person {
        String Name;
}

class Employee extends Person {}

class Client extends Person {}



def walk_dict(item):
    for k, v in item:
        if isinstance(v, str) or isinstance(v, int) or isinstance(v, float):
            path.append(k)
            print
            "{}={}".format(".".join(path), v)
            path.pop()
        elif v is None:
            path.append(k)
            ## do something special
            path.pop()
        elif isinstance(v, dict):
            path.append(k)
            walk(v)
            path.pop()
        else:
            print
            "###Type {} not recognized: {}.{}={}".format(type(v), ".".join(path), k, v)

def walk(d):
    global path
    print(type(d))
    if isinstance(d, plyj.CompilationUnit):
        for item in d:
            if isinstance(item, list):
                print("Dict")
            else:
                walk_dict(item)



def objwalk(obj, path=(), memo=None):
    if memo is None:
        memo = set()
    iterator = None
    if isinstance(obj, Mapping):
        iterator = iteritems
    elif isinstance(obj, (Sequence, Set)) and not isinstance(obj, string_types):
        iterator = enumerate
    if iterator:
        if id(obj) not in memo:
            memo.add(id(obj))
            for path_component, value in iterator(obj):
                for result in objwalk(value, path + (path_component,), memo):
                    yield result
            memo.remove(id(obj))
    else:
        yield path, obj