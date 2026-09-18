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