from onlineReceiptTracker import app
from onlineReceiptTracker.plugins.receiptParser import receiptParser

@app.route('/')
def index():
    return "Hello, world!"

