# TrollFactory

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/803cfecee34f4a28a402fca70da1ed6a)](https://app.codacy.com/gh/stanislawowski/TrollFactory?utm_source=github.com&utm_medium=referral&utm_content=stanislawowski/TrollFactory&utm_campaign=Badge_Grade_Settings)
[![License](https://img.shields.io/github/license/stanislawowski/TrollFactory.svg)](https://github.com/stanislawowski/TrollFactory)

The fake personalities generator.

## Usage
`python3 trollfactory.py --sex female --amount 10 --lang polish`

## Updating submodule
```
git clone git@github.com:stanislawowski/TrollFactory.git -b production
cd TrollFactory
git submodule update --init
cd langs
git fetch
git log --oneline origin/main -3
```
After executing the last command you'll see the latest commits.<br>
Then execute: `git checkout -q <checksum>`, replacing the `<checksum>` with the latest commit's SHA.<br>
At the end, run `git add .` and commit changes.
