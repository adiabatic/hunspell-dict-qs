#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

# Everyone says "who watches the watchers?", but who spell-checks the spell-checkers?

import fileinput

FILENAME = 'en_QS.dic'
M = {
    '\ue650': 'pea',
    '\ue651': 'bay',
    '\ue652': 'tea',
    '\ue653': 'day',
    '\ue654': 'key',
    '\ue655': 'gay',
    '\ue656': 'thaw',
    '\ue657': 'they',
    '\ue658': 'fee',
    '\ue659': 'vie',
    '\ue65a': 'see',
    '\ue65b': 'zoo',
    '\ue65c': 'she',
    '\ue65d': 'zhivago',
    '\ue65e': 'cheer',
    '\ue65f': 'jay',
    '\ue660': 'ye',
    '\ue661': 'way',
    '\ue662': 'he',
    '\ue663': 'why',
    '\ue664': 'oolong',
    '\ue665': 'may',
    '\ue666': 'no',
    '\ue667': 'low',
    '\ue668': 'roe',
    '\ue669': 'loch',
    '\ue66a': 'llan',
    '\ue66b': 'excite',
    '\ue66c': 'exam',
    '\ue66d': '(unused)',
    '\ue66e': '{left angled paren}',
    '\ue66f': '(right angled paren)',
    '\ue670': 'it',
    '\ue671': 'eat',
    '\ue672': 'et',
    '\ue673': 'eight',
    '\ue674': 'at',
    '\ue675': 'I',
    '\ue676': 'ah',
    '\ue677': 'awe',
    '\ue678': 'ox',
    '\ue679': 'oy',
    '\ue67a': 'utter',
    '\ue67b': 'out',
    '\ue67c': 'owe',
    '\ue67d': 'foot',
    '\ue67e': 'ooze',
    '\ue67f': '(also unused)'
}

for k, v in M.items():
    M[k] = "•" + v

VOWELS = set(chr(x) for x in range(0xe670, 0xe67e+1))
VOWELS_AND_SEMIVOWELS = VOWELS.union(set('\ue660'))

class L(object):
    def __str__(self):
        return str(dict(word=latinize(self.word),
                        extras=latinize(self.extras),
                        po=self.po,
                        comment=self.comment,
                        error=self.error))

def latinize(s):
    return s.translate(str.maketrans(M))

def parse_line(l):
    r = L()
    r.word = ''
    r.affixes = ''
    r.partofspeech = '' # po:noun
    r.stem = '' # feet st:foot is:plural
    r.allomorphs = [] # sing al:sang al:sung; sang st:sing; sung st:sing
    r.inflectionalsuffixes = [] # feet st:foot is:plural
    r.comment = ''
    r.error = False
    
    # see also: `man 5 hunspell, "optional data fields"`
    
    xs = l.split()
    if '/' in xs[0]: (r.word, r.affixes) = xs[0].split('/')
    else:             r.word = xs[0]
    for i in range(1, len(xs)):
        x = xs[i]
        if x.startswith('po:'):
            r.partofspeech = x[3:]
        elif x.startswith('st:'):
            r.stem = x[3:]
        elif x.startswith('al:'):
            r.allomorphs.append(x[3:])
        elif x.startswith('is:'):
            r.inflectionalsuffixes.append(x[3:])
        elif x.startswith('#'):
            x = x[1:].strip()
            r.comment = ' '.join(xs[i:])
        
    return r

for line in fileinput.input(FILENAME):
    if fileinput.isfirstline(): continue # skip the line with the line-count estimate
    i = fileinput.filelineno()
    
    l = parse_line(line)
        
    if l.error:
        print(l.error)
        break
    
    # p. 18: terminal -es, -ed
    # AFAICT these are entirely handled with the •zoo and •day suffixes in the .aff file.
    if False and l.word.endswith('\ue65b'): # •zoo
        if l.word.endswith('\ue67a\ue65b'): # •utter •zoo
            print('{}:{}: Final •zoo with preceding •utter: {}'.format(FILENAME, i, latinize(l.word)))            
    
    # p. 18: terminal -ing
    if l.word.endswith('\ue670\ue664') and not ('noun' in l.partofspeech):
        print('{}:{}: Final -ing with preceding •it: {}'.format(FILENAME, i, latinize(l.word)))

    # p. 19: terminal -al, el, -le, il
    # • Generally, omit any _unstressed_ vowel sound between the L and the preceding consonant,
    #   as in "triba̷l", "fina̷l", "ora̷l", "offici̷a̷l", "rifle̷", "devi̷l"
    # • Where another syllable is added, the vowel sound before this L must be pronounced and spelt
    #   in most cases, as in "fina̲lly", "ora̲lly", "officia̲lly", "devi̲lry"
    # • Ls don't need a vowel before the •ye in "Spaniel", but you need an •utter before •low in
    #   "burial", "visual", and "loyal".
    if l.word.endswith('\ue667'): # •low
        if False and len(l.word) >=2 and l.word[-2] in VOWELS: # lots of false positives
            print('{}:{}: Final -l with preceding (unstressed?) vowel: {}'.format(FILENAME, i, latinize(l.word)))
        if len(l.word) >= 3 and \
           l.word[-2] in {'\ue67a': '•utter'}.keys() and \
           l.word[-3] not in VOWELS and \
           "utter-low-ok" not in l.comment:
            print('{}:{}: Final -l with preceding •utter: {}'.format(FILENAME, i, latinize(l.word)))
    
    # p. 19: terminal -tion, -ssion, -shion, -cean, -sion, -gion, -ation, -asion.
    # - omit the vowel
    # p. 19: terminal -en, -on.
    # Written invariably as •utter•no; no contraction, no alternatives.
    # [implementer’s note: how in blazes is a modern English speaker supposed to differentiate between the two without referencing Orthodox? I’m tempted to codify “always elide the •utter”, but then I’d be overstepping my bounds as a dictionary author…]
    
    # p. 19: terminal -ent, -ant, -ence, -ance
    # written invariably with standard •utter•no followed by a penlift
    if l.word.endswith('\ue672\ue666\ue652'):
        print('{}:{}: ends with •et•no•tea; prefer •utter•no•tea: {}'.format(FILENAME, i, latinize(l.word)))    
    #print(l)
    
