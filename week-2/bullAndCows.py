class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        a, b = [0]*10, [0]*10
        for i in range(len(secret)):
            a[ord(secret[i]) - ord('0')] += 1
            if secret[i] == guess[i]:
                bulls += 1
                a[ord(secret[i]) - ord('0')] -= 1
            else:
                b[ord(guess[i]) - ord('0')] += 1
        for i in range(10):
            cows += b[i] if a[i]>=b[i] else a[i]
        return f'{bulls}A{cows}B'