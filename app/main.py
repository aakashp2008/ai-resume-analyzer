from fastapi import FastAPI, File, Form, HTTPException, UploadFile

from .models import AnalysisResponse
from .services.resume_parser import extract_text_from_pdf
from .services.matching_engine import analyze_resume


app = FastAPI(
    title="AI Resume Analyzer",
    description="Analyze a resume against a job description.",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "AI Resume Analyzer API",
        "version": "1.0.0",
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.post("/analyze", response_model=AnalysisResponse)
async def analyze(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    if not resume.filename:
        raise HTTPException(
            status_code=400,
            detail="Resume file is required."
        )

    if not resume.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF resumes are supported."
        )

    if not job_description.strip():
        raise HTTPException(
            status_code=400,
            detail="Job description cannot be empty."
        )

    pdf_bytes = await resume.read()

    if not pdf_bytes:
        raise HTTPException(
            status_code=400,
            detail="Uploaded resume is empty."
        )

    try:
        resume_text = extract_text_from_pdf(pdf_bytes)
    except Exception as error:
        raise HTTPException(
            status_code=400,
            detail="Unable to read the PDF file."
        ) from error

    if not resume_text.strip():
        raise HTTPException(
            status_code=400,
            detail="Could not extract text from the PDF."
        )

    result = analyze_resume(
        resume_text,
        job_description
    )

    return {
        "filename": resume.filename,
        **result
    }
