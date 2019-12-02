#include "types.h"
#include "user.h"
#define stdin 0
#define stdout 1
#define stderr 2

int main(int argc, char** argv)
{
	if(argc<2){
		printf(stdout, "Usage: bm child_1_tickets [child_2_tickets]...\n");
		exit();
	}
	printf(stdout, "Mother %d created\n", getpid());

	for(int i=1;i<argc;i++){
		const int pid = fork();
		if(pid<0){
			printf(stderr, "Stillbirth Occurred"); 
			exit();
		}
		if(!pid)
		{
			const int t = atoi(argv[i]);//number of tickets
			settickets(t);
			printf(stdout, "Child %d created with %d tickets\n", getpid(), t);
			sleep(5);
		}
	}
	for(int i=1;i<argc;i++){
		wait();
	}
	printf(stdout, "Parent exiting\n");
	exit();
}
