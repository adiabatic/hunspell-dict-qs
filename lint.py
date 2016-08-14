#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import fileinput

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
    M[k] = "•" + v + " "

class L(object):
    def __str__(self):
        if self.word and self.extras:
            return latinize(self.word) + "/" + latinize(self.extras)
        return latinize(self.word)

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
        
    if l.startswith('#'):
        r.comment = l
        return r
        
    for i, ch in enumerate(l):
        if ch != '/' or ch != ' ':
            r.word += ch
        else:
            if ch == '/':
                for j, chh in enumerate(l[i:]):
                    if chh != ' ':
                        r.extras += chh
            if ch == ' ':
                break
    
    return r

for line in fileinput.input('en_QS.dic'):
    if fileinput.isfirstline(): continue # skip the line with the line-count estimate
    i = fileinput.filelineno()
    
    l = parse_line(line)
    print(l)
    if l.error:
        print(l.error)
        break
