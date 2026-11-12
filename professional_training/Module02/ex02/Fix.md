# Exercise 02 - Fixing the CBC Bit-Flipping Vulnerability

## 1. Introduction

The application uses AES-128-CBC without verifying the integrity of encrypted identity information.

This creates a risk of CBC Bit-Flipping attacks.

## 2. Security Fixes

### 2.1 Use Authenticated Encryption

Replace unauthenticated CBC encryption with authenticated encryption such as AES-256-GCM.

### 2.2 Verify Data Integrity

Verify the authentication tag before trusting decrypted information.

Modified or unauthenticated data must be rejected.

### 2.3 Keep Identity on the Server

Store user identity and administrator permissions in a trusted server-side session.

Never trust client-controlled values to determine administrator privileges.

### 2.4 Secure Random Generation

Use random_bytes() instead of rand() when generating security-sensitive random values.

### 2.5 Secure Password Storage

Use password_hash() to store passwords and password_verify() to verify them.

### 2.6 Secure Session Management

- Use HttpOnly cookies.
- Use Secure cookies over HTTPS.
- Use SameSite protection.
- Regenerate session IDs after login.
- Invalidate sessions after logout.

### 2.7 Prevent SQL Injection

Use prepared statements instead of directly inserting user input into SQL queries.

## 3. Conclusion

The application should use authenticated encryption and trusted server-side authorization.

These measures prevent unauthorized manipulation of encrypted identity information.

## 4. References

- OWASP Cryptographic Storage Cheat Sheet:
https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html

- PHP OpenSSL Documentation:
https://www.php.net/manual/en/function.openssl-encrypt.php

- PHP Password Hashing:
https://www.php.net/manual/en/function.password-hash.php
