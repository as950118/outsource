
pthread_rwlock_t lock = PTHREAD_RWLOCK_INITIALIZER;

void *downtime(){

	sleep(1);
	//TODO: 1st downtime: Do balanceTree here

	sleep(1);
	//TODO: 2nd downtime: Do balanceTree here

	sleep(1);
	//TODO: 3rd downtime: Do balanceTree here

	return NULL;
}


void* ServeClient(char *client){

	// TODO: Open the file and read commands line by line

	char ch;
	FILE *fp;
	fp = open(client, "r");
	int num;
	while(fsacnf(fp, "%s %d",&ch, &num) != EOF)
	{
		if (strcmp("insertNode", &ch) == 0)
		{
			printf("[%s]insertNode <%d>\n", ,);			
			insertNode(&num);
		}
		else if (strcmp("deleteNode", &ch) ==0)
		{
			deleteNode(&num);
		}
		else if (strcmp("countNode", &ch) == 0)
		{
			countNode(root);
		}
		else if (strcmp("sumSubtree", &ch) == 0)
		{
			sumSubtree(root);	
		}
			
	}

	
	// TODO: match and execute commands

	fclose(fp);

	// TODO: Handle command: "insertNode <some unsigned int value>"
	// print: "[ClientName]insertNode <SomeNumber>\n"
	// e.g. "[client1_commands]insertNode 1\n"

	// TODO: Handle command: "deleteNode <some unsigned int value>"
	// print: "[ClientName]deleteNode <SomeNumber>\n"
	// e.g. "[client1_commands]deleteNode 1\n"

	// TODO: Handle command: "countNodes"
	// print: "[ClientName]countNodes = <SomeNumber>\n"
	// e.g. "[client1_commands]countNodes 1\n"


	// TODO: Handle command: "sumSubtree"
	// print: "[ClientName]sumSubtree = <SomeNumber>\n"
	// e.g. "[client1_commands]sumSubtree 1\n"


	return NULL;
}
