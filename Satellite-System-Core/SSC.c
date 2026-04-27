#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h> 
#include <arpa/inet.h>
#include <sys/socket.h>

#define SERVER_IP "server_ip"
#define PORT 9000

int main() {
    int sock;
    struct sockaddr_in server_addr;
    char *message = "Telemetry Code Here";

    sock = socket(AF_INET, SOCK_DGRAM, 0);
    if (sock < 0) return -1;

    memset(&server_addr, 0, sizeof(server_addr));
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(PORT);
    server_addr.sin_addr.s_addr = inet_addr(SERVER_IP);

    while (1) {
        sendto(sock, message, strlen(message), 0, 
               (struct sockaddr *)&server_addr, sizeof(server_addr));
        
        sleep(5);
    }

    close(sock);
    return 0;
}
