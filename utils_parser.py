import pdfplumber, docx, io, re

def extract_text_from_pdf(file_bytes: bytes) -> str:
    out = []
    with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
        for p in pdf.pages:
            text = p.extract_text()
            if text:
                out.append(text)
    return "\n".join(out)

def extract_text_from_docx(file_bytes: bytes) -> str:
    document = docx.Document(io.BytesIO(file_bytes))
    return "\n".join(p.text for p in document.paragraphs)

def extract_text_from_file(filename: str, file_bytes: bytes) -> str:
    lower = filename.lower()
    if lower.endswith(".pdf"):
        return extract_text_from_pdf(file_bytes)
    if lower.endswith(".docx") or lower.endswith(".doc"):
        return extract_text_from_docx(file_bytes)
    try:
        return file_bytes.decode("utf-8", errors="ignore")
    except:
        return ""

def parse_jd_simple(jd_text: str) -> dict:
    """Heuristic parser: extract must-have and good-to-have skills from JD."""
    lines = [ln.strip() for ln in jd_text.split("\n") if ln.strip()]
    must, good = [], []
    for ln in lines:
        low = ln.lower()
        if "must" in low or "required" in low:
            must.extend([s.strip() for s in re.split(r"[,:;]", ln) if s.strip()])
        elif "good" in low or "preferred" in low or "nice" in low:
            good.extend([s.strip() for s in re.split(r"[,:;]", ln) if s.strip()])
    return {
        "title": lines[0] if lines else "Unknown",
        "must": must,
        "good": good,
        "raw": jd_text,
    }
