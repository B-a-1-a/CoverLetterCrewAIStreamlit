from textwrap import dedent
from crewai import Task

class CoverLetterTasks():
    def job_posting_task(self, agent, url: str):
        return Task(
            description=dedent(f"Analyze the job posting URL provided {url} "
            "to extract key technical skills, experiences, and qualifications required. Also, if present, gather information about responsibilities of the role. "
            "Finally take a note of any communication skills, leadership skills, soft-skills or company mission/values. " 
            "Use the scraping tool to gather content and identify and categorize the requirements."),   
            expected_output=dedent("""4 Things: 
                                1. A highly detailed and comprehensive structured list of job requirements, including necessary skills, qualifications, and experiences.
                                2. A detailed description of the responsibilities of the role.
                                3. A list of company values and soft skills.
                                4. Any other relevant information extracted from the job posting URL."""),
            agent=agent
        )
  
    def personal_profile_task(self, agent, writup: str, job_posting_task: Task):
        return Task(
            description=dedent(f"Compile a detailed personal and professional profile using the file with experiences, and the following personal writup (if it is provided): {writup}, "
                               "Make sure to include all skills, experiences, projects, contributions, interests, and soft skills. You do not have to search for any other information, "
                               "just write the best profile."
                               ),   
            expected_output=dedent("A comprehensive profile document that includes skills, project experiences, contributions, interests, and soft skills."),
            agent=agent
        )
    
    def cover_letter_crafting_task(self, agent, job_posting_task: Task, personal_profile_task: Task, url: str):
        return Task(
                description=dedent(
                            "Using the personal profile and job requirements obtained from "
                            "previous tasks, write a cover letter to highlight the most "
                            "relevant areas. Employ tools to adjust and enhance the "
                            "cover letter content. Make sure this is the best cover letter and be sure glamorize and project the desired values, "
                            "but do not embellish or lie. Include proper introduction, "
                            "emphasize relevant experiences and skills, relate to soft skills and company values. "
                            "All to better reflect the candidates abilities and how it matches the job posting."
                ),
                expected_output=dedent("""A clean coverletter that effectively highlights the candidate's skills and traits relevant to the job."""),
                output_file= f"item{url}.txt",
                context = [job_posting_task, personal_profile_task],
                agent=agent
            )

#print("CoverLetterTasks class loaded")