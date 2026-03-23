# Rate limiter — BLOCKED on Redis cluster upgrade
# DevOps ETA: Thursday
#
# Design: per-tenant sliding window using Redis sorted sets
# - Key: rate:{tenant_id}:{endpoint}
# - Score: timestamp
# - Count members in window to check limit
# - Return Retry-After header on 429

# Placeholder until Redis cluster is ready
class RateLimiter:
    def __init__(self, redis_url: str, default_limit: int = 100, window_seconds: int = 60):
        self.redis_url = redis_url
        self.default_limit = default_limit
        self.window_seconds = window_seconds

    async def check(self, tenant_id: str, endpoint: str) -> tuple[bool, int]:
        # TODO: implement with Redis sorted sets
        return True, self.default_limit
