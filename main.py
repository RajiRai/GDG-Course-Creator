from agents.library import ResearcherAgent, JudgeAgent
from schemas.models import CourseOutline

def run_course_creator(topic):
    researcher = ResearcherAgent()
    judge = JudgeAgent()
    
    # 1. THE RESEARCH LOOP (Loop Agent Pattern)
    attempts = 0
    validated_research = None
    
    while attempts < 3:
        research = researcher.run(topic)
        status = judge.evaluate(research)
        if "PASS" in status:
            validated_research = research
            break
        attempts += 1
    
    # 2. THE SEQUENTIAL PIPELINE (Sequential Agent Pattern)
    if validated_research:
        print("Research validated. Handing off to Content Builder...")
        # Call ContentBuilderAgent here...
        return "Course Generated Successfully."
    
    return "Failed to meet quality standards."

if __name__ == "__main__":
    run_course_creator("Agentic AI Infrastructure")
