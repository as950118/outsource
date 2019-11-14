#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include <unistd.h>
#include "bst.h"

#define MAX(a,b) ((a>b) ? a : b)

/*

Place for the BST functions from Exercise 1.

*/

Node* insertNode(Node *root, int value)
{
	/*
	describe
	add new node with value 'data'
	we assume that we don't care the duplicates in tree.
	*/
	
	if (root == NULL)
	{
		root = malloc(sizeof (Node));
		root->data = value;
		root->left = NULL;
		root->right = NULL;
	}
	else if (value < root->data)
	{
		root->left = insertNode(root->left, value);
	}
	else
	{
		root->right = insertNode(root->right, value);
	}
	
	return root;
}

Node* findMinNode(Node* root){

	/*
	describe
	finding minimum value node at the tree
	this is helper function for deleteNode.
	*/
	struct Node* temp = root;
	while(temp->left != NULL){
		temp = temp->left;
	}
	return temp;
}

Node* deleteNode(Node* root, int value){

	/*
	describe
	remove node that has value 'value'
	if leaf has 'value', then remove it
	if node(which has left or right) has 'value', have to find
	minimum of the right, and then replace it.
	*/

	struct Node *temp;

	if(root == NULL){
		return NULL;
	}

	if(root->data > value){
		root->left = deleteNode(root->left, value);
	}else if(root->data < value){
		root->right = deleteNode(root->right, value);
	}else {
		if(root->left != NULL && root->right != NULL) {
			temp = findMinNode(root->right);
			root->data = temp->data;
			root->right = deleteNode(root->right, temp->data);
		}else{
			temp = (root->left == NULL) ? root->right : root->left;
			free(root);
			return temp;
		}
	}
	return root;
}

void printSubtree(Node *N){
	
	/*
	describe
	print trees "inorder" way
	whic is left, node, right order
	*/

	if(N == NULL){
		return;
	}
	printSubtree(N->left);
	printf("%d\n", N->data);
	printSubtree(N->right);
	
	return;
}

int countNodes(Node *N){

	/*
	describe
	count all node in N
	*/

	int count = 0;

	if(N == NULL){
		return 0;
	}
	
	count = countNodes(N->left) + countNodes(N->right);

	return count;
}

Node* freeSubtree(Node *N){

	/*
	free all nodes in tree N except root Node	
	*/

	struct Node *left;
	struct Node *right;

	if(N == NULL) {
		return N;
	}

	left = N->left;
	right = N->right;

	N->left = NULL;
	N->right = NULL;
	
	freeSubtree(left);
	freeSubtree(right);

	if(left != NULL){
		free(left);
	}

	if(right != NULL){
		free(right);
	}
	
	return N;
}

*/  


int sumSubtree(Node *N)
{

	// TODO: Implement this function
	if (N == NULL)
		return 0;
	return (N->data + sumSubtree(N->left) + sumSubtree(root->right)); 
}

int height(struct Node* N)
{
	if (N == NULL)
		return 0;
	else
	{
		/* compute the depth of each subtree */
		int lHeight = height(N->left);
		int rHeight = height(N->right);
		
		/*use the larger one */
		if (lHeight > rHeight)
			return (lHeight+1);
		else return(rHeight+1);
	}
}

/*
struct Node* newNode(int data)
{
	struct Node* Node = (struct Node*)malloc(sizeof(struct Node));
	
	Node->data = data;
	Node->left = NULL;
	Node->right = NULL;
	
	return(Node);
}
*/



struct Node *rightRotate(struct Node *y)
{
	struct Node *x = y->left;
	struct Node *T2 = x->right;

	x->right = y;
	y->left = T2;

	// How to update heights?

	return y;

}

struct Node *leftRotate(struct Node *x)
{
	struct Node *y = x->right;
	struct Node *T2 = y->left;

	y->left = x;
	x->right = T2;

	// How to update heights?

	return y;
}

int getBalance(struct Node *N)
{
	if (N == NULL)
		return 0;
	return height(N->left) - height(N->right);
}



// This functions converts an unbalanced BST to a balanced BST 
Node* balanceTree(Node* root) 
{
	int balacne = getBalance(root);
	int balance_left = getBalance(root->left);
	int balance_right = getBalacne(root->right);

	// TODO: Implement this function
	if (balance > 1 && 0 < balance_left)
		 return rightRoatate(root);
	 
	if (balance < -1 && 0 > balance_right)
		 return leftRoatate(root);

	if (balance > 1 && 0 > balance_left)
		 return rightRoatate(root);

	if (balance >1 && 0 < balance_left)
		 return leftRoatate(root);

	return root;
	
} 






