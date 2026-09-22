---------------------------------------
---                                 ---
---             IN Mac              ---
---                                 ---
---------------------------------------
cd ~/prj/python/obsidian-bookreading
$ python3 -m venu .venv
$ souce .venv/bin/activate
$ python --version
$ code .
$ python -m pytest -s       ; -m run a module such as pytest -s show print outputs

Real Test:
$ export OBSIDIAN_VALUT="/Users/jalil/MEGAsync/Documents/Obsidian/کتابخوانی"
$ pythest -m obsidian_readingbook.search CMB
OR without export
$ pythest -m obsidian_readingbook.search CMB "/Users/jalil/MEGAsync/Documents/Obsidian/کتابخوانی"
OR
nano ~/.zshrc
export OBSIDIAN_VALUT="/Users/jalil/MEGAsync/Documents/Obsidian/کتابخوانی"


---------------------------------------
---                                 ---
---             IN Boox             ---
---                                 ---
---------------------------------------
copy prj files from Mac to ~/storage/shared/MegaSyncFiles/prj/reading with out .venv .git .pytest_cache
$ nano ~/.bashrc
export OBSIDIAN_VALUT="/storage/emulated/0/MegaSyncFiles/کتابخوانی"
$ source ~/.bashrc
$ mkdir ~/venvs
$ python -m venv ~/venvs/bookreading
$ source ~/venvs/bookreading/bin/activate
$ pythest -m obsidian_readingbook.search CMB

