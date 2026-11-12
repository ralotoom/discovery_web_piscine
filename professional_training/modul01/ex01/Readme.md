
## Overview
XML External Entity (XXE) Injection occurs when XML input containing a reference to an external entity is processed by a weakly configured XML parser. This allows an attacker to interact with backend or external systems, read local files, or perform Server-Side Request Forgery (SSRF).

## Vulnerability Explanation (OWASP)
According to OWASP guidelines, XML processors are vulnerable when they evaluate external entity references defined within a Document Type Definition (DTD). When an application parses raw or untrusted XML input without disabling DTDs and external entities, the parser resolves the reference and embeds sensitive local resources into the application response.

## Impact in this Exercise
- Reading sensitive system files directly from the server, such as `/etc/passwd`.
- Bypassing input validation and application logic through malicious DTD declarations.

## References
- OWASP XML External Entity (XXE) Prevention Cheat Sheet
