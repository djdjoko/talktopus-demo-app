from fastapi import APIRouter

router = APIRouter()


@router.get("/stats")
async def get_stats():
    return {
        "active_users": 1247,
        "revenue_mtd": 48500,
        "api_calls_today": 89432,
        "error_rate": 0.02,
    }


@router.get("/export")
async def export_csv():
    # Known bug: truncates UTF-8 characters above 25MB
    return {"status": "generating"}
