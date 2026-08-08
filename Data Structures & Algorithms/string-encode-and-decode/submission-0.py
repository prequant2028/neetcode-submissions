class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for n in strs:
            res+=str(len(n))
            res+="#"
            res+=n
        return res

    def decode(self, s: str) -> List[str]:
        m=list(s)
        cur_num=0
        res=[]
        i=0
        while i<len(m):
            try:
                cur_num=cur_num*10+int(m[i])
                i+=1
            except:
                if m[i]=="#":
                    word = s[i+1:i+1+cur_num]
                    res.append(word)
                    i+=cur_num+1
                    cur_num=0
        return res