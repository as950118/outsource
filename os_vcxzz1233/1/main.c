#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <memory.h>
#include "stack.h"
#include "faststack.h"
#define MAX 10000000  // 스택에 쌓이는 최대 크기 설정

int push_or_pop(int j, int pushnum, int popnum, int max) {
// max 정도 쌓일 때까지는 push가 주로 나옴.
// 전에 push 였으면 push가 가능성이 높고 pop이었으면 pop이 가능성이 높음.
	static double cont = 1.0;
	if (j%10 + 1 > ((pushnum-popnum)*cont/max)*10) {
		cont = 0.1; 
		return 1;
	}
	else {
		cont = 0.9;
		return 0;
	}
}

void test_fastStack() {
	int i, j,p,q;
	fastStack* s1 = newFastStack();
	i = p = q = 0;

	printf("---- check stack -----------------\n");
	while (i++<50) {
		j = rand()%100;
		if (push_or_pop(j, p, q, 10)) {
			p++;
			fastPush(s1,j);
			printf("push %d(%d):", j, p-q); printFastStack(s1);
		}
		else {
			q++;
			j = fastPop(s1);
			printf("pop %d(%d):", j, p-q); printFastStack(s1);
		}
	}
	printf("\npush:%d, pop:%d\n", p, q);
	printf("---------------------------------- \n");
	freeFastStack(s1);
}

void test_stack_speed(stack *s) {
	int i= 0,j;
	int p = 0;
	int q = 0;
	double cont = 1.0;
	int *t = (int *) malloc(4);
		
	i = -1;

	while (++i<MAX*40) {
		if (i%100000000 == 0) printf("\nStack size: %d", p-q);
		if (i%1000000 == 0) printf(".");
		j = rand();
		if (push_or_pop(j, p, q, MAX)) {
			push (s,j); 
			p++;
			cont = 0.4;
		}
		else {
			pop(s);
			q++;
			cont = 1.6;
		}

		fflush(stdout);
	}
	printf("\npush:%d, pop:%d\n", p, q);
}

void test_fastStack_speed(fastStack *s) {
	int i= 0,j;
	int p = 0;
	int q = 0;
	double cont = 1.0;
	int *t = (int *) malloc(4);
	i = -1;

	while (++i<MAX*40) {
		if (i%100000000 == 0) printf("\nStack size: %d", p-q);
		if (i%1000000 == 0) printf(".");
		j = rand();
		if (push_or_pop(j, p, q, MAX)) {
			fastPush (s,j); 
			p++;
			cont = 0.4;
		}
		else {
			fastPop(s);
			q++;
			cont = 1.6;
		}

		fflush(stdout);
	}
	printf("\npush:%d, pop:%d\n", p, q);
}

main() {
    clock_t before;
    double  result, result2;
    stack* s; 
    fastStack* fs; 

    printf("Fast Stack Test\n");
    test_fastStack();
    printf("\n\n");

    printf("Normal Stack Speed\n");
    s = newStack(); 
    before  = clock(); 
    test_stack_speed(s);
    result = (double)(clock() - before) / CLOCKS_PER_SEC;
    printf("걸린시간은 %5.2f 입니다.\n", result);
    freeStack(s); 

    printf("Fast Stack Speed\n");
    fs = newFastStack(); 
    before  = clock(); 
    test_fastStack_speed(fs);
    result2 = (double)(clock() - before) / CLOCKS_PER_SEC;
    printf("개선된 스택의 걸린시간은 %5.2f 입니다.\n", result2);

    printf("\n속도 향상(percent): %f%% \n\n", (result-result2)/result);
    freeFastStack(fs); 

}
