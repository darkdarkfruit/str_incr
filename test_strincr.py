#!env python
# --- coding: utf-8 ----
# use py.test (if not installed, pip install pytest)

import sys
path = '/fire/project/incrementable_str'
if path not in sys.path:
    sys.path.append(path)

import strincr as si

    
def test_base30():
    s1 = '5abccyy'
    s2 = '5ab'
    b30 = si.StrIncr()
    assert b30.incr(s1) == '5abcd33'
    assert b30.incr(s2) == '5ac'

def test_base36():
    s1 = '5bczzz'
    s2 = '5ab'
    b36 = si.StrIncr(si.base36_tokens)
    assert b36.incr(s1) == '5bd000'
    assert b36.incr(s2) == '5ac'

def test_base53():
    s1 = '5bcYYY'
    s2 = '5aB'
    b53 = si.StrIncr(si.base53_tokens)
    assert b53.incr(s1) == '5bd333'
    assert b53.incr(s2) == '5aC'

def test_base62():
    s1 = '5bcZZZ'
    s2 = '5aB'
    b62 = si.StrIncr(si.base62_tokens)
    assert b62.incr(s1) == '5bd000'
    assert b62.incr(s2) == '5aC'

def test_base64():
    s1 = '5bc///'
    s2 = '5aB'
    b64 = si.StrIncr(si.base64_tokens)
    assert b64.incr(s1) == '5bdAAA'
    assert b64.incr(s2) == '5aC'



if __name__ == '__main__':
    test_base30()
    test_base36()
    test_base53()
    test_base62()
    test_base64()

