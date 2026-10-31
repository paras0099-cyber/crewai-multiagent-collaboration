import os 
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM

load_dotenv()

llm = LLM(
    model="gemini/gemini-2.5-flash",
    api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0.3,
    verbose=True
)

researcher = Agent(
    role="you are a professional senior software engineer and a technical content writer",
    goal="find the top three verified facts about '{topic}'",
    backstory=(
        "You are an expert technical content writer and "
        "a senior software engineer. You have deep expertise in AI and its applications"
        "You write high-quality, well-researched, and engaging technical content"
        "You always provide factual information with proper citations and references"
    ),
    llm=llm,
    verbose=True
)

writer = Agent(
    role="you are an expert technical content writer",
    goal="you have to write bulleted list 2-paragraph post of {topic}",
    backstory=(
        "You are an expert technical content writer "
        "specializing in crafting engaging and informative content for **social media platforms**."
        "You excel at summarizing complex information into concise"
    ),
    llm=llm,
    verbose=True
)

task_research = Task(
    description="Research the {topic}. identify the top 3 verified reasons or advantages",
    expected_output="A bulleted list of top 3 verified technical facts with brief explanations",
    agent=researcher,
)

task_write = Task(
    description="using the bulleted facts provided by the researcher , write a crisp 2-paragraph summary on '{topic}'",
    expected_output="A clean 2-paragraph summary of the topic, ready to post on social media",
    agent=writer
)

my_crew = Crew(
    agents=[researcher, writer],
    tasks=[task_research, task_write],
    process=Process.sequential,
    verbose=True
)

if __name__ == "__main__":
    # The topic to interpolate into {topic} placeholders across agents and tasks
    topic_input = "Why developers are switching from Flask to FastAPI"
    print(f"\n🚀 Starting Crew with topic: '{topic_input}'\n")

    # kickoff() starts the execution pipeline and passes the input variables
    result = my_crew.kickoff(inputs={"topic": topic_input})

    # Print the finalized article produced by the writer
    print("\n" + "=" * 50)
    print("🎉 FINAL DELIVERABLE PRODUCED BY THE CREW:")
    print("=" * 50)
    print(result)
