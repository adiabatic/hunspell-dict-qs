# hunspell-dict-qs

[Hunspell][]-compatible dictionary for [Quikscript][].


## Usage

I usually copy text to the clipboard, run `$ pbpaste | hunspell -d en_QS | pbcopy`, and then paste the spell-check results into a new document. `pbpaste` is built into OS X, while `hunspell` comes from [homebrew](http://brew.sh/).


## Hacking

If you want to check for duplicate lines in BBEdit or TextWrangler, I use the following pattern:

<code><pre>^([^/]*)(/?)([^/\s]*)(\s*.*)$</pre></code>

I then match using the specific subsets “\1 \4”. Duplicates get shunted to a new document so I can check and resolve differences between, say, foo, foo/z, and foo/zvs.

[hunspell]: http://hunspell.sourceforge.net/
[quikscript]: http://en.wikipedia.org/wiki/Quikscript

## License

[CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/).
