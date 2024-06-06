from crewai_tools import (
  FileReadTool,
  ScrapeWebsiteTool,
  TXTSearchTool,
)

class CoverLetterTools():
    def __init__(self, filePath: str, url: str):
        self.scrape_tool = ScrapeWebsiteTool(website_url=url)
        self.read_resume = FileReadTool(file_path=filePath)
        #self.rag_search_resume = TXTSearchTool()

# scrape_tool = ScrapeWebsiteTool()
# read_resume = FileReadTool(file_path='./fake_resume.md')
# semantic_search_resume = MDXSearchTool(mdx='./fake_resume.md')

# print("CoverLetterTools class loaded")