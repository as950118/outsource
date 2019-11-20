from collections import deque

class Node:
    def __init__(self, item, parent=None, left=None, right=None):  # 노드 생성자
        self._item = item
        self._parent = parent
        self._left = left
        self._right = right

    @property
    def item(self):
        return self._item

    @property
    def parent(self):
        return self._parent
    @parent.setter
    def parent(self, new_parent):
        self._parent = new_parent

    @property
    def left(self):
        return self._left
    @left.setter
    def left(self, new_left):
        self._left = new_left

    @property
    def right(self):
        return self._right
    @right.setter
    def right(self, new_right):
        self._right = new_right

    @property
    def is_leaf(self):
        return self.left == None and self.right == None

class BinaryTree:
    def __init__(self):  # 트리 생성자
        self.root = None

    def insert_node(self, new_node : Node):
        if self.root == None:
            self.root = new_node
            return self.root

        cur_node = self.root
        while cur_node:
            prv_node = cur_node
            if cur_node.data > new_node.item:
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right

        new_node.parent = prv_node
        if cur_node == prv_node.left:
            prv_node.left = new_node
        else:
            prv_node.right = new_node

    def preorder(self, n):  # 전위순회
        if n == None:
            return n
        #배열을 이용한 방식
        arr = list()
        ret = list()
        arr.append(n)
        while arr:
            cur = arr.pop()
            ret.append(cur.item)
            # 오른쪽을 먼저 넣어주는 이유는 배열에서 나중에 들어간 값을 먼저 탐색하기 때문이다.
            # 즉, 왼쪽을 먼저 탐색하기 위해 오른쪽을 먼저 넣어준다.
            if cur.right:
                arr.append(cur.right)
            if cur.left:
                arr.append(cur.left)
        #출력
        for elem in ret:
            print(elem, end="  ")
        #반환
        return ret

    def inorder(self, n):  # 중위순회
        if n == None:
            return n

        #배열을 이용한 방식
        arr = list()
        ret = list()
        cur = n
        while cur or arr:
            # 왼쪽 자식이 없을때까지 반복한다.
            while cur:
                arr.append(cur)
                cur = cur.left
            # 왼쪽자식이 없는 노드에 도착하면
            # 현재 값을 탐색하고
            # 오른쪽 노드를 탐색한다
            # 만약에 여기서도 오른쪽 노드가 없다면
            # 아까 탐색하지 못한 부모 노드를 탐색하게 될 것이다.
            cur = arr.pop()
            ret.append(cur.item)
            cur = cur.right

        #출력
        for elem in ret:
            print(elem, end="  ")
        #반환
        return ret

    def postorder(self, n):  # 후위순회
        if n == None:
            return n

        #배열을 이용한 방식
        arr = list()
        ret = list()
        cur = n
        while 1:
            # cur를 2번 append 해주는 것은
            # 왼쪽 서브트리와 시작 노드로 나누기 위해서이다.
            while cur:
                arr.append(cur)
                arr.append(cur)
                cur = cur.left
            # 더 이상 탐색할 서브트리가 없다면 종료한다
            if not arr:
                break
            cur = arr.pop()
            # 남아있는 노드가 있고, 현재 노드가 시작 노드라면
            # 오른쪽 서브트리를 탐색 시작한다.
            if arr and arr[-1] == cur:
                cur = cur.right
            # 둘 중에 하나라도 없다면
            # 더 이상 탐색할 것이 없다는 것이므로
            # 시작 노드를 추가하고 종료한다.
            else:
                ret.append(cur.item)
                cur = None
        #출력
        for elem in ret:
            print(elem, end="  ")
        #반환
        return ret

    def levelorder(self, root):  # 레벨순회
        q = []
        q.append(root)
        while len(q) != 0:
            t = q.pop(0)
            print(str(t.item), ' ', end='')
            if t.left != None:
                q.append(t.left)
            if t.right != None:
                q.append(t.right)

    def height(self, root):  # 트리 높이 계산
        if root == None:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1

    def size(self, root):  # 트리 노드 수 계산
        if root is None:
            return 0
        else:
            return 1 + self.size(root.left) + self.size(root.right)

    def copy_tree(self, n):  # 트리 복제
        if n == None:
            return None
        else:
            left = self.copy_tree(n.left)
            right = self.copy_tree(n.right)
            return self.Node(n.item, left, right)

    def is_equal(self, n, m):  # 두 트리의 동일성 검사
        if n == None or m == None:
            return n == m
        if n.item != m.item:
            return False
        return (self.is_equal(n.left, m.left) and
                self.is_equal(n.right, m.right))

