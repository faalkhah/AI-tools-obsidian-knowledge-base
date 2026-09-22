import argparse
import os

from .vault import Vault

def main() -> int:
    parser = argparse.ArgumentParser(description="Search an Obsidian vault") 
    parser.add_argument("query", help="Text to search for") 
    parser.add_argument( 
        "vault_path", 
        nargs="?", 
        help="Path to the Obsidian vault", 
    )

    args = parser.parse_args() 
    
    vault_path = args.vault_path or os.environ.get("OBSIDIAN_VAULT") 
    
    if not vault_path: 
        print("Vault path is not set.") 
        print("Use the second argument or set OBSIDIAN_VAULT.") 
        return 1
    
    vault = Vault(vault_path)

    if not vault.exists(): 
        print(f"Vault does not exist: {vault.path}") 
        return 1
    
    results = vault.search(args.query)

    if not results: 
        print(f'No results found for "{args.query}".') 
        return 0
    
    for result in results: 
        print(f"\n{result.title}") 
        print(result.path.relative_to(vault.path)) 
        print(result.matched_text)

    print(f"\nFound {len(results)} occurrence(s).") 
    return 0

if __name__ == "__main__": 
    raise SystemExit(main())