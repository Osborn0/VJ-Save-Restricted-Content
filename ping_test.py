import os

def test_connection():
    result = os.popen("ping -c 3 ac-azylfst-shard-00-00.mxnt38b.mongodb.net").read()
    print("=== PING RESULT ===")
    print(result)
    print("===================")

test_connection()
