#include <stdio.h>
#include <windows.h>
#include <time.h>

int main(int argc, char **argv){
    // 找到窗口并改名
    srand(time(NULL));
    int r = rand() % 100000;
    char w_name[] = "00000";
    itoa(r, w_name, 10); 

    HWND hwnd;
    while (1)
    {
        hwnd = FindWindow("UninstallVerify", NULL);
        if(hwnd != NULL){
            break;
        }
    }
    HWND hwnd1 = FindWindowEx(hwnd, NULL, "Edit", NULL);
    HWND hwnd2 = FindWindowEx(hwnd, NULL, "Button", NULL);
    HWND hwnd3;
    SetWindowText(hwnd, w_name);

    for(int i=1; i<argc; i++){
        // pwd = argv[i]
        // 发送消息
        if(hwnd != NULL){ // 有效
            SendMessage(hwnd1, WM_SETTEXT, 0, argv[i]);
            SendMessage(hwnd2, WM_LBUTTONDOWN, 0, 0);
            SendMessage(hwnd2, WM_LBUTTONUP, 0, 0);
            while(1){
                hwnd3 = FindWindow("#32770", NULL); // 必须关闭自己的对话框
                if(hwnd3 != NULL){
                    SendMessage(hwnd3, WM_CLOSE, 0, 0);
                    break;
                }
            }
            // FindWindow("UninstallVerify", w_name);
            hwnd = GetParent(hwnd1); // 判断窗口是否还在
            if(hwnd == NULL){
                printf("%s\n", argv[i]);
                FILE *fp;
                fp = fopen("pwd.txt", "w+");
                fprintf(fp, "最可能的密码: %s\n", argv[i]);
                fprintf(fp, "同组密码: ");
                for(int k=1; k<argc; k++){
                    fprintf(fp, "%s ", argv[k]);
                }
                fprintf(fp, "\n");
                fclose(fp);
                SendMessage(hwnd, WM_CLOSE, 0, 0);
                return 2;
            }
        }else{
            SendMessage(hwnd, WM_CLOSE, 0, 0);
            printf("execute failed!\n"); // 从进程列表中去除本进程 并把本组密码放回重试
            return -1;
        }
    }
    SendMessage(hwnd, WM_CLOSE, 0, 0);
    printf("No pwd\n"); // 从进程列表中去除本进程 并去除本组密码
    return 1;
}