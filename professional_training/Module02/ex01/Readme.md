
## Vulnerability Overview
Insecure Deserialization occurs when untrusted data is used to populate an object or structure within an application. In Python applications using libraries like `pickle`, deserializing user-supplied input can allow an attacker to manipulate object state and achieve Arbitrary Code Execution (ACE) or Remote Code Execution (RCE).

## Risks
* Full compromise of the underlying application server.
* Unauthorized access to sensitive system files (e.g., `/etc/passwd`).
* Execution of arbitrary system commands with the privileges of the web application user.

## Exploitation Scenarios
1. **Insecure Session Stores:** Applications that store serialized object data directly inside client-side session cookies without cryptographic verification, allowing users to modify the cookie content to inject serialized code.
2. **Background Task Queues:** Systems passing serialized Python objects across messaging queues or task managers (such as Celery or Redis) without validating input origin, enabling command injection via malicious job payloads.
