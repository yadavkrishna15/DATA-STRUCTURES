import heapq

# ---------------------------
# Part 1: AVL Tree Logic
# ---------------------------

class AVLNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

class AVLTree:
    def __init__(self, log_callback=None):
        self.log = log_callback or (lambda msg, tag="WHITE": print(msg))

    def insert(self, root, key):
        if not root:
            return AVLNode(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        # Left Heavy
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)
        # Right Heavy
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)
        # Left-Right Case
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        # Right-Left Case
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        self.log(f"  ↪ Left Rotation on Node {z.key}", "YELLOW")
        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        self.log(f"  ↪ Right Rotation on Node {z.key}", "YELLOW")
        return y

    def get_height(self, root):
        return root.height if root else 0

    def get_balance(self, root):
        return self.get_height(root.left) - self.get_height(root.right) if root else 0

    def pre_order(self, root, result=None):
        if result is None:
            result = []
        if root:
            result.append(str(root.key))
            self.pre_order(root.left, result)
            self.pre_order(root.right, result)
        return result

# ---------------------------
# Part 2: Heap Helpers
# ---------------------------

def process_min_heap(data_list):
    min_h = data_list.copy()
    heapq.heapify(min_h)
    return min_h

def process_max_heap(data_list):
    max_h = [-x for x in data_list]
    heapq.heapify(max_h)
    return [-x for x in max_h]

# ---------------------------
# Part 3: Task Manager Class
# ---------------------------

class TaskManager:
    def __init__(self):
        self.pq = []

    def add_task(self, priority, description):
        heapq.heappush(self.pq, (priority, description))

    def get_next_task(self):
        if self.pq:
            return heapq.heappop(self.pq)
        return None
