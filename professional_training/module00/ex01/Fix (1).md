# Vulnerability Remediation (Fixing CSRF)

To effectively secure the web application against Cross-Site Request Forgery (CSRF), the following defensive mechanisms must be implemented:

## 1. Anti-CSRF Tokens (Synchronizer Token Pattern)
* Generate a unique, unpredictable, and cryptographically secure token for each user session/request.
* Embed this token inside submitted forms as a hidden field.
* On the server side, validate the submitted token against the session token before executing state-changing operations. Requests without a valid token are rejected.

## 2. SameSite Cookie Attributes
Configure session cookies with the `SameSite` attribute set to `Strict` or `Lax`:
```http
Set-Cookie: session_id=xyz123; Secure; HttpOnly; SameSite=Strict
```
* **Strict:** Prevents the browser from sending session cookies in all cross-site requests.
* **Lax:** Restricts cookies from being sent in cross-site state-changing POST requests.

## 3. Mandatory Re-Authentication & Custom Headers
* Require users to enter their current password or a One-Time Password (OTP) before performing sensitive financial transactions.
* Utilize custom request headers (e.g., `X-Requested-With`) via AJAX/Fetch calls, which cross-origin HTML forms cannot forge without explicit CORS permissions.