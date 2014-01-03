#show alert box
import easygui 
      
import pdb

import urllib2 
from urllib import urlencode
from urllib2 import urlopen

from flask import Flask,request
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])

def hello_world():
    
    if request.method == 'GET':
        return """ 
            <form action="/" method="POST">
                <br><br><br><br><br><br><br><br><br><br><br><br>
                <div align ="center">
                    <font size="5"> Url:</font> 
                    <input type="text" name="url" size="40" style="height:40px;font-size:15pt"/>
                </div>
                <br>
                <div align="center">
                    <input type="submit" id="bt_get" value="Get links" style="height:50px;width:140px;font-size:20pt"/>
                </div>
            </form>
            
            """    
            
    elif request.method == 'POST':
        """
        <script type="text/javascript">
            if (url.value.trim() == "")
                alert("Please enter something");
        </script>
        """
        from pyquery import PyQuery as pq
        try:
            d = pq(url=request.form['url'])
            return """
                    Urls: %s
                    """   % ("<br>".join([x.attrib.get('href','') for x in d('a')]))
        except urllib2.HTTPError, e1:
            print e1.msg
            print e1.headers
            print e1.fp.read()
        except pyquery.PyQuery.ValueError, e2:
            print e2.msg
            print e2.headers
            print e2.fp.read()
    else: print "Unknown method"
    
 
if __name__ == '__main__':
    app.run(debug=True)