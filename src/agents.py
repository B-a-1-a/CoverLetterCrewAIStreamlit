# Agent 1: Researcher
from textwrap import dedent
from crewai import Agent

class CoverLetterAgents():
    def job_researcher(self, scrape_tool, llm):
        return Agent(
            role="Tech Job Researcher",
            goal="Make sure to do amazing analysis on "
                "job posting to help job applicants",
            tools = [scrape_tool],
            verbose=True,
            backstory=(
                "As a Job Researcher, your prowess in "
                "navigating and extracting critical "
                "information from job postings is unmatched."
                "Your skills help pinpoint the necessary "
                "qualifications and skills sought "
                "by employers, forming the foundation for "
                "effective application tailoring."
                ), 
            llm=llm,
            allow_delegation=False
            )
  
    def personal_profiler(self, read_resume, llm):
        return Agent(
            role="Personal Profiler for Engineers",
            goal="Extract and synthesize information from a resume and writup to create a comprehensive personal profile to be used by the cover letter writer.",
            tools = [read_resume],
            verbose=True,
            backstory=(
                "Equipped with analytical prowess, you dissect "
                "and synthesize information "
                "from diverse sources to craft comprehensive "
                "personal and professional profiles."
                ), 
            llm=llm,
            allow_delegation=False
            )
    
    def cover_letter_writer(self, llm):
        return Agent(
                role="Cover Letter Strategist for Engineers",
                goal="Use information gathered to write the best cover letter stand out in the job market. You do not have to search for information, just write the best cover letter.",
                verbose=True,
                backstory=(
                    "With a strategic mind and an eye for detail, you "
                    "excel at writing coverletters to highlight the most "
                    "relevant skills and experiences, ensuring they "
                    "resonate perfectly with the job's requirements and company values."
                ), 
            llm=llm,
            allow_delegation=False
            )

#print("CoverLetterAgents class loaded")