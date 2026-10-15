// UDP Client - Machine to Machine Communication

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

    struct sockaddr_in servaddr;
    socklen_t len;
    int n;

    // Create UDP socket
    sockfd = socket(AF_INET, SOCK_DGRAM, 0);

    if (sockfd < 0)
    {
        perror("Socket creation failed");
        exit(EXIT_FAILURE);
    }

    // Clear server address
    memset(&servaddr, 0, sizeof(servaddr));

    // Server information
    servaddr.sin_family = AF_INET;
    servaddr.sin_port = htons(PORT);

    // Friend's IP address
    if (inet_pton(AF_INET, "10.21.3.115", &servaddr.sin_addr) <= 0)
    {
        perror("Invalid server IP address");
        close(sockfd);
        exit(EXIT_FAILURE);
    }

    len = sizeof(servaddr);

    printf("Client started.\n");
    printf("Server IP: 10.21.3.115\n");
    printf("Server Port: %d\n", PORT);
    printf("Type 'bye' to end the chat.\n\n");

    while (1)
    {
        // Enter message
        printf("Client: ");

        if (fgets(message, MAXLINE, stdin) == NULL)
        {
            break;
        }

        // Remove newline
        message[strcspn(message, "\n")] = '\0';

        // Send message to server
        if (sendto(sockfd,
                   message,
                   strlen(message),
                   0,
                   (const struct sockaddr *)&servaddr,
                   sizeof(servaddr)) < 0)
        {
            perror("sendto failed");
            break;
        }

        // If client says bye
        if (strcmp(message, "bye") == 0)
        {
            printf("Chat ended.\n");
            break;
        }

        // Receive server response
        n = recvfrom(sockfd,
                     buffer,
                     MAXLINE - 1,
                     0,
                     (struct sockaddr *)&servaddr,
                     &len);

        if (n < 0)
        {
            perror("recvfrom failed");
            break;
        }

        // Add string terminator
        buffer[n] = '\0';

        printf("Server: %s\n", buffer);

        // If server says bye
        if (strcmp(buffer, "bye") == 0)
        {
            printf("Server ended the chat.\n");
            break;
        }
    }

    // Close socket
    close(sockfd);

    return 0;
}
