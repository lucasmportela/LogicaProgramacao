#include <sys/types.h>

#include <sys/socket.h>

#include <unistd.h>

#include <netinet/in.h>

int main( int argc, char ** argv )

{

int listenfd, connfd, size;

struct sockaddr_in myaddr, cliaddr;

listenfd = socket( AF_INET,SOCK_STREAM, 0 );

memset( &myaddr, 0, sizeof(myaddr) );

myaddr.sin_family = AF_INET;

myaddr.sin_port = htons(12345);

myaddr.sin_addr.s_addr =

INADDR_ANY;

bind( listenfd, (struct sockaddr *)&myaddr, sizeof(myaddr) );

listen( listenfd, 5 );

for( ; ; )

{

memset( &cliaddr, 0,

sizeof(cliaddr) );

size = sizeof( cliaddr );

connfd = accept( listenfd, (struct sockaddr *)&cliaddr, &size );

send( connfd, “Alo Mundo!”, 10,MSG_WAITALL );

close( connfd );

}

return 0;

}