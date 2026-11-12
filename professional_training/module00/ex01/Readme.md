# Piscine Pro - Module 00: Exercise 01 (CSRF Challenge)

## Overview
This project demonstrates a Cross-Site Request Forgery (CSRF) vulnerability within a local web application deployed via Docker.

## What is CSRF?
Cross-Site Request Forgery (CSRF) is an attack that forces an authenticated end-user to execute unwanted actions on a web application in which they are currently logged in. CSRF specifically targets state-changing requests (such as fund transfers) because the browser automatically sends active authentication session cookies with cross-origin requests.

## Setup & Execution
1. Ensure Docker and Docker Compose are installed and running.
2. Launch the application environment:
   ```bash
   ./start.sh
   ```
3. Access the web interface in your browser:
   ```text
   http://localhost:8080
   ```

## Objective
Exploit the CSRF vulnerability without modifying the source code of the application to execute a full money transfer, reducing the current balance from $1000 to $0.