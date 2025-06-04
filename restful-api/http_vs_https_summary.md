
# HTTP vs HTTPS

## Differences between HTTP and HTTPS

| Aspect            | HTTP                                               | HTTPS                                               |
|-------------------|----------------------------------------------------|-----------------------------------------------------|
| Encryption        | No encryption; data is sent in plain text          | Data is encrypted using SSL/TLS                    |
| Security          | Vulnerable to eavesdropping and tampering          | Secure; protects data from being intercepted       |
| Default Port      | 80                                                 | 443                                                 |
| Certificate       | No certificate required                            | Requires SSL/TLS certificate                        |
| Typical Use       | Non-sensitive websites                             | Websites handling sensitive data (login, banking)   |

---

# HTTP Request & Response Structure

## Request Example:
```
GET /index.html HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0
Accept: text/html
```

## Response Example:
```
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 1234

<html>...</html>
```

### Key Components in a Request:
- **Method:** Action to perform (e.g., GET, POST)
- **Path:** Resource being requested
- **Headers:** Additional info like browser type

### Key Components in a Response:
- **Status Code:** Outcome of the request (e.g., 200, 404)
- **Headers:** Info about the content (type, length)
- **Body:** Actual data returned

---

# Common HTTP Methods

| Method  | Description             | Use Case                                 |
|---------|-------------------------|------------------------------------------|
| GET     | Retrieves data          | Fetch a webpage or read from an API      |
| POST    | Sends data to create    | Register a new user or upload a file     |
| PUT     | Updates existing data   | Edit a user's profile                    |
| DELETE  | Removes a resource      | Delete a post or account                 |

---

# Common HTTP Status Codes

| Code | Description           | Scenario                                      |
|------|-----------------------|-----------------------------------------------|
| 200  | OK - Successful       | Page loads successfully                       |
| 201  | Created               | A new user was successfully registered        |
| 400  | Bad Request           | Sent incomplete or malformed data             |
| 404  | Not Found             | Trying to access a missing page or endpoint   |
| 500  | Internal Server Error | Server crashed or encountered an error        |
