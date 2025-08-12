import re
from typing import List, Dict

COMMON_SKILLS = [
    "python","sql","aws","gcp","azure","pytorch","tensorflow","scikit-learn",
    "nlp","docker","kubernetes","mlops","pandas","numpy","git","rest","spark",
    "java","c++","javascript","react","nodejs"
]

SALARY_RE = re.compile(r"(\₹|Rs\.?|INR|\$|USD|€|£)\s?[0-9,]+(?:\s?(?:k|K|lakhs|LPA|per year|/year|pa))?", re.IGNORECASE)
EXP_RE = re.compile(r"(\d+(?:\.\d+)?\+?)\s*(?:years|yrs|y)\b", re.IGNORECASE)

def clean_text(text: str) -> str:
    t = re.sub(r"\s+", " ", text or "")
    t = re.sub(r"\s*[\n\r]\s*", " ", t)
    return t.strip()

def extract_skills(text: str):
    t = (text or "").lower()
    found = set()
    for s in COMMON_SKILLS:
        if s in t:
            found.add(s)
    extras = re.findall(r"(?:experience with|proficient in|familiar with|knowledge of)\s+([a-z0-9\-\+\.\s,/]{2,60})", t)
    for e in extras:
        parts = re.split(r",|/| and | & ", e)
        for p in parts:
            p = p.strip()
            if 2 <= len(p) <= 40:
                found.add(p)
    return sorted(found)

def extract_experience(text: str):
    m = EXP_RE.search(text or "")
    return m.group(0) if m else None

def extract_salary(text: str):
    m = SALARY_RE.search(text or "")
    return m.group(0) if m else None

def summarise_results(results: List[Dict]) -> Dict:
    """
    Aggregate results and produce a minimal summary:
      - combined_snippet: joined snippets
      - detected_skills / experience / salary
      - top_urls
    """
    combined = " ".join((r.get("snippet") or r.get("content") or "") for r in results)
    cleaned = clean_text(combined)
    skills = extract_skills(cleaned)
    exp = extract_experience(cleaned)
    sal = extract_salary(cleaned)
    urls = [r.get("url") for r in results if r.get("url")]
    return {
        "combined_snippet": cleaned[:2000],
        "skills_detected": skills,
        "experience_detected": exp,
        "salary_detected": sal,
        "top_urls": urls
    }
