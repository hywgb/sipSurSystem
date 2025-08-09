from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/ai", tags=["ai"])


class QARequest(BaseModel):
    conversation_id: str | None = None
    question: str


class QAResponse(BaseModel):
    answer: str
    sources: list[str] = []


class SummaryRequest(BaseModel):
    conversation_id: str


class SummaryResponse(BaseModel):
    summary: str


class QCRequest(BaseModel):
    conversation_id: str


class QCResponse(BaseModel):
    score: float
    findings: list[str] = []


@router.post("/qa", response_model=QAResponse)
def knowledge_qa(req: QARequest) -> QAResponse:
    # TODO: integrate RAG pipeline
    return QAResponse(answer="[placeholder]", sources=[])


@router.post("/summary", response_model=SummaryResponse)
def summarize(req: SummaryRequest) -> SummaryResponse:
    # TODO: integrate summarization
    return SummaryResponse(summary="[placeholder summary]")


@router.post("/quality", response_model=QCResponse)
def quality_check(req: QCRequest) -> QCResponse:
    # TODO: integrate quality/complianace checks
    return QCResponse(score=0.0, findings=["[placeholder]"])