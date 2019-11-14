#include<stdio.h>
#include<stdlib.h>
#include "bst.h"

/*
except for the helper function 'findMinNode, all functions are the recursive function.
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
