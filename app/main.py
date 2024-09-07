from fastapi import FastAPI
from app.routes.user_routes import router as user_router

app = FastAPI()

# Register routes
app.include_router(user_router)

@app.get("/")
async def root():
    print("seen")
    return {"message": "Welcome to FastAPI with MongoDB!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)