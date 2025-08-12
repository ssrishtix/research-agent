import pytest
from summarizer import extract_skills, extract_experience, extract_salary, clean_text

def test_text_clean():
    s = "Hello\nWorld   \n"
    assert clean_text(s) == "Hello World"

def test_extract_skills():
    t = "We use Python, TensorFlow and AWS for deployments. Experience with Docker is a plus."
    skills = extract_skills(t)
    assert "python" in skills
    assert any("docker" in s for s in skills)

def test_experience_and_salary():
    t = "We expect 3-5 years experience. Salary up to $120000 per year."
    exp = extract_experience(t)
    sal = extract_salary(t)
    assert exp is not None
    assert sal is not None
