import json
import urllib.request
from dataclasses import dataclass, field


@dataclass
class Response:
    """The parsed result of one LLM call."""
    content: str = ""
    reasoning: str = ""
    tool_call: dict | None = None
    metadata: dict = field(default_factory=dict)


class LLM:
    def __init__(
        self,
        model: str,
        base_url: str = "http://localhost:11434/v1",
        api_key: str = "no_key",
        think: bool = False, 
    ):
        """Initialize the LLM with the given model."""
        self.model = model
        self.base_url = base_url
        self.api_key = api_key
        self.think = think

    def generate(
        self, messages: list[dict], tools: list | None = None
    ) -> Response:
        """Generate a response from the LLM given a list of messages."""
        # build the request body
        body = {
            "model": self.model,
            "messages": messages,
        }
        if tools is not None:
            body["tools"] = tools

        # post request to the OpenAI-compatible endpoint
        req = urllib.request.Request(
            url=f"{self.base_url}/chat/completions",
            data=json.dumps(body).encode("utf-8"),
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_key}",
            },
            method="POST",
        )

        # parse the openai-shaped response
        with urllib.request.urlopen(req) as res:
            result = json.loads(res.read())

        choice = result["choices"][0]
        message = choice["message"]

        tool_call = None
        if message.get("tool_calls"):
            fn = message["tool_calls"][0]["function"]
            tool_call = {
                "name": fn["name"],
                "arguments": json.loads(fn.get("arguments") or "{}"),
            }

        return Response(
            content=message.get("content") or "",
            reasoning=message.get("reasoning") or message.get("reasoning_content") or "",
            tool_call=tool_call,
            metadata={
                "model": result.get("model"),
                "finish_reason": choice.get("finish_reason"),
                "usage": result.get("usage"),
            },
        )