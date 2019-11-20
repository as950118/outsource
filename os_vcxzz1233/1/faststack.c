#include <stdlib.h>
#include <stdio.h>
#include <memory.h>
#include "faststack.h"

fastStack *newFastStack() {
	fastStack *s = (fastStack *)malloc(sizeof(fastStack));
	s->l = NULL;
	return s;
}

void freeFastStack(fastStack *s) {
        fastNode *n1, *n2;
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

int fastPop(fastStack * s) {
	int v;
	fastNode *f;
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

void fastPush(fastStack * s, int v) {
	fastNode *n;
	n = (fastNode *)malloc(sizeof(fastNode));
	if (n==NULL) {
		printf("full \n");
		return;
	}

	n->v = v;
	n->next = s->l;
	s->l = n;
}

void printFastStack(fastStack *s) {
	fastNode *n = s->l;
	while (n!=NULL) {
		printf("%d ", n->v);
		n = n->next;
	}
	printf("\n");
}

