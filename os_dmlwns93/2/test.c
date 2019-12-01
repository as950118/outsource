#include "types.h"
#include "stat.h"
#include "user.h"
#define stdin 0
#define stdout 1
#define stderr 2

int
main(int argc, char *argv[]) {
	if(argc<2){
		printf(stdout, "Usage: lottery_sched child_1_tickets [child_2_tickets]...\n");
		exit();
	}
    int rc1 = fork();

    if (rc1 == 0) {
        settickets(30);
        sleep(50);
    } else if (rc1 > 0) {
        int rc2 = fork();
        if (rc2 == 0) {
            settickets(20);
            sleep(50);
        } else if (rc2 > 0) {
            int rc3 = fork();
            if (rc3 == 0) {
                settickets(10);
                sleep(50);
            }
        }
    }
    
    for (int i = 0; i < 3; i++) {
        wait();
    }

    exit();
}

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

