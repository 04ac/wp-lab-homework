class ReverseString:
    def reverse_words(self, s: str) -> str:
        return ' '.join(s.split()[::-1])

rs = ReverseString()
print(rs.reverse_words("Hello World"))
