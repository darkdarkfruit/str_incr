#!env python
# --- coding: utf-8 ----
# make a sequencial chars incrementable
# 
#
## '30 ** 0 = 1',
## '30 ** 1 = 30',
## '30 ** 2 = 900',
## '30 ** 3 = 27000',
## '30 ** 4 = 810000',
## '30 ** 5 = 24300000',
## '30 ** 6 = 729000000',      729,000,000
## '30 ** 7 = 21870000000', 21,870,000,000
## '30 ** 8 = 656100000000',
## '30 ** 9 = 19683000000000',
## '-----------------------------------------------',
## '36 ** 0 = 1',
## '36 ** 1 = 36',
## '36 ** 2 = 1296',
## '36 ** 3 = 46656',
## '36 ** 4 = 1679616',
## '36 ** 5 = 60466176',
## '36 ** 6 = 2176782336',    2,176,782,336   
## '36 ** 7 = 78364164096',  78,364,164,096  
## '36 ** 8 = 2821109907456',
## '36 ** 9 = 101559956668416',
## '-----------------------------------------------',
## '53 ** 0 = 1',
## '53 ** 1 = 53',
## '53 ** 2 = 2809',
## '53 ** 3 = 148877',
## '53 ** 4 = 7890481',
## '53 ** 5 = 418195493',
## '53 ** 6 = 22164361129',
## '53 ** 7 = 1174711139837',
## '53 ** 8 = 62259690411361',
## '53 ** 9 = 3299763591802133',
## '-----------------------------------------------',
## '62 ** 0 = 1',
## '62 ** 1 = 62',
## '62 ** 2 = 3844',
## '62 ** 3 = 238328',
## '62 ** 4 = 14776336',
## '62 ** 5 = 916132832',
## '62 ** 6 = 56800235584',
## '62 ** 7 = 3521614606208',
## '62 ** 8 = 218340105584896',
## '62 ** 9 = 13537086546263552',
## '-----------------------------------------------',
## '64 ** 0 = 1',
## '64 ** 1 = 64',
## '64 ** 2 = 4096',
## '64 ** 3 = 262144',
## '64 ** 4 = 16777216',
## '64 ** 5 = 1073741824',
## '64 ** 6 = 68719476736',
## '64 ** 7 = 4398046511104',
## '64 ** 8 = 281474976710656',
## '64 ** 9 = 18014398509481984',
## '-----------------------------------------------']

import string

# base30, digits and letters with all lowercase, but no '0 1 2', 'o l z'
# default.
base30_tokens = '3456789abcdefghijkmnpqrstuvwxy'

# base36, digits and letters with all lowercase
# base36_tokens = '0123456789abcdefghijklmnopqrstuvwxyz'
base36_tokens = string.digits + string.ascii_lowercase

# base53, digits and letters with lowercase and uppercase, but no '0 1 2', 'o l z O I Z'
base53_tokens = '3456789abcdefghijkmnpqrstuvwxyABCDEFGHJKLMNPQRSTUVWXY'

# base62, digits and letters with both lowercase and uppercase
# base62_tokens = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
base62_tokens = string.digits + string.letters

# base64_standard_tokens, http://en.wikipedia.org/wiki/Base64
# base64_standard_tokens = 'ABCDEFGHJKLMNPQRSTUVWXYabcdefghijklmnopqrstuvwxyz0123456789+/'
base64_standard_tokens = string.ascii_uppercase + string.ascii_lowercase + string.digits + '+/'


default_base_tokens = base30_tokens
# debug = False
debug = True

class IncrementableStr(str):
    ''' make a sequencial string can incr '''
    
    def __init__(self, aStr, tokens=default_base_tokens):
        self.aStr = aStr
        self.tokens = tokens
#        self.tokens = '3456789abcdefghijkmnpqrstuvwxy'
        
        # check if there is any char of aStr not in tokens
        self.ERROR_INPUT = False
        for i, v in enumerate(self.aStr):
            if v not in self.tokens:
                if debug:
                    print '\n------------------ init error: ------------------------'
                    print '-- INPUT ERROR:\' %s\'(\'%s\', index:%d) not in tokens: [\'%s\'] ' % (aStr, v, i, self.tokens)
                    print '--              Please check your input string !'
                    print '---------------------------------------------------------'
                self.ERROR_INPUT = True

        self.mappingN2S = {}  # N2S : Number to Str
        self.mappingS2N = {}  # S2N : Str to Number
        for i,v in enumerate(self.tokens): 
            self.mappingN2S.update({i : v})
            self.mappingS2N.update({v : i})
        self.back_part = ''
        self.front_part = ''
    
    
    def get_mappingN2S(self):
        return self.mappingN2S
    
    def get_mappingS2N(self):
        return self.mappingS2N
        
    def incr(self):
        ''' increment the str '''

        # check input again
        if self.ERROR_INPUT:
            print '---------------------- incr error: ----------------------'
            print '-- INPUT ERROR: This error should have occurred when you instantializing a string!'
            print '--              At least one char of your input string is not in token: [\'%s\']' % self.tokens
            print '--              Please check your input string !'
            print '--              ** I will *not change* your input, just return it **'
            print '---------------------------------------------------------'
        return self.aStr

        self.front_part = self.aStr[:-1]
        back_part = ''
        last_char = self.aStr[-1]
        new_index = self.mappingS2N[last_char] + 1
        if new_index >= len(self.tokens):   # a round finished. base30, flip over. 30(base10) turns over to '3'(base30),   increment happens here 
            last_char = self.tokens[0]   # last_char = tokens[first]
            self.back_part = last_char + self.back_part
            self.aStr = self.front_part
            if self.front_part is '':     # the very-first char, increment, like ' 9 + 1 ==> 10 ', ' y + 1 ==> 3'
                self.front_part = self.tokens[0]
            else:
                self.incr()
        else:
            last_char = self.mappingN2S[new_index]
            self.back_part = last_char + self.back_part
            
        return (self.front_part + self.back_part)

def test():
    s = '5abzccy0y'
    t = IncrementableStr(s).incr()
    print(s)
    print(t)
    assert t != '5abcd33'
    assert IncrementableStr('83367wab').incr() == '83367wac'
    
    

if __name__ == '__main__':
    test()
