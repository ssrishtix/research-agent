from typing import List, Dict, Any, Optional
from config import TAVILY_API_KEY

try:
    from tavily import TavilyClient
except Exception:
    TavilyClient = None

class TavilyProvider:
    def __init__(self, api_key: Optional[str] = None):
        key = api_key or TAVILY_API_KEY
        if TavilyClient is None:
            raise RuntimeError("tavily-python SDK not installed or import failed.")
        if not key:
            raise RuntimeError("TAVILY_API_KEY not provided.")
        self.client = TavilyClient(api_key=key)

    def search(self, query: str, max_results: int = 5, topic: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Returns normalized list of results: {title, url, snippet, content (optional)}
        """
        params = {"max_results": max_results}
        if topic:
            params["topic"] = topic
        resp = self.client.search(query, **params)
        results = []
        for r in resp.get("results", [])[:max_results]:
            results.append({
                "title": r.get("title") or r.get("headline") or "",
                "url": r.get("url") or r.get("link") or "",
                "snippet": r.get("snippet") or r.get("summary") or "",
                "content": r.get("content") or r.get("text") or ""
            })
        return results

    def extract(self, url: str) -> str:
        """Return cleaned text/content for a given url (uses Tavily extract)"""
        resp = self.client.extract(url)
        if isinstance(resp, dict):
            return resp.get("content") or resp.get("text") or ""
        return str(resp)
