def stack_init(self):
    self.stack=[]

def stack_empty(self):
    return not self.stack

def stack_push(self,item):
    self.stack.append(item)

def stack_pop(self):
    if stack_empty(self):
        return None
    return self.stack.pop()

def stack_peek(self):
    if stack_empty(self):
        return None
    return self.stack[-1]

def stack_size(self):
    return len(self.stack)
