from fastapi import FastAPI
from code.app.routers import expenses, stats

app = FastAPI(title="Expense Tracker API")

app.include_router(expenses.router)
app.include_router(stats.router)


@app.get("/")
def root():
    return {"status": "ok"}