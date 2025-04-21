import os

def test_connection():
    result = os.popen("curl -I https://ac-azylfst-shard-00-00.mxnt38b.mongodb.net:27017").read()
    print("=== CURL RESULT ===")
    print(result)
    print("===================")

test_connection()
