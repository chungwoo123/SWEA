def queue_init(self):
    self.queue = []

def queue_empty(self):
    return not self.queue

def queue_enqueue(self, item):
    self.queue.append(item)

def queue_dequeue(self):
    if queue_empty(self):
        return None
    return self.queue.pop(0)

def queue_size(self):
    return len(self.queue)

def queue_peek(self):
    if queue_empty(self):
        return None
    return self.queue[0]