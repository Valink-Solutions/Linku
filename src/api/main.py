from fastapi import FastAPI


app = FastAPI(
    title="Linku Backend API",
    description="Linku is a personal link shortener.",
    version="0.1.0",
)


@app.get("/public/")
async def root():
    return {"message": "Hello World"}