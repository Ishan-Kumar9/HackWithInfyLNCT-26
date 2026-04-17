class Solution:
    def capitalizeTitle(self, title: str) -> str:
        sent = title.split()
        for i in range(len(sent)):
            if len(sent[i]) <= 2:
                sent[i] = sent[i].lower()
            else:
                sent[i] = sent[i].capitalize()
        res = " ".join(sent)
        return res