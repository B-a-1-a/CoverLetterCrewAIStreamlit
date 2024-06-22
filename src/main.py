import os
from dotenv import load_dotenv
from crewai import Crew
from tasks import CoverLetterTasks
from agents import CoverLetterAgents
from tools import CoverLetterTools
from langchain_groq import ChatGroq
import streamlit as st

def main():
    load_dotenv()
    llm = ChatGroq(
        temperature=0.7,
        api_key=os.environ.get('GROQLLAMA370b_API_KEY'), 
        model="llama3-70b-8192"
    )
    
    st.title("Cover Letter Writer")
    st.write('--------------------------------')

    # Use Streamlit widgets for input
    job_posting_url = st.text_input("Enter Job Posting URL:")
    personal_statement = st.text_area("Enter your personal statement [edit this]:", 
                                          """Example: Sam is a seasoned leader in Software Engineering with nearly two decades of experience under his belt. 
He has demonstrated expertise in leading both remote and onsite teams and possesses deep knowledge in a variety of programming 
languages and frameworks. With an MBA and a robust foundation in artificial intelligence and data science, Sam has spearheaded 
significant technological projects and startup ventures, showcasing his capacity to foster innovation and propel industry growth. 
His skills make him perfectly suited for executive positions that demand strategic thinking and a creative, forward-thinking mindset.""")
    resume_file = st.file_uploader("Optionally upload your resume (text files only):", type=['txt'])

    generate_button = st.button("Generate Cover Letter")

    if generate_button and job_posting_url and personal_statement:
        if resume_file is not None:
            # Assuming the resume is a plain text file
            file_path = resume_file.name
            with open(file_path, "wb") as f:
                f.write(resume_file.getbuffer())
        else:
            file_path = 'Sam-Resume.txt'  # A default or example resume path

        urls = [job_posting_url]
        results = []

        for i, currurl in enumerate(urls):
            tools = CoverLetterTools(filePath=file_path, url=currurl)
            tasks = CoverLetterTasks()
            agents = CoverLetterAgents()

            research_agent = agents.job_researcher(scrape_tool=tools.scrape_tool, llm=llm)
            profile_agent = agents.personal_profiler(read_resume=tools.read_resume, llm=llm)
            writer_agent = agents.cover_letter_writer(llm=llm)

            research_task = tasks.job_posting_task(research_agent, currurl)
            profile_task = tasks.personal_profile_task(profile_agent, personal_statement, job_posting_task=research_task)
            cover_letter_task = tasks.cover_letter_crafting_task(writer_agent, job_posting_task=research_task, personal_profile_task=profile_task, url="{i}")

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
            results.append(result)
        
        for result in results:
            st.text(result)

if __name__ == "__main__":
    main()

