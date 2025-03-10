# HyperRequest

HyperRequest is an optimized request management library that automatically handles errors, retries, anti-flood mechanisms, and more.

## Installation

```sh
pip install git+https://github.com/speedrunblaze/hyperrequest-lib.git
```

## Usage

```python
import hyperrequest

hyperrequest.configure(base_url="https://example.com", max_retries=3, timeout=5)

response = requests.get("/api/data")
if response:
    print(response.text)
```

## Features

- Auto-handles request errors (404, 500, etc.).
- Implements retry logic for failed requests.
- Prevents request flooding.
- Customizable configuration.
- Provides formatted logging.
