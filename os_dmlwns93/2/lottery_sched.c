#include "types.h"
#include "user.h"
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
			// Loop forever
			while(1);
			printf(stdout, "Child %d exiting\n", getpid());
			exit();
		}
	}
	for(int i=1;i<argc;i++){
		wait();
	}
	printf(stdout, "Parent exiting\n");
	exit();
}
