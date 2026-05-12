import sys

def tree_init(self):
    self.tree = {}

def tree_insert(self, parent, child):
    if parent not in self.tree:
        self.tree[parent] = []
    self.tree[parent].append(child)

def tree_find(self, parent):
    if parent in self.tree:
        return self.tree[parent]
    return None

def tree_delete(self, parent, child):
    if parent in self.tree and child in self.tree[parent]:
        self.tree[parent].remove(child)
    return None

def tree_update(self, parent, child):
    if parent in self.tree and child in self.tree[parent]:
        self.tree[parent][child] = self.tree[parent][child] + 1
    return None

def tree_display(self):
    print(self.tree)

def tree_size(self):
    return len(self.tree)

def tree_clear(self):
    self.tree = {}

def tree_preorder(self, parent):
    if parent in self.tree:
        print(parent)
        for child in self.tree[parent]:
            self.tree_preorder(child)

def tree_inorder(self, parent):
    if parent in self.tree:
        for child in self.tree[parent]:
            self.tree_inorder(child)
        print(parent)

def tree_postorder(self, parent):
    if parent in self.tree:
        for child in self.tree[parent]:
            self.tree_postorder(child)
        print(parent)

def tree_bfs(self, parent):
    if parent in self.tree:
        for child in self.tree[parent]:
            print(child)
        self.tree_bfs(self.tree[parent][0])

def tree_dfs(self, parent):
    if parent in self.tree:
        for child in self.tree[parent]:
            self.tree_dfs(child)
        print(parent)

if __name__ == "__main__":

    tree = []

    tree_init(tree)

    tree_insert(tree, 1, 2)

    tree_insert(tree, 1, 3)

    tree_insert(tree, 2, 4)

    tree_insert(tree, 2, 5)

    tree_insert(tree, 3, 6)

    tree_insert(tree, 3, 7)

    tree_display(tree)

    tree_preorder(tree, 1)
    
    tree_inorder(tree, 1)

    tree_postorder(tree, 1)
    
    tree_bfs(tree, 1)

    tree_dfs(tree, 1)