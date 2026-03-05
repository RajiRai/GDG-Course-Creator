from vertexai.generative_models import GenerativeModel
from schemas.models import ResearchOutput

class ResearcherAgent:
    def __init__(self):
        self.model = GenerativeModel("gemini-1.5-flash")
    
    def run(self, topic: str):
        # In production, this uses the Google Search Tool
        prompt = f"Research the topic: {topic}. Return structured facts."
        return self.model.generate_content(prompt)

class JudgeAgent:
    def evaluate(self, research_data):
        # Logic to return PASS/FAIL based on schema completeness
        if len(research_data.key_facts) < 3:
            return "FAIL: Insufficient depth."
        return "PASS"
