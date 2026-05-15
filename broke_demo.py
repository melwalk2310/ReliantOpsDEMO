from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.post("/webhook")
async def receive_webhook(data: dict):
    print(f"[WEBHOOK] Event received: {data}")
    return {"status": "success", "message": "ReliantOps Broker received data"}

if __name__ == "__main__":
    print("Starting ReliantOps Webhook Broker Demo...")
    uvicorn.run(app, host="127.0.0.1", port=8000)
