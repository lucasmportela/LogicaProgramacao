
#include <graphics.h>
#include <stdio.h>
#include <conio.h>

int main()
{
    initwindow (1920, 1000);

    setfillstyle(SOLID_FILL, GREEN);
    rectangle(20, 20, 1890, 980);
    floodfill(22, 22, 15);
 
    setfillstyle(SOLID_FILL, BLUE);
    circle(950, 500, 160);
    floodfill(952, 498, 15);
    
    setfillstyle(SOLID_FILL, YELLOW);
    //bottom left
    line(400, 500, 945, 180);
  
    //top left
    line(400, 500, 945, 820);
 
    //top right
    line(1500, 500, 945, 180);

    //bottom right
    line(1500, 500, 945, 820);
    floodfill(552, 498, 15);

    getch();
    closegraph();
}