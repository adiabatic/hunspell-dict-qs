# hunspell-dict-qs

[Hunspell][]-compatible dictionary for [Quikscript][].


## Usage

I usually copy text to the clipboard, run `$ pbpaste | hunspell -d en_QS | pbcopy`, and then paste the spell-check results into a new document. `pbpaste` is built into OS X, while `hunspell` comes from [homebrew](http://brew.sh/).


## Pragmas

I use lint.py to make sure that I’m not accidentally violating spelling rules in Read’s own manual. I use pragmas in the comments to tell the automated linter that some constructions, in some words, are OK. These are:

- utter-low-ok — this word ends in •utter•low, and that’s OK
- et-no-tea-ok (e.g. “spent”)
- et-no-see-ok
- may-utter-ok (e.g. “demon”)


## Hacking

If you want to check for duplicate lines in BBEdit or TextWrangler, I use the following pattern:

<code><pre>^([^/]*)(/?)([^/\s]*)(\s*.*)$</pre></code>

I then match using the specific subsets “\1 \4”. Duplicates get shunted to a new document so I can check and resolve differences between, say, foo, foo/z, and foo/zvs.

[hunspell]: http://hunspell.sourceforge.net/
[quikscript]: http://en.wikipedia.org/wiki/Quikscript

## License

[CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/).
