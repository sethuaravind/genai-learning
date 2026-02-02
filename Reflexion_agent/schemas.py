from typing import List
from langchain_core.pydantic_v1 import BaseModel, Field


class Reflection:
    missing: str = Field(description='Critique of what is missing')
    superfluous: str = Field(description='Critique of what is superfluous')

class AnswerQuestion:
    "Answer the question"
    answer: str = Field(description='~250 words detailed answer to the questions')
    reflection: Reflection = Field(description='Your reflection on initial answers')
    search_queries: List[str] = Field(description='1-3 search queries for researching improvements to address the critiques of current answers')