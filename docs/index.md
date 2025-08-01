# iphotocopy

**iphotocopy** is a command-line utility for sorting and organizing iPhone photos.

It detects Apple-originated photos based on EXIF metadata and either **copies** or **moves** them to a specified destination directory.

---

## Features

- Detects photos taken with Apple devices using EXIF metadata.
- Supports both **copy** and **move** modes.
- Clean CLI interface with standard Python tooling.
- Easily extendable and well-tested.

---

## Quickstart

```bash
uv venv
source .venv/bin/activate
uv pip install -e .
```

Then:

```bash
iphotocopy --input_folder /path/to/source --output_folder /path/to/destination
```

Add `--move` to move instead of copy.
