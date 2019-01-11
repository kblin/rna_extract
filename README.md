Extract RNA features from sequences identified by NCBI GenBank ID
=================================================================

Shaun (@sjackman) [was asking](https://twitter.com/sjackman/status/1083062091366293504)
for a script to download tRNAs and rRNAs for a sequence identified by NCBI GenBank ID.

While this violates the requirements of "curl to Entrez or E-utilities" as only dependency,
I just wanted to show how easy this task is with a bit of Python.

Installation
------------

```bash
git clone https://github.com/kblin/rna_extract.git && cd rna_extract
# recommended: create/activate a python virtualenv here (using virtualenv or conda)
pip install -r requirements.txt
```

Usage
-----

```
./rna_extract.py NC_003888 > my_rnas.fa
```

You can use the `--reuse` flag to skip donloading GenBank files that already exist in your
current directory.


License
-------

This script is licensed under the Apache 2 license.
See [`LICENSE`](LICENSE) for details.
