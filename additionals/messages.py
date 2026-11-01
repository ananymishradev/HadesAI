import json
import urllib.request

# Prepare request
data = json.dumps(
    {
        "model": "qwen3:0.6b",
        "messages": [
            {
                "role": "user",
                "content": "What is the capital of India?"
            }
        ]
    }
).encode("utf-8")

# Post request to the API endpoint
req = urllib.request.Request(
    url="http://localhost:11434/api/chat/",
    data=data,
    headers={"Content-Type": "application/json"}
)

# Parse response
with urllib.request.urlopen(req) as response:
    result = json.loads(response.read())

# Print the response
print(result["choices"][0])
