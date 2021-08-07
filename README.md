# TrollFactory

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/be2f935c44f04d4c94b97ea5cfc8e44f)](https://www.codacy.com/gh/stanislawowski/TrollFactory/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=stanislawowski/TrollFactory&amp;utm_campaign=Badge_Grade)
[![License](https://img.shields.io/github/license/stanislawowski/TrollFactory.svg)](https://github.com/stanislawowski/TrollFactory)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/stanislawowski/TrollFactory)
![GitHub last commit](https://img.shields.io/github/last-commit/stanislawowski/TrollFactory)
[![PyPI version](https://badge.fury.io/py/trollfactory.svg)](https://badge.fury.io/py/trollfactory)

**Fake personality generator for the 21st century!**

## What's this?
TrollFactory is a fairly advanced fake personality generator written in Python. It aims to generate as much data about a person as possible. At the moment it only supports Polish personalities, we're finishing US dataset soon.

## Installation
TrollFactory is available as a PyPI package: `pip3 install trollfactory`

## Usage

### TrollFactory CLI
The TrollFactory PyPI package also contains TrollFactory CLI. It's currently the most reliable way of using TrollFactory.<br>
To use it, simply execute the `trollfactory` binary from your terminal emulator.


If executed without any parameters, it will generate a personality with default options (Polish dataset, female gender).

At the moment, you can specify a custom dataset and gender (support for other static properties is coming soon):<br>
`trollfactory --gender male --dataset english_us`<br>

You can also generate many personalities at once:<br>
`trollfactory --amount 10`

You can execute `trollfactory --help` to read the full help.

### Python library
After installing the TrollFactory Python package, you can use it in your scripts.
```python
import trollfactory.functions as tf
tf.generate_personality('polish', 'male')
```
The `generate_personality()` function returns a dict with generated data.

### Web interface (beta)
You can access the TrollFactory web interface under [beta.trollfactory.tk](https://beta.trollfactory.tk) domain, though it may be unstable/unreliable, as it's still in beta.
