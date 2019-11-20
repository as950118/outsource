#include<pthread.h>
#include<stdlib.h>
#include<stdio.h>
#include<string.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include "bst.h"
Node *root=NULL;
Node *root_balanced=NULL;
int f_verbose = 0;

#define RAND_PERIOD 65536
unsigned int *rand_array;
//int *treeArray;
int init_rand(){
	int i;
	unsigned int r1, r2, temp;
	rand_array = (unsigned int*) malloc(RAND_PERIOD*sizeof(unsigned int));
	
	for(i=0; i<RAND_PERIOD; i++)
		rand_array[i] = i;
	
	// Shuffle array
	for(i=0; i<RAND_PERIOD; i++){
		r1 = rand() % RAND_PERIOD;
		r2 = rand() % RAND_PERIOD;
		temp = rand_array[r1];
		rand_array[r1] = rand_array[r2];
		rand_array[r2] = temp;
	}
	return 0;
}

int destroy_rand(){
	free(rand_array);
	return 0;
}

unsigned int unique_random_number(){
	static int rand_array_index=0;
	unsigned int temp;
	temp = rand_array[rand_array_index];
	rand_array_index++;
	return temp;
}






Node *insertNode(Node *root, int value)
{	
	Node* ptr = root;
	Node* par = NULL;
	
	while(ptr != NULL){
		if(value == (ptr->data)){
			//printf("Duplicate Key\n");
			return root;
		}
		par = ptr;
		
		if(value < ptr->data){
			if(ptr->left != NULL){
				ptr = ptr->left;
			}
			else{
				break;
			}
		}
		else{
			if(ptr->right != NULL){
				ptr = ptr->right;
			}
			else{
				break;
			}
		}
	}
	Node* temp = (Node *)malloc(sizeof(Node));
	temp->data = value;
	temp->left = NULL;
	temp->right = NULL;
	if(par == NULL){
		root = temp;
	}
	else if(value < par->data){
		par->left = temp;
	}
	else{
		par->right = temp;
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
    if (N == NULL){
        //printf("Node is null!\n");
        return 0;
    }
    printf("%d\n", N->data);
    int ret = 1;
    if(N->left != NULL)
    	ret += countNodes(N->left);
    if(N->right != NULL)
    	ret += countNodes(N->right);
    return ret;
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
	int treeSize = countNodes(root);
	printf("%d", treeSize);
	getchar();
	int * treeArray = (int *)malloc(sizeof(int)*treeSize);
	inOrderTraversal(root, treeArray, 0);
	int i;
	int ret=0;
	for(i=0; i<treeSize; i++){
		ret += treeArray[i];
	}
	free(treeArray);
	return ret;
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







pthread_rwlock_t lock = PTHREAD_RWLOCK_INITIALIZER;

void *downtime(){
	
	balanceTree(root);
	sleep(1);
	//TODO: 1st downtime: Do balanceTree here

	balanceTree(root);
	sleep(1);
	//TODO: 2nd downtime: Do balanceTree here

	balanceTree(root);
	sleep(1);
	//TODO: 3rd downtime: Do balanceTree here

	return NULL;
}


void* ServeClient(char *client){

	// TODO: Open the file and read commands line by line
	FILE *fp;
	fp = fopen(client, "r");
	if(fp == NULL){
		printf("Unable to open file\n");
		exit(-1);
	}
	
	
	// TODO: match and execute commands
	char ch[10];
	int num;
	
	while(fscanf(fp, "%s %d", ch, &num) != EOF)
	{
	// TODO: Handle command: "insertNode <some unsigned int value>"
	// print: "[ClientName]insertNode <SomeNumber>\n"
	// e.g. "[client1_commands]insertNode 1\n"
		if (strcmp("insertNode", ch) == 0)
		{
			printf("[%s]%s <%d>\n", client, ch, num);
			insertNode(root, num);
		}
	// TODO: Handle command: "deleteNode <some unsigned int value>"
	// print: "[ClientName]deleteNode <SomeNumber>\n"
	// e.g. "[client1_commands]deleteNode 1\n"
		else if (strcmp("deleteNode", ch) ==0)
		{
			printf("[%s]%s <%d>\n", client, ch, num);
			deleteNode(root, num);
		}
	// TODO: Handle command: "countNodes"
	// print: "[ClientName]countNodes = <SomeNumber>\n"
	// e.g. "[client1_commands]countNodes 1\n"
		else if (strcmp("countNode", ch) == 0)
		{
			num = countNodes(root);
			printf("[%s]%s = <%d>\n", client, ch, num);
		}
	// TODO: Handle command: "sumSubtree"
	// print: "[ClientName]sumSubtree = <SomeNumber>\n"
	// e.g. "[client1_commands]sumSubtree 1\n"
		else if (strcmp("sumSubtree", ch) == 0)
		{
			num = sumSubtree(root);
			printf("[%s]%s = <%d>\n", client, ch, num);
		}
	}

	fclose(fp);

	return NULL;
}

void clean(){
	/*****************************************************/
	/******   Free resources before program ends  ********/
	/*****************************************************/

	root=freeSubtree(root);
	root_balanced = freeSubtree(root_balanced);
	root= NULL;
	root_balanced = NULL;
	return;
}
#ifdef CYCLE_TEST
// DO NOT add any test functions here, as they will not be compiled
void test_cycle(){
	unsigned int COUNTER, REPEAT=1000;
	unsigned int i, r, sum, sum_balanced;

	init_rand();

	// Create a random BST rooted at 'root'
	for(i=0; i<10000; i++){
		r = unique_random_number();
		root=insertNode(root, r);
	}

	long int CLOCK_total, CLOCK_end, CLOCK_start;
	// Create a balanced BST from the unbalanced BST
	root_balanced = balanceTree(root);


	// Cycle count for sum on unbalanced BST
	CLOCK_total=0;
	for(COUNTER=0; COUNTER<REPEAT; COUNTER++)
	{
		CLOCK_start = cpucycles();
		sum = sumSubtree(root);
		CLOCK_end = cpucycles();
		CLOCK_total = CLOCK_total + CLOCK_end - CLOCK_start;
	}
	printf("Avg cycle count for unbalanced BST = %ld\n", CLOCK_total/REPEAT);
	printf("Sum of unbalanced BST = %u\n", sum);

	// Cycle count for sum on balanced BST
	CLOCK_total=0;
	for(COUNTER=0; COUNTER<REPEAT; COUNTER++)
	{
		CLOCK_start = cpucycles();
		sum_balanced = sumSubtree(root_balanced);
		CLOCK_end = cpucycles();
		CLOCK_total = CLOCK_total + CLOCK_end - CLOCK_start;
	}
	printf("Avg cycle count for balanced BST = %ld\n", CLOCK_total/REPEAT);
	printf("Sum of balanced BST = %u\n", sum_balanced);

	printf("Difference in sums = %d\n", sum - sum_balanced);

	clean();

}
#else
void test_task12(){
	unsigned int i,r, sum, sum_balanced;
	int failed = 0;
	init_rand();
	// Create a random BST rooted at 'root'
	for(i=0; i<10000; i++){
		r = unique_random_number();     // This will give you the same set of random numbers every time
		root=insertNode(root, r);
	}

	/*****************************************************/
	/******   Part 1 of Exercise 2 Starts here    ********/
	/*****************************************************/

	printf("/******** TEST OF PART 1 ********/\n\n");

	// Create a balanced BST from the unbalanced BST
	root_balanced = balanceTree(root);
	// Sum on unbalanced BST
	sum = sumSubtree(root);

	printf("Sum of unbalanced BST = %u\n", sum);

	// Sum on balanced BST
	sum_balanced = sumSubtree(root_balanced);

	printf("Sum of balanced BST = %u\n", sum_balanced);

	printf("Difference in sums = %d\n", sum - sum_balanced);
	//destroy_rand();
	printf("sese");

	failed = (sum - sum_balanced) + (sum - 289060379);
	
	if(failed || f_verbose)
	{
	  printf("\n/******** START DEBUG MODE *********/\n");

	  printf("\nUnbalanced tree:\n");
	  printf("label1\n");
	  printSubtree(root);
	  printf("label2\n");
	  printf("\nBalanced tree:\n");
	  printf("label3\n");
	  printSubtree(root_balanced);
	  printf("label4\n");
	  printf("\n/******** END DEBUG MODE ********/\n");
	}

	printf("\n /******** END OF PART 1 ********/\n\n");
	getchar();
	clean();
}

void test_tack34(){

	printf("/******** TEST OF PART 2 ********/\n\n");
	unsigned int i;
	char *client_names[5] = {"client1_commands", "client2_commands", "client3_commands",
	                         "client4_commands", "client5_commands"};

	pthread_t threads[6];

	/*****************************************************/
	/******   Part 2 of Exercise 2 Starts here    ********/
	/*****************************************************/

	// spawn all threads
	pthread_create(&threads[0], NULL, (void *) ServeClient, client_names[0]);
	pthread_create(&threads[1], NULL, (void *) ServeClient, client_names[1]);
	pthread_create(&threads[2], NULL, (void *) ServeClient, client_names[2]);
	pthread_create(&threads[3], NULL, (void *) ServeClient, client_names[3]);
	pthread_create(&threads[4], NULL, (void *) ServeClient, client_names[4]);
	pthread_create(&threads[5], NULL, (void *) downtime, NULL);


	// join all readers
	for (i = 0; i < 6; i++) {
		pthread_join(threads[i], NULL);
	}

	// The tree should only have one node now
	int count = countNodes(root);
	int sum = sumSubtree(root);

	if (count == 1 && sum == 1){
		printf("Test for Part2 seems OK\n");
	} else{
		printf("Test for Part2 fail\n");
	}

	// Free the tree
	clean();
}

// TODO: You could add more test functions here

#endif
int main(){

//	if(argc == 2){
//	  if(strcmp(argv[1],"-v") == 0)
//	    {
//	      f_verbose = 1;
//	    }
//	}
    f_verbose = 1;
#ifdef CYCLE_TEST
	// DO NOT add any test functions here, as they will not be compiled
	test_cycle();
#else
	test_task12();
	test_tack34();

	// TODO: You could call your test functions at here

#endif
	return 0;
}
