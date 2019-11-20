#include <stdio.h>
#include <stdlib.h>
#include "bst.h"

Node *insertNode(Node *root, int value)
{
    // check for the empty tree.
    if (root == NULL)
    {
        root = (Node *)malloc(sizeof(Node));
        if (root == NULL)
        {
            //printf("Allocation unsuccessful\n");
            return NULL;
        }
        // Initialise all data values.
        root->data = value;
        root->left = NULL;
        root->right = NULL;
        //printf("Node with value %d has been inserted\n", value);
    }
    else if (value > root->data)
    { // Inserting the data.
        //printf("%d > %d so inserting right\n", value, root->data);
        root->right = insertNode(root->right, value);
    }
    else
    {
        //printf("%d < %d so inserting left\n", value, root->data);
        root->left = insertNode(root->left, value);
    }
    return root;
}

Node *deleteNode(Node *root, int value)
{
    // Firstly, we can check if the tree is empty...
    if (root == NULL)
    {
        //printf("Tree is empty!\n");
        return root;
    }

    // We first need to traverse to the part of the tree which holds our value...
    if (value == root->data)
    {
        //printf("%d = %d so deleting node\n", value, root->data);
        if (root->left == NULL)
        { // Right children exist
            //printf("Deleting node\n");
            Node *temp = root->right;
            free(root);
            return temp;
        }
        else if (root->right == NULL)
        { // Left children exist.
            //printf("Deleting node\n");
            Node *temp = root->left;
            free(root);
            return temp;
        }
        // When left AND right children exist.
        Node *temp = findMinimum(root->right);
        root->data = temp->data;
        root->right = deleteNode(root->right, temp->data);
    }
    else if (value > root->data)
    {
        //printf("%d > %d so traversing right subtree\n", value, root->data);
        root->right = deleteNode(root->right, value);
    }
    else
    { // The default case where the value is less than the root.
        //printf("%d < %d so traversing left subtree\n", value, root->data);
        root->left = deleteNode(root->left, value);
    }
    return root;
}

// inorder sucessor finds the minimum value of the right child of the root passed into it.
Node *findMinimum(Node *root)
{
    while (root->left != NULL)
    {
        root = root->left;
    }
    return root;
}

// Prints using in order traversal.
void printSubtree(Node *N)
{
    if (N == NULL)
    {
        return;
    }

    printSubtree(N->left);
    printf("%d\n", N->data);
    printSubtree(N->right);
}

int countNodes(Node *N)
{
    //printf("Inside count nodes\n");
    if (N == NULL)
    {
        //printf("Node is null!\n");
        return 0;
    }
    return 1 + countNodes(N->left) + countNodes(N->right);
}

Node *balanceTree(Node *root)
{
    // Perform an in order traversal and store every item in an array.
    int treeSize = countNodes(root);
    //printf("Tree size is %d\n", treeSize);
    int *treeArray = (int *)malloc(sizeof(int) * treeSize);
    inOrderTraversal(root, treeArray, 0);

    root = freeSubtree(root); // Clear the tree to start balancing.

    for (int i = 0; i < treeSize; i++)
    {
        //printf("index %d in tree array: %d\n", i, treeArray[i]);
    }

    // Next, we recursively add the items back into the tree.
    root = reAdd(root, treeArray, 0, treeSize - 1);

	free(treeArray);
    return root;
}

Node *reAdd(Node *N, int arr[], int first, int last)
{
    // Take the middle item in the array and add to the tree.
    // Recursively call the left then right side.
    if (first > last)
    {
        return NULL;
    }

    int mid = (first + last) / 2; // The middle element in the array.
    //printf("middle item in array is %d\n", arr[mid]);
    N = insertNode(N, arr[mid]);
    reAdd(N, arr, first, mid - 1);
    reAdd(N, arr, mid + 1, last);
    return N;
}

int inOrderTraversal(Node *N, int arr[], int index)
{
    if (N == NULL)
        return index;

    index = inOrderTraversal(N->left, arr, index);
    arr[index] = N->data;
    return inOrderTraversal(N->right, arr, index + 1);
}

int sumSubtree(Node *N)
{
    if (N == NULL)
        return 0;
    return sumSubtree(N->left) + N->data + sumSubtree(N->right);
}

Node *freeSubtree(Node *N)
{
    // Start from bottom of the tree and go up.
    if (N == NULL)
    { // If tree is empty.
        //printf("Node is null\n");
        return N;
    }
    N->left = freeSubtree(N->left);
    N->right = freeSubtree(N->right);
    free(N);
    N = NULL;
    //printf("Node has been freed\n");

    return N;
}
