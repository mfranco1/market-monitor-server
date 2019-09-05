import os

region = os.getenv("DYNAMO_DB_REGION", None)
if not region:
    host = os.getenv("DYNAMO_DB_HOST", "http://localhost:8000")
    region = None
