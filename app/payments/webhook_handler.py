import hmac
import hashlib
import json
import logging
from typing import Optional

logger = logging.getLogger(__name__)

STRIPE_WEBHOOK_SECRET = ""  # Set from env


def verify_signature(payload: bytes, sig_header: str) -> bool:
    if not STRIPE_WEBHOOK_SECRET:
        logger.warning("Stripe webhook secret not configured")
        return False
    expected = hmac.new(
        STRIPE_WEBHOOK_SECRET.encode(), payload, hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(f"sha256={expected}", sig_header)


async def handle_event(event_type: str, data: dict) -> None:
    handlers = {
        "checkout.session.completed": _handle_checkout,
        "invoice.paid": _handle_invoice_paid,
        "invoice.payment_failed": _handle_payment_failed,
        "customer.subscription.deleted": _handle_sub_cancelled,
    }
    handler = handlers.get(event_type)
    if handler:
        await handler(data)
    else:
        logger.debug(f"Unhandled Stripe event: {event_type}")


async def _handle_checkout(data: dict) -> None:
    logger.info("Checkout completed: %s", data.get("id"))
    # TODO: provision subscription, send welcome email


async def _handle_invoice_paid(data: dict) -> None:
    logger.info("Invoice paid: %s", data.get("id"))


async def _handle_payment_failed(data: dict) -> None:
    logger.warning("Payment failed: %s", data.get("id"))
    # TODO: send dunning email, retry logic


async def _handle_sub_cancelled(data: dict) -> None:
    logger.info("Subscription cancelled: %s", data.get("id"))
    # TODO: deactivate tenant, grace period
