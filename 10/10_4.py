class HashTable:
    def __init__(self, max_size=128):
        self.data_list = [None] * max_size
    def __setitem__(self, key, value):
        idx = ord(key)
        #print(idx)
        self.data_list[idx] = (key, value)
    def __getitem__(self, key):
        idx = ord(key)
        kv = self.data_list[idx]
        if kv is None:
            return None
        else:
            return kv[1]

person = HashTable()
gift = HashTable()
key,value = input("Enter str1,str2: ").split(",")
for k,v in zip(key,value):
    if person[k] == None and gift[v] == None:
        person[k] = v
        gift[v] = k
    elif person[k] == v and gift[v] == k:
        pass
    else:
        print(f'{key} and {value} are not Isomorphic')
        exit()
print(f'{key} and {value} are Isomorphic')