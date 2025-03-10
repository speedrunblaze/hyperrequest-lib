import hyperrequest

hyperrequest.configure(base_url="https://example.com", max_retries=3, timeout=5)

response = requests.get("/api/data")
if response:
    print(response.text)
