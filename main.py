import argparse
import json
import os
from search_agent import TavilyProvider
from summarizer import summarise_results, extract_skills, clean_text

OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def run(company: str, role: str, limit: int = 3, outpath: str = None):
    prov = TavilyProvider()
    # Company overview search
    comp_q = f"{company} company overview size domain latest news"
    comp_hits = prov.search(comp_q, max_results=limit, topic="news")
    # Role search
    role_q = f"{role} job description {company} responsibilities qualifications skills experience salary"
    role_hits = prov.search(role_q, max_results=limit)

    if comp_hits and comp_hits[0].get("url"):
        try:
            comp_content = prov.extract(comp_hits[0]["url"])
            comp_hits[0]["content"] = comp_content
        except Exception:
            pass

    aggregated = {
        "company": {
            "name": company,
            "search_results": comp_hits
        },
        "role": {
            "title": role,
            "search_results": role_hits
        }
    }

    # Summaries
    company_summary = summarise_results(comp_hits)
    role_summary = summarise_results(role_hits)

    output = {
        "aggregated": aggregated,
        "company_summary": company_summary,
        "role_summary": role_summary,
        "meta": {"generated_at": __import__("time").ctime()}
    }

    outpath = outpath or os.path.join(OUTPUT_DIR, f"{company}_{role}.json".replace(" ", "_"))
    with open(outpath, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
        
    print(json.dumps(output, indent=2, ensure_ascii=False))
    print(f"Wrote summary to {outpath}")
    return output

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--company", required=True)
    parser.add_argument("--role", required=True)
    parser.add_argument("--limit", type=int, default=3)
    parser.add_argument("--output", default=None)
    args = parser.parse_args()
    run(args.company, args.role, limit=args.limit, outpath=args.output)