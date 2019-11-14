#include <stdlib.h>
#include <stdio.h>
#include <memory.h>
#include "stack.h"

stack *newStack() {
	stack *s = (stack *)malloc(sizeof(stack));
	s->l = NULL;
	return s;
}

void freeStack(stack *s) {
        node *n1, *n2;
        if (s == NULL)
                return;
        n1 = n2 = s->l;
        while (n1) {
                n1 = n1->next;
                free(n2);
                n2 = n1;
        }
        free(s);
}

int pop(stack * s) {
	int v;
	node *f;
	if (s->l == NULL) {
		printf("empty \n");
		return 0;
	}

    /* 첫 노드 삭제 */
	f = s->l;   
	v = f->v;
	s->l = f->next;
	free(f);

	return v;
}

void push(stack * s, int v) {
	node *n;
	n = (node *)malloc(sizeof(node));
	if (n==NULL) {
		printf("full \n");
		return;
	}

	n->v = v;
	n->next = s->l;
	s->l = n;
}

void printstack(stack *s) {
	node *n = s->l;
	while (n!=NULL) {
		printf("%d ", n->v);
		n = n->next;
	}
	printf("\n");
}
