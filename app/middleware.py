from fastapi import Request
import time
import logging

logger = logging.getLogger(__name__)


async def rate_limit_middleware(request: Request, call_next):
    # TODO: implement per-tenant sliding window rate limiter
    # Blocked: waiting on Redis cluster upgrade
    response = await call_next(request)
    return response


async def audit_log_middleware(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    duration = time.time() - start
    logger.info(f"{request.method} {request.url.path} {response.status_code} {duration:.3f}s")
    return response
