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
	//옵션을 parsing해주는 함수를 이용해서 s,d 옵션을 가져옴
	//그 후 switch를 이용해서 처리 
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

//숫자를 비교하는 함수 
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

	//첫줄에서 숫자 입력받기 
	int num_of_students;
	fscanf(fp, "%d", &num_of_students);
	
	//학생숫자만큼 동적할당 
	Student *Students = (Student *)calloc(num_of_students, sizeof(Student));

	//학생 정보 입력받기 
	for(i=0; i<num_of_students; i++){
		fscanf(fp, "%s %d %s", Students[i].name, &Students[i].num, Students[i].major);
	}
	
	//중요 순서 : major -> name -> num 
	//버블 정렬을 이용함 
	int flag;
	int k;
	Student temp_student;
	for(i=num_of_students; i>1; i--){
		for(j=1; j<i; j++){
			//i번째와 j번째를 비
			flag = strcmp(Students[j-1].major, Students[j].major);
			//major가 같은 경우 -> name 비교 
			if(flag == 0){
				flag = strcmp(Students[j-1].name, Students[j].name);
				//major와 name 모두 같은경우 -> num 비교 
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
			//i번째 major가 더 클 경우 
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

	//첫줄에서 숫자 입력받기 
	int num_of_num;
	fscanf(fp, "%d", &num_of_num);
	
	//한줄에 공백을 기준으로 숫자를 입력받음 
	double nums[num_of_num];
	for(i=0; i<num_of_num; i++){
		fscanf(fp, "%lf ", &nums[i]);
	}
	
	//버블 정렬
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
