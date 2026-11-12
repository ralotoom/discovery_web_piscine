## Overview
This document provides a comprehensive analysis of Server-Side Request Forgery (SSRF) and Local File Inclusion (LFI) vulnerabilities identified within the Exercise 02 web application. It outlines the underlying mechanics of these flaws, their impact according to OWASP guidelines, and how they interact to allow unauthorized access to server resources.

## Vulnerability Breakdown

### 1. Server-Side Request Forgery (SSRF)
- **Definition:** SSRF occurs when a web application fetches a remote resource based on a user-supplied URL without properly validating or restricting the target destination.
- **Mechanism:** The application acts as a proxy, executing HTTP or URI scheme requests on behalf of the client. When input validation is absent, an attacker can manipulate the request to target internal microservices, loopback interfaces (`127.0.0.1`), or alternative URI handlers.

### 2. Local File Inclusion (LFI) via URI Schemes
- **Definition:** LFI vulnerabilities allow an attacker to read files on the local server file system through the application.
- **Mechanism:** In this scenario, the fetch mechanism supports URI schemes such as `file://`. When supplied with a local file path (e.g., `file:///etc/passwd`), the server-side parser resolves the URI protocol and retrieves local file contents directly instead of making an outbound HTTP request.

## OWASP Categorization & Risk Impact

According to the OWASP Top 10 guidelines:
- **SSRF (A10:2021):** SSRF vulnerabilities occur when web applications fetch remote resources without validating user-supplied URLs. They allow attackers to bypass network firewalls, access internal administrative portals, or leak internal credentials.
- **Impact in this Exercise:** By utilizing the `file://` scheme, the combination of SSRF and insecure file handling exposes sensitive operating system files (such as `/etc/passwd`), leading to critical Information Disclosure and compromising server confidentiality.
