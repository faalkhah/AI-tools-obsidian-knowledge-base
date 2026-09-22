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

def test_search():
    vault = Vault(VAULT_PATH)

    # results = vault.search("JALILFAAL")
    results = vault.search("CMB")

    print("\n----- Search Results ------")


    for result in results:
        # print("\n", result.title)
        # print(result.path.relative_to(vault.path))
        print(result.matched_text)

    assert len(results) > 0
    for result in results:
        assert result.match_type == "content"

def test_search_multiple_occurrences(tmp_path):
    note = tmp_path / "test.md"

    # note.write_text(
    #     "CMB is important. "
    #     "We study CMB. "
    #     "The CMB is observed.",
    #     encoding="utf-8",
    # )

    # note.write_text(
    #     "A" * 150
    #     + " CMB first occurrence. "
    #     + "B" * 150
    #     + " CMB second occurrence. "
    #     + "C" * 150
    #     + " CMB third occurrence. "
    #     + "D" * 150,
    #     encoding="utf-8",
    # )

    note.write_text(
        "First paragraph. CMB is important.\n\n"
        "Second paragraph. We study CMB in cosmology.\n\n"
        "Third paragraph. The CMB is observed everywhere.",
        encoding="utf-8",
    )
    
    vault = Vault(tmp_path)

    results = vault.search("CMB")

    print("\n")

    for result in results:
        # print("\n--- matched_text ---")
        # print(result.matched_text)
        print(            
            f"{result.title} | "
            f"occurrence={result.occurrence} | "
            f"position={result.position}"
        )

    assert len(results) == 3
    assert results[0].occurrence == 1
    assert results[1].occurrence == 2
    assert results[2].occurrence == 3

    assert results[0].position == 17

    assert results[0].position < results[1].position < results[2].position
