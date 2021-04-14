# TrollFactory

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/be2f935c44f04d4c94b97ea5cfc8e44f)](https://www.codacy.com/gh/stanislawowski/TrollFactory/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=stanislawowski/TrollFactory&amp;utm_campaign=Badge_Grade)
[![License](https://img.shields.io/github/license/stanislawowski/TrollFactory.svg)](https://github.com/stanislawowski/TrollFactory)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/stanislawowski/TrollFactory)
![GitHub last commit](https://img.shields.io/github/last-commit/stanislawowski/TrollFactory)

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
