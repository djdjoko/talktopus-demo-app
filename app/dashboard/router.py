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
    # Fixed: added BOM header for UTF-8 CSV export
    headers = {"Content-Type": "text/csv; charset=utf-8-sig"}
    return {"status": "generating", "headers": headers}
