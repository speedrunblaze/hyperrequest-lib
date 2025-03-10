_config = {
    "base_url": "",
    "max_retries": 3,
    "timeout": 5,
    "anti_flood": 0.5,
}

def configure(base_url: str, max_retries: int = 3, timeout: int = 5, anti_flood: float = 0.5):
    global _config
    _config.update({
        "base_url": base_url.rstrip("/"),
        "max_retries": max_retries,
        "timeout": timeout,
        "anti_flood": anti_flood,
    })

def get_config():
    return _config
