class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def mask(s):
            return ''.join(['_' if c in 'aeiou' else c for c in s.lower()])
        original = set(wordlist)
        capt = dict()
        verror = dict()
        res = []
        
        for w in wordlist:
            lw = w.lower()
            nw = mask(w)
            if lw not in capt:
                capt[lw] = w
            if nw not in verror:
                verror[nw] = w
        
        for q in queries:
            lw = q.lower()
            nw = mask(q)
            if q in original:
                res.append(q)
            elif lw in capt:
                res.append(capt[lw])
            elif nw in verror:
                res.append(verror[nw])
            else:
                res.append("")
        return res