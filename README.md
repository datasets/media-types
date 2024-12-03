<a className="gh-badge" href="https://datahub.io/core/media-types"><img src="https://badgen.net/badge/icon/View%20on%20datahub.io/orange?icon=https://datahub.io/datahub-cube-badge-icon.svg&label&scale=1.25" alt="badge" /></a>

This dataset lists all the Media Types (MIME types), Media Subtypes, and their file extensions.

## Data

The details of the Media Types and Media Subtypes are taken from the [official registry of Media Types](http://www.iana.org/assignments/media-types/media-types.xhtml) maintained by IANA. The extension details are taken [the website](https://github.com/apache/httpd/blob/trunk/docs/conf/mime.types) of the Apache Software Foundation .

## Preparation

The `media-types.csv` is processed using `scripts/process.py` script.

```
    pip install -r scripts/requirements.txt
    python scripts/process.py
```

Data was automated using Github Actions.

## License

These data are made available under the Public Domain Dedication and License v1.0 whose full text can be found at: http://www.opendatacommons.org/licenses/pddl/1.0/