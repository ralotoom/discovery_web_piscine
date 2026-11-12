# Exercise 02 - CBC Bit-Flipping Attack

## 1. Vulnerability Type

The identified vulnerability is CBC Bit-Flipping Attack.

It occurs because the application uses AES-128-CBC encryption without verifying the integrity and authenticity of the initialization vector (IV).

## 2. Vulnerable Code

The vulnerable code is located in src/index.php.

The application uses:

- AES-128-CBC.
- A hardcoded encryption key.
- A token cookie containing the IV.
- PHP sessions to store encrypted identity information.

The test_identity() function decrypts the identity using the IV received from the browser.

## 3. How the Vulnerability Works

CBC decryption of the first block follows:

P1 = D(K, C1) XOR IV

Changing the IV can modify the corresponding bytes of the decrypted plaintext.

The application trusts the decrypted identity when deciding whether a user is an administrator.

If the identity equals admin, the application sets:

$_SESSION['isadmin'] = true;

## 4. Root Cause

1. CBC encryption does not provide integrity by itself.
2. The application accepts an IV from a client-controlled cookie.
3. The application does not authenticate the IV before decryption.
4. Authorization depends on the decrypted identity.

## 5. Security Impact

An attacker may manipulate the decrypted identity and potentially escalate privileges from guest to admin.

This could expose administrator-only information.

## 6. Exploitation Scenarios

### Scenario 1: Privilege Escalation

An attacker manipulates the IV used by the application. If the decrypted identity becomes admin, the application may grant administrator privileges.

### Scenario 2: Unauthorized Role Manipulation

In another application using unauthenticated CBC-encrypted role information, an attacker may manipulate decrypted role values and potentially access unauthorized functionality.

## 7. Recommended Protection

- Use authenticated encryption such as AES-GCM.
- Verify authentication tags before trusting decrypted information.
- Keep identity and permissions in a trusted server-side session.
- Use cryptographically secure random generation.
- Protect session cookies.
- Verify authorization on every protected operation.

## 8. References

- OWASP Cryptographic Storage Cheat Sheet:
https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html

- PHP OpenSSL Documentation:
https://www.php.net/manual/en/function.openssl-encrypt.php
