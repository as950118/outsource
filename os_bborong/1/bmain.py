from binary_tree import BinaryTree, Node
#from nonrecursion import BinaryTree, Node
if __name__ == '__main__':
    t = BinaryTree() # 이진트리 객체 t 생성
    n1 = Node(100)   # 8개의 노드 생성
    n2 = Node(200)
    n3 = Node(300)    
    n4 = Node(400)    
    n5 = Node(500)    
    n6 = Node(600)
    n7 = Node(700)    
    n8 = Node(800)
    n1.left  = n2  # n1의 왼쪽 자식->  n2
    n1.right = n3  # n1의 오른쪽 자식-> n3
    n2.left  = n4  # n2의 왼쪽 자식->  n4
    n2.right = n5  # n2의 오른쪽 자식-> n5
    n3.left  = n6  # n3의 왼쪽 자식->  n6
    n3.right = n7  # n3의 오른쪽 자식-> n7
    n4.left  = n8  # n4의 왼쪽 자식->  n8       
    t.root = n1    # t의 루트노드를 n1으로
    print('트리 높이 =', t.height(t.root))
    print('전위순회:\t', end='')
    t.preorder(t.root)
    print('\n중위순회:\t', end='')
    t.inorder(t.root)
    print('\n후위순회:\t', end='')
    t.postorder(t.root)
    print('\n레벨순회:\t', end='')
    t.levelorder(t.root)
