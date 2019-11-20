struct _fastNode {
	int v;
	struct _fastNode * next;
};
typedef struct _fastNode fastNode;

typedef struct {
	fastNode* l;
} fastStack;

fastStack *newFastStack(); 
void freeFastStack(fastStack *);
int fastPop(fastStack * s);
void fastPush(fastStack * s, int v); 
void printFastStack(fastStack * s);
