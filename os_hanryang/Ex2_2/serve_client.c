
pthread_rwlock_t lock = PTHREAD_RWLOCK_INITIALIZER;

void *downtime(){
	
	root = balanceTree(root);
	sleep(1);
	//TODO: 1st downtime: Do balanceTree here

	root = balanceTree(root);
	sleep(1);
	//TODO: 2nd downtime: Do balanceTree here

	root = balanceTree(root);
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
