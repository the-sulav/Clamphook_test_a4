from fastapi import FastAPI, WebSocket
from fastapi.responses import StreamingResponse
import asyncio

app = FastAPI()

async def stream_response():
    for i in range(1, 6):
        yield f"data: {i}\n\n"
        await asyncio.sleep(1)

@app.get("/stream")
async def get_stream():
    return StreamingResponse(stream_response(), media_type="text/event-stream")

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    for i in range(1, 6):
        await websocket.send_text(f"Message {i}")
        await asyncio.sleep(1)
    await websocket.close()
