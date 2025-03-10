import requests
from .manager import optimized_request

def enable_interceptor():
    requests.get = lambda url, **kwargs: optimized_request("GET", url, **kwargs)
    requests.post = lambda url, **kwargs: optimized_request("POST", url, **kwargs)
    requests.put = lambda url, **kwargs: optimized_request("PUT", url, **kwargs)
    requests.delete = lambda url, **kwargs: optimized_request("DELETE", url, **kwargs)
