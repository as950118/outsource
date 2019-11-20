#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<unistd.h>

int i,j;
typedef struct student Student;
struct student{
	char name[10];
	int num;
	char major[10];
};

int cmp_int(int a, int b);
int case_s(int argc, char *argv[]);
int case_d(int argc, char *argv[]);

int main(int argc, char *argv[]){
	int opt;
	//�ɼ��� parsing���ִ� �Լ��� �̿��ؼ� s,d �ɼ��� ������
	//�� �� switch�� �̿��ؼ� ó�� 
	while( (opt = getopt(argc, argv, "sd")) != -1 ){
		switch(opt){
			case 's':
				case_s(argc, argv);
				break;
			case 'd':
				case_d(argc, argv);
				break;
		}
	}
}

//���ڸ� ���ϴ� �Լ� 
int cmp_int(int a, int b){
	if(a==b){
		return 0;
	}
	if(a>b){
		return 1;
	}
	return -1;
}


int case_s(int argc, char *argv[]){
	char *filename = argv[2];
	FILE* fp = fopen(filename, "r");

	//ù�ٿ��� ���� �Է¹ޱ� 
	int num_of_students;
	fscanf(fp, "%d", &num_of_students);
	
	//�л����ڸ�ŭ �����Ҵ� 
	Student *Students = (Student *)calloc(num_of_students, sizeof(Student));

	//�л� ���� �Է¹ޱ� 
	for(i=0; i<num_of_students; i++){
		fscanf(fp, "%s %d %s", Students[i].name, &Students[i].num, Students[i].major);
	}
	
	//�߿� ���� : major -> name -> num 
	//���� ������ �̿��� 
	int flag;
	int k;
	Student temp_student;
	for(i=num_of_students; i>1; i--){
		for(j=1; j<i; j++){
			//i��°�� j��°�� ��
			flag = strcmp(Students[j-1].major, Students[j].major);
			//major�� ���� ��� -> name �� 
			if(flag == 0){
				flag = strcmp(Students[j-1].name, Students[j].name);
				//major�� name ��� ������� -> num �� 
				if(flag == 0){
					flag = cmp_int(Students[j-1].num, Students[j].num);
					if(flag>0){
						temp_student = Students[j];
						Students[j] = Students[j-1];
						Students[j-1] = temp_student;
					}
				}
				else if(flag>0){
					temp_student = Students[j];
					Students[j] = Students[j-1];
					Students[j-1] = temp_student;
				}
			}
			//i��° major�� �� Ŭ ��� 
			else if(flag>0){
				temp_student = Students[j];
				Students[j] = Students[j-1];
				Students[j-1] = temp_student;
			}

		}
	}
	for(i=0; i<num_of_students; i++){
		printf("%s %d %s\n", Students[i].name, Students[i].num, Students[i].major);
	}
}

int case_d(int argc, char *argv[]){
	char *filename = argv[2];
	FILE* fp = fopen(filename, "r");

	//ù�ٿ��� ���� �Է¹ޱ� 
	int num_of_num;
	fscanf(fp, "%d", &num_of_num);
	
	//���ٿ� ������ �������� ���ڸ� �Է¹��� 
	double nums[num_of_num];
	for(i=0; i<num_of_num; i++){
		fscanf(fp, "%lf ", &nums[i]);
	}
	
	//���� ����
	double temp;
	for(i=num_of_num; i>1; i--){
		for(j=1; j<i; j++){
			if(cmp_int(nums[j-1], nums[j]) > 0){
				temp = nums[j];
				nums[j] = nums[j-1];
				nums[j-1] = temp;
			}
		}
	}
	for(i=0; i<num_of_num; i++){
		printf("%0.1lf ", nums[i]);
	}
}
