from flask import Flask
app = Flask(__name__)

import onlineReceiptTracker.views

if __name__=="__main__":
    app.run()
