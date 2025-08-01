# iPhone Photos Sorter

## Summary

Python script to sort photos taken with an iPhone vs photos taken with other devices.

## Usage

```bash
iphotocopy --input_folder /path/to/source --output_folder /path/to/destination
```

Note: Currently this must be run with `PYTHONPATH=src uv run python -m iphotocopy -h` using `UV`

Add `--move` to move instead of copy.

Run `--help` for all CLI options:

```bash
iphotocopy --help
```

## MKDocs

Build with:

```
$ PYTHONPATH=$(pwd)/src uv run mkdocs build
```

Server with:

```
$ PYTHONPATH=$(pwd)/src uv run mkdocs serve
```

## To-do

- [ ] Package this correctly so it can easily be run without `UV`
