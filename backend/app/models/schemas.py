from pydantic import BaseModel


class AnalysisRequest(BaseModel):
    media_url: str
    description: str | None = None


class AnalysisResult(BaseModel):
    result: str
