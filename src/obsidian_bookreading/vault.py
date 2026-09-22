from .models import SearchResult
from pathlib import Path

class Vault:
    def __init__(self, path:str | Path):
        self.path = Path(path)

    def exists(self) -> bool:
        return self.path.is_dir()
    
    def markdown_files(self) -> list[Path]:
        return list(self.path.rglob("*.md"))
    
    def read(self, file: str | Path) -> str:
        path = self.path / file
        return path.read_text(encoding ="utf-8")
    
    def paragraph_at(self, content: str, index: int) -> str:
        start = content.rfind("\n\n", 0, index)

        if start == -1:
            start = 0
        else:
            start += 2

        end = content.find("\n\n", index)

        if end == -1:
            end = len(content)

        return content[start:end].strip()    

    def search(self, query: str) -> list[SearchResult]:
        results = []

        query_lower = query.lower()

        for file in self.markdown_files():
            content = file.read_text(encoding="utf-8")
            content_lower = content.lower()

            search_start = 0
            occurrence = 0

            while True:
                index = content_lower.find(query_lower, search_start)

                if index == -1:
                    break

                occurrence += 1

                matched_text = self.paragraph_at(content, index)

                results.append(
                    SearchResult(
                        path=file,
                        title=file.stem,
                        matched_text=matched_text,
                        match_type="content",
                        occurrence=occurrence,
                        position=index,
                    )
                )

                search_start = index + len(query_lower)

        return results            
