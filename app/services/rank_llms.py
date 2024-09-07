from fastapi import FastAPI, Query
import motor.motor_asyncio

app = FastAPI()

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
db = client.llm_benchmark

@app.get("/rankings/{metric}")
async def get_rankings(metric: str):
    pipeline = [
        {"$match": {"metric": metric}},
        {"$project": {"llm": 1, "avg_score": {"$avg": "$data_points"}}},
        {"$sort": {"avg_score": 1}}
    ]
    results = await db.simulations.aggregate(pipeline).to_list(length=10)
    return results