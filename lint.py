#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
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

class L(object):
    def __str__(self):
        return str(dict(word=latinize(self.word),
                        extras=latinize(self.extras),
                        po=self.po,
                        comment=self.comment,
                        error=self.error))

def latinize(s):
    """
        r = ''
        for ch in s:
            if ch in M:
                r += M[ch]
            else:
                r += ch
        return r
    """
    return s.translate(str.maketrans(M))
def parse_line(l):
    r = L()
    r.word = ''
    r.extras = ''
    r.po = ''
    r.comment = ''
    r.error = False
        
    slashlist = l.split('/', 1)
    if len(slashlist) == 1: # "abc" or "abc po:verb" or "abc # …" or "abc po:verb # …"
        spacelist = slashlist[0].split(' ', 1)
        if len(spacelist) == 1: # "abc"
            r.word = spacelist[0]
        elif len(spacelist) == 2: # "abc po:verb" or "abc # …" or "abc po:verb # …"
            r.word = spacelist[0]
            if spacelist[1].startswith('po:'):
                pol = spacelist[1].split(' ', 1)
                if len(pol) == 1:
                    r.po = spacelist[1]
                elif len(pol) == 2:
                    r.po = spacelist[1]
                    if pol[1].startswith('#'):
                        r.comment = pol[1]
            elif spacelist[1].startswith('#'):
                r.comment = spacelist[1]
                
            r.tail = spacelist[1]
    elif len(slashlist) == 2: #"abc/z" or "abc/z po:verb" or "abc/z po:verb # …"
        r.word = slashlist[0]
        spacelist = slashlist[1].split(' ', 1)
        r.extras = spacelist[0]
        if len(spacelist) == 2:
            if spacelist[1].startswith('po:'):
                pol = spacelist[1].split(' ', 1)
                if len(pol) == 1:
                    r.po = spacelist[1]
                elif len(pol) == 2:
                    r.po = spacelist[1]
                    if pol[1].startswith('#'):
                        r.comment = pol[1]
            elif spacelist[1].startswith('#'):
                r.comment = spacelist[1]
    
    r.word = r.word.strip()
    r.extras = r.extras.strip()
    r.po = r.po.strip()
    r.comment = r.comment.strip()
    return r

for line in fileinput.input(FILENAME):
    if fileinput.isfirstline(): continue # skip the line with the line-count estimate
    i = fileinput.filelineno()
    
    l = parse_line(line)
        
    if l.error:
        print(l.error)
        break
    
    # p. 18: terminal -es, -ed
    # TBI
    
    # p. 18: terminal -ing
    if l.word.endswith('\ue670\ue664') and not ('noun' in l.po):
        print('{}:{}:Final -ing with preceding •it: {}'.format(FILENAME, i, latinize(l.word)))

    # p. 19: terminal -al, el, -le, il
    # Generally, omit any _unstressed_ vowel sound between the L and the preceding consonant
    if l.word.endswith('\ue667'):
        print('{}:{}:Final -l with preceding (unstressed?) vowel: {}'.format(FILENAME, i, latinize(l.word)))
        
    
    #print(l)
    
