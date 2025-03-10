import requests
import time
from .config import get_config
from .utils.logger import log_error

_last_request_time = 0

def optimized_request(method, url, **kwargs):
    global _last_request_time
    config = get_config()

    url = config["base_url"] + url if not url.startswith("http") else url

    while time.time() - _last_request_time < config["anti_flood"]:
        time.sleep(0.1)

    for attempt in range(config["max_retries"]):
        try:
            response = requests.request(method, url, timeout=config["timeout"], **kwargs)
            _last_request_time = time.time()

            if response.status_code >= 500:
                log_error(f"[SERVER ERROR] {response.status_code} - Attempt {attempt + 1}")
            elif response.status_code == 404:
                log_error("[ERROR 404] Resource not found")
                return None
            elif response.status_code == 403:
                log_error("[ERROR 403] Forbidden access")
                return None
            elif response.status_code >= 400:
                log_error(f"[ERROR {response.status_code}] Client request issue")

            return response

        except requests.exceptions.Timeout:
            log_error(f"[TIMEOUT] Request timed out - Attempt {attempt + 1}")
        except requests.exceptions.ConnectionError:
            log_error("[ERROR] Connection failed")
        except Exception as e:
            log_error(f"[UNKNOWN ERROR] {e}")

    return None
