from crewai_tools import (
  FileReadTool,
  ScrapeWebsiteTool,
  TXTSearchTool,
)

class CoverLetterTools():
    def __init__(self, filePath: str, url: str):
        self.scrape_tool = ScrapeWebsiteTool(website_url=url)
        self.read_resume = FileReadTool(file_path=filePath)
