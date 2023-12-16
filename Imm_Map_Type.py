from  collections.abc import Mapping
class ImmMap(Mapping):
    def __init__(self, *args, **kwargs):
        self._data = dict(*args, **kwargs)
    def __len__(self):
        return len(self._data)
    def __iter__(self):
        return iter(self._data)
    def __contains__(self, key):
        if key in self._data:
            return True
        else:
            False
    def __getitem__(self, key):
        return self._data[key]
    def __repr__(self):
        return f"Immutble Mapping Type : ({repr(self._data)})"
    def values(self):
        return self._data.values()
    def keys(self):
        return self._data.keys()
    def items(self):
        return self._data.items()
    def __setitem__(self, *args, **kwargs):
        raise TypeError("Immutable Mapping Type")
    def __delitem__(self, *args):
        raise TypeError("Immutable Mapping Type")


if __name__=="__main__":
    dic={"k": 2,"c":123,"d":"wal"}
    map=ImmMap(dic)
    print(len(map))
    print(map['c'])
    for key in map:
        print(key)
    print("x" in map)
    print("k" in map)
    print(repr(map))
    print(map.values())
    print(map.keys())
    print(map.items())
    try:
        map['c'] = 11
    except TypeError as e:
        print(e)
    try:
        del map['c']
    except TypeError as e:
        print(e)