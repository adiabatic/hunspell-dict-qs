# hunspell-dict-qs

[Hunspell][]-compatible dictionary for [Quikscript][].

## Hacking

If you want to check for duplicate lines in BBEdit or TextWrangler, I use the following pattern:

<blockquote><code><pre>^([^/]*)(/?)([^/]*)$</pre></code></blockquote>

I then match using specific subsets — \1. Duplicates get shunted to a new document so I can check and resolve differences between, say, foo, foo/z, and foo/zvs.

[hunspell]: http://hunspell.sourceforge.net/
[quikscript]: http://en.wikipedia.org/wiki/Quikscript
