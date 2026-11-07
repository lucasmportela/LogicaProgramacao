// C program to create a smiley face
#include <conio.h>
#include <dos.h>
#include <graphics.h>
#include <stdio.h>
 
// Driver Code
int main()
{
 
    // Initialize graphic driver
    int gr = DETECT, gm;
 
    // Initialize graphics mode by passing
    // three arguments to initgraph function
 
    // &gdriver is the address of gdriver
    // variable, &gmode is the address of
    // gmode and  "C:\\Turboc3\\BGI" is the
    // directory path where BGI files
    // are stored
    initgraph(&gr, &gm, "");
 
    // Set color of smiley to yellow
    setcolor(YELLOW);
 
    // creating circle and fill it with
    // yellow color using floodfill.
    circle(300, 200, 120);
    setfillstyle(SOLID_FILL, YELLOW);
    floodfill(300, 200, YELLOW);
 
    // Set color of background to black
    setcolor(BLACK);
    setfillstyle(SOLID_FILL, BLACK);
 
    // Use fill ellipse for creating eyes
    fillellipse(260, 160, 24, 28);
    fillellipse(340, 160, 24, 28);
 
    // Use ellipse for creating mouth
    ellipse(300, 230, 205, 335, 80, 40);
    ellipse(300, 230, 205, 335, 80, 41);
    ellipse(300, 230, 205, 335, 80, 42);
    ellipse(300, 230, 205, 335, 80, 43);
    ellipse(300, 230, 205, 335, 80, 44);
    ellipse(300, 230, 205, 335, 80, 45);
    ellipse(300, 230, 205, 335, 80, 46);
    ellipse(300, 230, 205, 335, 80, 47);
    ellipse(300, 230, 205, 335, 80, 48);
    ellipse(300, 230, 205, 335, 80, 49);
 
    getch();
 
    // closegraph function closes the
    // graphics mode and deallocates
    // all memory allocated by
    // graphics system
    closegraph();
 
    return 0;
}