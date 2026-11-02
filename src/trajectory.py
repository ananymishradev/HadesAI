from dataclasses import dataclass, field

from src.llm import Response


@dataclass
class Step:
    """One step of an agent run: thought, action + observation, or answer."""
    thoughts: str = ""
    metadata: dict = field(default_factory=dict)
    action: dict | str | None = None
    observation: str | None = None
    answer: str | None = None


class Trajectory:
    """Records agent execution as a sequence of runs"""
    def __init__(self) -> None:
        self.runs: list[dict] = []

    def initialize(self, query: str) -> None:
        """Register a new run with the query"""
        self.runs.append({"query": query, "steps": []})

    def add(self, response: Response, observation: str | None = None) -> None:
        """Record a step from the Response, optionally with an observation."""

        # add thought
        step = Step(
            thoughts=response.reasoning or "",
            metadata=response.metadata,
        )

        # add action + observation, or answer
        if observation is not None:
            step.action = response.tool_call
            step.observation = observation
        else:
            step.answer = response.content

        self.runs[-1]["steps"].append(step)
