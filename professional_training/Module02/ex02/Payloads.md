Exercise 02 — Payloads and Test Results
1. Test Environment

Application: Local training application
URL: http://127.0.0.1:8085/
Vulnerability: CBC Bit-Flipping Attack
Encryption Algorithm: AES-128-CBC

The application was tested in a local Docker environment.

A test account was created to verify the normal authentication functionality.

Username: labuser
Password: LabPass123!

SQL Injection was not used.

2. Payload 1 — Baseline Authentication Test

Purpose: Verify that normal authentication works correctly before security testing.

Input:

Username: labuser
Password: LabPass123!

Procedure:

Open the application in a browser.
Enter the test username.
Enter the test password.
Click the Login button.
Observe the application response.

Observed Result:

The application displayed:

text
you are in!
Hello Nice to see you!
Log out


Conclusion:

Normal authentication was successful.

The user was authenticated, but administrator privileges were not demonstrated.

Status: Successfully tested.

3. Payload 2 — CBC IV Bit-Flipping Test

Purpose: Investigate whether modifying the Initialization Vector (IV) can change the decrypted identity.

The application uses AES-128-CBC encryption.

CBC decryption of the first plaintext block follows:

P1 = D(K, C1) XOR IV

The IV influences the first decrypted plaintext block.

If the IV is modified, the decrypted plaintext may also change.

Target Identity:

Original identity: guest
Target identity: admin

Security Observation:

The application retrieves the IV from the client-controlled token cookie and does not authenticate it before decryption.

This creates a potential CBC bit-flipping vulnerability.

Expected Security Behavior:

A secure application should reject modified or unauthenticated encrypted data.

Observed Result:

The normal authentication test succeeded.

A successful privilege escalation through IV manipulation has not yet been independently verified.

Status: Vulnerability identified in the source code; practical exploitation requires verification.

4. Payload 3 — Invalid Data Control Test

Purpose: Examine how the application handles invalid or modified encryption data.

Procedure:

Use a local test session.
Observe the application's response to invalid authentication data.
Check whether the application rejects the data.
Record any error or unexpected behavior.

Expected Result:

The application should reject invalid or unauthenticated data without granting additional privileges.

Observed Result:

No verified result has been recorded for this test yet.

Status: Pending practical verification.

5. Exploitation Scenarios
Scenario 1 — Privilege Escalation

An attacker may manipulate an unauthenticated IV used during CBC decryption.

If the application trusts the modified plaintext as an administrator identity, unauthorized administrator access may become possible.

Scenario 2 — Unauthorized Role Manipulation

In another application that stores user roles inside unauthenticated CBC-encrypted data, an attacker may manipulate decrypted role information.

If the application trusts the modified role without independent authorization checks, restricted functionality may become accessible.

These scenarios describe potential security impacts and are not both confirmed exploits against this particular application.

6. Test Summary
Test	Result
Normal authentication	Successful
CBC IV vulnerability analysis	Identified in source code
Practical privilege escalation	Not yet verified
Invalid data handling	Pending verification
7. Conclusion

The baseline authentication test was successful.

Source-code analysis identified a potential CBC Bit-Flipping vulnerability caused by the absence of integrity and authenticity verification for encrypted identity information.

Authenticated encryption, secure IV generation, and server-side authorization checks are recommended to protect the application.

8. References
OWASP Cryptographic Storage Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html
PHP OpenSSL Documentation: https://www.php.net/manual/en/function.openssl-encrypt.php
CWE-649: https://cwe.mitre.org/data/definitions/649.html


