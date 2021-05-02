from fastapi import FastAPI


app = FastAPI()


@app.get('/')
async def hello():
    return {"text": "hello world!"}

@app.get("/countup/round{round}")
async def render_countup_round(round):
    return {"round": round}