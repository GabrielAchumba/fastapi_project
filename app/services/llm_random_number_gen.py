import random
import motor.motor_asyncio

# Simulate metric values for each LLM
async def generate_metrics_data(db, llms, metrics, num_points=1000):
    for llm in llms:
        for metric in metrics:
            data_points = [random.uniform(0.1, 1.0) for _ in range(num_points)]
            await db.simulations.insert_one({
                "llm": llm,
                "metric": metric,
                "data_points": data_points
            })

# LLM and metric definitions
llms = ["GPT-4o", "Llama 3.1 405", "Claude 3.5 Sonnet", ...]
metrics = ["TTFT", "TPS", "e2e_latency", "RPS"]

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
db = client.llm_benchmark