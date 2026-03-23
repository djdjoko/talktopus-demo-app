from fastapi import APIRouter, Request, HTTPException

router = APIRouter()


@router.post("/webhook")
async def stripe_webhook(request: Request):
    payload = await request.body()
    # TODO: verify webhook signature
    # TODO: handle checkout.session.completed, invoice.paid, etc.
    return {"received": True}
