# what is client server architecture ?

# Client-Server Architecture

## Definition
Client-Server Architecture is a network model where a **client** requests services or resources, and a **server** provides them.

- **Client:** A device or application that sends requests.
- **Server:** A computer or application that processes requests and sends responses.

## How It Works

1. Client sends a request to the server.
2. Server receives and processes the request.
3. Server sends back the required data or response.
4. Client displays the result to the user.

## Best Example: Web Browser and Website

### Scenario
You open Google Chrome and visit `www.youtube.com`.

### Process

```text
+-------------+        Request        +-------------+
|   Client    | --------------------> |   Server    |
| (Browser)   |                       | (YouTube)   |
+-------------+                       +-------------+
       ^                                     |
       |                                     |
       +----------- Response ----------------+
```

1. Your browser (client) requests the YouTube webpage.
2. YouTube's server receives the request.
3. The server processes it and fetches the required data.
4. The server sends the webpage back to your browser.
5. The browser displays YouTube on your screen.

## Real-World Examples

| Client | Server |
|----------|----------|
| Chrome Browser | YouTube Server |
| WhatsApp App | WhatsApp Server |
| Free Fire Game | Garena Server |
| Gmail App | Google Mail Server |

## Advantages

- Centralized data management
- Better security
- Easy maintenance
- Supports multiple clients simultaneously

## Conclusion

Client-Server Architecture is a system where clients request resources and servers provide them. Most modern applications such as YouTube, WhatsApp, Gmail, and Free Fire use this architecture.