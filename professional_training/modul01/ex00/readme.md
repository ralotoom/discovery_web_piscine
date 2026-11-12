
## Overview
Server-Side Template Injection (SSTI) occurs when an application embeds user-supplied input directly into a template engine rather than passing it safely as data. This allows an attacker to inject malicious template expressions that get evaluated and executed by the server.

## Vulnerability Explanation (OWASP)
According to OWASP guidelines[span_1](start_span)[span_1](end_span), template engines are designed to generate dynamic web pages by combining static templates with data models. When an application unsafely concatenates or evaluates raw user input directly inside the template rendering function, the engine treats the input as executable code instead of plain text.

## Impact in this Exercise
- Bypassing application logic restrictions through template syntax.
- Accessing internal objects to read sensitive system files directly from the server, such as `/etc/passwd`[span_2](start_span)[span_2](end_span).


