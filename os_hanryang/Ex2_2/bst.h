#ifndef BST_H
#define BST_H
typedef struct Node
{
	int data;
	struct Node *left;
	struct Node *right;
} Node;

Node *insertNode(Node *root, int value);
Node *deleteNode(Node *root, int value);
Node *inorderSuccessor(Node *root, int value);
Node *findMinimum(Node *root);
void printSubtree(Node *N);
int countNodes(Node *N);
Node *freeSubtree(Node *N);
Node *balanceTree(Node *root);
int inOrderTraversal(Node *N, int arr[], int index);
Node* reAdd(Node *N, int arr[], int first, int last);
int sumSubtree(Node *N);

#endif
