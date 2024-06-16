class Solution(object):
    def romanToInt(self, s):
        sum = 0
        roman_numerals = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}
        priv = 0
        for i in reversed(s):
            cornv =roman_numerals[i]
            if cornv >= priv:
                sum+=cornv
                priv = cornv
            else:
                sum-=cornv
                privr = cornv
        return sum