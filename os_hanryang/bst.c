#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include <unistd.h>
#include "bst.h"


/*

Place for the BST functions from Exercise 1.

*/

int height(struct Node* node);

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
	int count=0;
	if(N==NULL)
		return 0;
	count = count + countNodes(N->left);
	count = count + countNodes(N->right);
	count = count + 1;
	return count;
}

Node* freeSubtree(Node *N){
	if (N==NULL)
		return N;
	if (N->left)
		freeSubtree(N->left);
	if (N->right)
		freeSubtree(N->right);
	free(N);
	N = NULL; 
	return N;  	
}

  


int sumSubtree(Node *N)
{

	// TODO: Implement this function
	if (N == NULL)
		return 0;
	return (N->data + sumSubtree(N->left) + sumSubtree(N->right)); 
}

int max(int a, int b)
{
	return (a >= b) ? a : b;
}

int height(Node *N)
{
	int height_left = 0;
	int height_right = 0;

	if(N->left) height_left = height(N->left);
	if(N->right) height_right = height(N->right);

	return height_right > height_left ? ++height_right : ++height_left;
}

int balance_factor(Node *N)
{
	int bf = 0;
	
	if(N->left) bf += height(N->left);
	if(N->right) bf += height(N->right);
	
	return bf;
}


Node *llRotate(Node *node)
{
	Node *a = node;
	Node *b = a->left;
	
	a->left = b->right;
	b->right = a;
	
	return (b);
}

Node *lrRotate(Node *node)
{
	Node *a = node;
	Node *b = a->left;
	Node *c = b->right;
	
	a->left = c->right;
	b->right = c->left;
	c->left = b;
	c->right = a;

	return (c);

}

Node *rlRotate(Node *node)
{
	Node *a = node;
	Node *b = a->right;
	Node *c = b->left;

	a->right = c->left;
	b->left = c->right;
	c->right = b;
	c->left = a;

	return (c);

}

Node *rrRotate(Node *node)
{
	Node *a = node;
	Node *b = a->right;
	
	a->right = b->left;
	b->left = a;
	
	return (b);

}

// This functions converts an unbalanced BST to a balanced BST 
Node* balanceTree(Node* root) 
{
	Node *newroot = NULL;
	
	if(root->left)
		root->left = balanceTree(root->left);
	if(root->right)
		root->right = balanceTree(root->right);

	int bf = balance_factor(root);

	if(bf >=2)
	{
		if(balance_factor(root->left) <= -1)
			newroot = lrRotate(root);
		else
			newroot = llRotate(root);	
	}
	else if(bf <= -2)
	{
		if(balance_factor(root->right) >= 1)
			newroot = rlRotate(root);
		else
			newroot = rrRotate(root);
	}
	else
		newroot = root;
	return newroot;
}








