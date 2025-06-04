
# Using curl to Interact with APIs

## 1. Check curl installation
Run the following command to verify curl is installed:
```bash
curl --version
```
**Expected Output:** Details about the curl version and supported protocols.

---

## 2. Fetching a Web Page
Retrieve a basic web page using curl:
```bash
curl http://example.com
```
**Expected Output:** HTML content of example.com.

---

## 3. Fetch Data from JSONPlaceholder API
Use curl to retrieve posts data from the public API:
```bash
curl https://jsonplaceholder.typicode.com/posts
```
**Expected Output:** A JSON array of posts with fields like `userId`, `id`, `title`, and `body`.

---

## 4. Fetch Only HTTP Headers
Use the `-I` flag to get only the headers from the response:
```bash
curl -I https://jsonplaceholder.typicode.com/posts
```
**Expected Output:** HTTP status code and headers such as `Content-Type`, `Content-Length`, etc.

---

## 5. Make a POST Request
Use `-X` to specify the HTTP method and `-d` to send data:
```bash
curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts
```
**Expected Output:** JSON response simulating a created post, typically with an `id` of 101.

---

## Notes
- Add `| jq` at the end of a curl command (if you have jq installed) to format JSON output:
```bash
curl https://jsonplaceholder.typicode.com/posts | jq
```
- JSONPlaceholder is a fake online REST API useful for testing and prototyping.
