from obsidian_bookreading.vault import Vault

VAULT_PATH = "/Users/jalil/MEGAsync/Documents/Obsidian/کتابخوانی"
    
# def test_real_vault():
#     vault = Vault(VAULT_PATH)

#     assert vault.exists()

#     files = vault.markdown_files()

#     print(f"\nFound {len(files)} markdown files")

#     assert len(files) > 0

def test_vault_exists():
    vault = Vault(VAULT_PATH)

    assert vault.exists()

def test_read_note():
    vault = Vault(VAULT_PATH)

    content = vault.read("Concepts/Physics/CMB.md")

    print("\n----- CMB.md -----")
    print(content)

    assert "CMB" in content
