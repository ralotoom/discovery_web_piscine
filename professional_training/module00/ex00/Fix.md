--- `Fix.md`:
```markdown
# Vulnerability Remediation (Fix)
To secure the application against Cross-Site Scripting (XSS), implement proper input sanitization and output encoding on the server side (e.g., inside `index.html` or backend rendering scripts).
## 1. Output Encoding
Convert special characters to their corresponding HTML entities before rendering user input back to the DOM:
- `&` becomes `&amp;`
- `<` becomes `&lt;`
- `>` becomes `&gt;`
- `"` becomes `&quot;`
- `'` becomes `&#x27;`

## 2. Example (JavaScript / Frontend Sanity)
Avoid using innerHTML with raw user input. Instead, use safe text assignment properties:
```javascript
// Unsafe:
element.innerHTML = userInput;

// Safe:
element.textContent = userInput;
