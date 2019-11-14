struct _node {
	int v;
	struct _node * next;
};
typedef struct _node node;

typedef struct {
	node* l;
} stack;

stack *newStack(); 
void freeStack(stack *);
int pop(stack * s);
void push(stack * s, int v); 
void printstack(stack * s);
