class hadesAI:
    """A minimal agent to learn about ai agent engineering from scratch"""
    def __init__(self, llm: LLM):
        self.llm = llm
        self.memory = None
        self.tools = None
        self.planner = None
        self.trajectory = Trajectory()

    def run(self, task: str) -> str:
        """Run the agent on a track"""
        self.trajectory.initialize(task)
        return self._step(task)
    
    def _step(self, task: str) -> str:
        """Perform a single step"""
        messages = [{ "role": "user", "content": task }]
        response = self.llm.generate(messages)
        self.trajectory.add(response)
        return response.content

    def _execute_action(self, action: str) -> str:
        """"Execute a tool action"""

        return f"Executed action: {action}"
