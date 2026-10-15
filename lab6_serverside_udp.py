// UDP Server - Two Way Communication

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netinet/in.h>

#define PORT 8080
#define MAXLINE 1024

int main()
{
    int sockfd;
    char buffer[MAXLINE];
    char message[MAXLINE];

    struct sockaddr_in servaddr, cliaddr;
    socklen_t len;
    int n;

    // Create UDP socket
    sockfd = socket(AF_INET, SOCK_DGRAM, 0);

    if (sockfd < 0)
    {
        perror("Socket creation failed");
        exit(EXIT_FAILURE);
    }

    // Clear structures
    memset(&servaddr, 0, sizeof(servaddr));
    memset(&cliaddr, 0, sizeof(cliaddr));

    // Server information
    servaddr.sin_family = AF_INET;
    servaddr.sin_addr.s_addr = INADDR_ANY;
    servaddr.sin_port = htons(PORT);

    // Bind socket
    if (bind(sockfd,
             (const struct sockaddr *)&servaddr,
             sizeof(servaddr)) < 0)
    {
        perror("Bind failed");
        close(sockfd);
        exit(EXIT_FAILURE);
    }

    printf("Server started on port %d\n", PORT);
    printf("Waiting for client...\n");

    while (1)
    {
        len = sizeof(cliaddr);

        // Receive message from client
        n = recvfrom(sockfd,
                     buffer,
                     MAXLINE - 1,
                     0,
                     (struct sockaddr *)&cliaddr,
                     &len);

        if (n < 0)
        {
            perror("recvfrom failed");
            break;
        }

        buffer[n] = '\0';

        printf("Client: %s\n", buffer);

        // If client says bye, stop server
        if (strcmp(buffer, "bye") == 0)
        {
            printf("Client ended the chat.\n");
            break;
        }

        // Server enters reply
        printf("Server: ");
        fgets(message, MAXLINE, stdin);

        // Remove newline
        message[strcspn(message, "\n")] = '\0';

        // Send reply to client
        sendto(sockfd,
               message,
               strlen(message),
               0,
               (const struct sockaddr *)&cliaddr,
               len);

        // Server can also end
        if (strcmp(message, "bye") == 0)
        {
            printf("Server ended the chat.\n");
            break;
        }
    }

    close(sockfd);

    printf("Server closed.\n");

    return 0;
}
