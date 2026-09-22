from dataclasses import dataclass
from pathlib import Path

@dataclass
class SearchResult:
    path: Path
    title: str
    matched_text: str
    match_type: str     # content, title بعدا emun خواهد شد
    occurrence: int     # occurrence=2 مثلا دومین تطابق
    position: int       # position=157 از کاراکتر ۱۵۷ شروع شده