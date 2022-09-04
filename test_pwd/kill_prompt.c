#include <windows.h>

int main(){
    while(1){
        HWND hwnd = FindWindow("#32770", NULL);
        if(hwnd){
            SendMessage(hwnd, WM_CLOSE, 0, 0);
        }
    }
    return 0;
}


