from fastapi import FastAPI
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from starlette.responses import Response
import logging

app = FastAPI(title="Metrics App")
logging.basicConfig(level=logging.INFO)
HITS = Counter("hits_total", "Total hits")

@app.get("/")
def root():
    logging.info("root accessed")
    HITS.inc()
    return {"ok": True}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
