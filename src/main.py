import os
from dotenv import load_dotenv
from crewai import Crew
from tasks import CoverLetterTasks
from agents import CoverLetterAgents
from tools import CoverLetterTools
from langchain_groq import ChatGroq



def main():
    load_dotenv()
    llm = ChatGroq(
        temperature=0,
        api_key=os.environ.get('GROQLLAMA370b_API_KEY'), 
        model = "llama3-70b-8192"
    )
    
    print("## Welcome to the Cover Letter Writing Crew")
    print('-------------------------------')
    # file_path = input("Enter path to the file containing Experiences and Other Info: \n")
    # personal_statement = input("Enter Personal Statement: \n")
    job_posting_url = input("Enter Job Posting URL: \n")

    file_path = 'Sam-Resume.txt'
    personal_statement =  """Sam is a seasoned leader in Software Engineering with nearly two decades of experience under his belt. 
    He has demonstrated expertise in leading both remote and onsite teams and possesses deep knowledge in a variety of programming 
    languages and frameworks. With an MBA and a robust foundation in artificial intelligence and data science, Sam has spearheaded 
    significant technological projects and startup ventures, showcasing his capacity to foster innovation and propel industry growth. 
    His skills make him perfectly suited for executive positions that demand strategic thinking and a creative, forward-thinking mindset. """
    #job_posting_url = ''
    # Build UI Later


    tools = CoverLetterTools(filePath=file_path, url=job_posting_url)
    tasks = CoverLetterTasks()
    agents = CoverLetterAgents()

    
    # create agents
    research_agent = agents.job_researcher(scrape_tool = tools.scrape_tool, llm=llm)
    profile_agent = agents.personal_profiler(read_resume = tools.read_resume, llm=llm)
    writer_agent = agents.cover_letter_writer(llm=llm)
    
    # create tasks
    research_task = tasks.job_posting_task(research_agent, job_posting_url)
    profile_task = tasks.personal_profile_task(profile_agent, personal_statement, job_posting_task = research_task)
    cover_letter_task = tasks.cover_letter_crafting_task(writer_agent, job_posting_task = research_task, personal_profile_task = profile_task)
    
    
    crew = Crew(
      agents=[
        research_agent,
        profile_agent,
        writer_agent
      ],
      tasks=[
        research_task,
        profile_task,
        cover_letter_task,
      ]
    )

    result = crew.kickoff()
    print(result)

    
if __name__ == "__main__":
    main()