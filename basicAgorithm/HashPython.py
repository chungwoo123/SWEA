def hash_init(self):
    self.size = 11
    self.slots = [None] * self.size
    self.data = [None] * self.size

def hash_function(self,key):
    return hash(key) % self.size

def hash_put(self,key,data):
    hashvalue = self.hash_function(key)
    if self.slots[hashvalue] == None:
        self.slots[hashvalue] = key
        self.data[hashvalue] = data
    else:
        if self.slots[hashvalue] == key:
            self.data[hashvalue] = data
        else:
            nextslot = self.rehash(hashvalue)
            while self.slots[nextslot] != None and self.slots[nextslot] != key:
                nextslot = self.rehash(nextslot)
            if self.slots[nextslot] == None:
                self.slots[nextslot] = key
                self.data[nextslot] = data
            else:
                self.data[nextslot] = data

def hash_get(self,key):
    hashvalue = self.hash_function(key)
    data = None
    stop = False
    while self.slots[hashvalue] != None and not stop:
        if self.slots[hashvalue] == key:
            data = self.data[hashvalue]
            stop = True
        else:
            hashvalue = self.rehash(hashvalue)
    return data

def rehash(self,oldhash):
    return (oldhash+1) % self.size

    
def hash_del(self,key):
    hashvalue = self.hash_function(key)
    if self.slots[hashvalue] == None:
        return None
    else:
        stop = False
        while self.slots[hashvalue] != None and not stop:
            if self.slots[hashvalue] == key:
                self.slots[hashvalue] = None
                self.data[hashvalue] = None
                stop = True
            else:
                hashvalue = self.rehash(hashvalue)
        return None

def hash_size(self):
    return self.size

def hash_data(self):
    return self.data

def hash_slots(self):
    return self.slots