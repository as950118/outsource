class Node:
    def __init__(self, item, left=None, right=None): # 노드 생성자
        self.item  = item 
        self.left  = left 
        self.right = right 

class BinaryTree:
    def __init__(self): # 트리 생성자
        self.root = None 

    def preorder(self, n): # 전위순회
        if n != None:
            print(str(n.item),' ', end='')
            if n.left:
                self.preorder(n.left)
            if n.right:
                self.preorder(n.right)
 
    def inorder(self, n): # 중위순회
        if n != None:
            if n.left:
                self.inorder(n.left)
            print(str(n.item),' ', end='')
            if n.right:
                self.inorder(n.right)

    def postorder(self, n): # 후위순회
        if n != None:
            if n.left:
                self.postorder(n.left)
            if n.right:
                self.postorder(n.right)
            print(str(n.item),' ', end='')
              
    def levelorder(self, root): # 레벨순회
        q = []
        q.append(root)
        while len(q) != 0:  
            t = q.pop(0) 
            print(str(t.item), ' ', end='')
            if t.left != None: 
                q.append(t.left)  
            if t.right != None: 
                q.append(t.right)    

    def height(self, root): # 트리 높이 계산
        if root == None:
            return 0
        return max(self.height(root.left), self.height(root.right))+ 1
  
    def size(self, root): # 트리 노드 수 계산
        if root is None:
            return 0
        else:
            return 1 + self.size(root.left) + self.size(root.right)  
     
    def copy_tree(self, n): # 트리 복제
        if n == None: 
            return None
        else: 
            left  = self.copy_tree(n.left)
            right = self.copy_tree(n.right)
            return self.Node(n.item, left, right)
   
    def is_equal(self, n, m): # 두 트리의 동일성 검사
        if n == None or m == None: 
            return n == m        
        if n.item != m.item: 
            return False      
        return( self.is_equal(n.left,  m.left) and  
                self.is_equal(n.right, m.right) )

