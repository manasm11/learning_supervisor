#include<stdio.h>
#include<unistd.h>
int main(){
    while(1){
        printf("%s", "I am still running\n");
        sleep(5);
    }
}