from base64 import b64decode, b64encode
from Crypto.Cipher import AES
from Crypto import Random
from flask import Flask, request 
from lxml import etree
import cgi
import os
import traceback

app = Flask(__name__)

@app.route('/')
def index():
    return """
    <html>
    <head><title>Vulnerable Flask App: XXE</title></head>
    <body>
        <p><h3>Functions</h3></p>
        <a href="/xml">Parse XML</a><br>
    </body>
    </html>
    """

@app.route('/xml', methods=['POST', 'GET'])
def xml():
    parsed_xml = None
    errormsg = ''
    
    html = """
    <html>
      <body>
    """
    
    if request.method == 'POST':
        xml = request.form['xml']
        parser = etree.XMLParser(no_network=False, resolve_entities=True) # to enable network entity. see xmlparser-info.txt
        try:
            doc = etree.fromstring(str(xml), parser)
            parsed_xml = etree.tostring(doc)
            print repr(parsed_xml)
        except:
            print "Cannot parse the xml"
            html += "Error: Bad format\n<br>\n" #+ traceback.format_exc()
    if (parsed_xml):
        html += "Result:\n<br>\n" + cgi.escape(parsed_xml)
    else:
        html += """
          <form action = "/xml" method = "POST">
             <p><h3>Enter xml to parse</h3></p>
             <textarea class="input" name="xml" cols="40" rows="5"></textarea>
             <p><input type = 'submit' value = 'Parse'/></p>
          </form>
        """
    html += """
      </body>
    </html>
    """
    return html



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('APP_PORT', 5000)))
