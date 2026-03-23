from enum import Enum
from urllib.parse import urlencode


class Platform(Enum):
    IOS = "ios"
    ANDROID = "android"


BASE_SCHEME = "demosaas://"
FALLBACK_WEB = "https://app.example.com"


def build_deep_link(
    path: str,
    params: dict | None = None,
    platform: Platform = Platform.IOS,
) -> str:
    query = f"?{urlencode(params)}" if params else ""
    native = f"{BASE_SCHEME}{path}{query}"

    if platform == Platform.ANDROID:
        # Android: intent URI for cold-start handling
        return (
            f"intent://{path}{query}"
            f"#Intent;scheme=demosaas;package=com.example.demosaas;"
            f"S.browser_fallback_url={FALLBACK_WEB}/{path}{query};end"
        )
    return native


def notification_link(notification_type: str, resource_id: str) -> str:
    routes = {
        "task_assigned": f"tasks/{resource_id}",
        "comment_mention": f"comments/{resource_id}",
        "invoice_ready": f"billing/invoices/{resource_id}",
        "report_generated": f"reports/{resource_id}",
    }
    path = routes.get(notification_type, f"notifications/{resource_id}")
    return build_deep_link(path)
