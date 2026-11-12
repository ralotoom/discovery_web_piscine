from flask import Flask, request
import os
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return """
    <html>
    <head><title>SSRF + LFI Example</title></head>
    <body>
        <h1>SSRF + LFI Example</h1>
        <form method="GET" action="/fetch">
            <label for="url">Enter URL:</label>
            <input type="text" id="url" name="url">
            <button type="submit">Fetch URL</button>
        </form>
        <div id="content"></div>
    </body>
    </html>
    """

@app.route('/fetch', methods=['GET'])
def fetch():
    url = request.args.get('url')
    if url:
        try:
            if url.startswith('file:///'):
                file_path = url[7:]  # Remove "file:///" prefix
                if os.path.exists(file_path):
                    file_content = open(file_path, 'r').read()
                    return """
                    <html>
                    <head><title>SSRF + LFI Result</title></head>
                    <body>
                        <h1>SSRF + LFI Result</h1>
                        <div>Content fetched from URL:</div>
                        <pre>{}</pre>
                    </body>
                    </html>
                    """.format(file_content)
                else:
                    return "File not found"
            else:
                response = requests.get(url, allow_redirects=False)
                content = response.text
                return """
                <html>
                <head><title>SSRF + LFI Result</title></head>
                <body>
                    <h1>SSRF + LFI Result</h1>
                    <div>Content fetched from URL:</div>
                    <pre>{}</pre>
                </body>
                </html>
                """.format(content)
        except Exception as e:
            return "Error fetching content: {}".format(str(e))
    else:
        return "Please provide a URL."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)