class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n <= 1:
            return s

        def check_palindrome(s, start, end):
            """
            s[start:end+1]이 대칭단어인지 아닌지 판별
            :param s:
            :param start:
            :param end:
            :return:
            """
            word = s[start:end + 1]
            if word == word[::-1]:
                return True
            return False
            # for i in range((end-start+1)//2):
            #    if s[start+i] != s[end-i]:
            #        return False
            # return True

        section = [0, 1]  # idx 0 만 추가
        for i in range(n - 1):
            for j in range(i + 1, n):
                if j + 1 - i > section[1] - section[0] and check_palindrome(s, i, j):
                    section = [i, j + 1]
        return s[section[0]:section[1]]