def node_init(self,item):
    self.item = item
    self.next = None
    
def ordered_list_init(self):
    self.head = None

def ordered_list_search(self, item):
    current = self.head
    position = 0
    found = False
    while current != None and not found:
        if current.item == item:
            found = True
        else:
            current = current.next
            position = position + 1
    if found:
        return position
    else:
        return None
    
def ordered_list_insert(self, item):
    current = self.head
    previous = None
    stop = False
    while current != None and not stop:
        if current.item > item:
            stop = True
        else:
            previous = current
            current = current.next
    temp = node_init(item)
    if previous == None:
        temp.next = self.head
        self.head = temp
    else:
        temp.next = current
        previous.next = temp

def ordered_list_remove(self, item):
    current = self.head
    previous = None
    found = False
    while current != None and not found:
        if current.item == item:
            found = True
        else:
            previous = current
            current = current.next
    if not found:
        raise ValueError
    else:
        if previous == None:
            self.head = current.next
        else:
            previous.next = current.next

def is_ordered(self):
    current = self.head
    while current != None and current.next != None:
        if current.item > current.next.item:
            return False
        current = current.next
    return True

def ordered_list_size(self):
    current = self.head
    count = 0
    while current != None:
        count = count + 1
        current = current.next
    return count