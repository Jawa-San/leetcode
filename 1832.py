class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

        upsent = sentence.upper()
        for char in upsent:
            if char in alphabet:
                alphabet.discard(char)

        if alphabet:
            return False
        return True
