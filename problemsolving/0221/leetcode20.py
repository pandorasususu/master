#20.Valid Parentheses
#stack 개념에 대해서 완전히 모른 상태에서 접근하니 수십번의 시도 동안 계속 틀림
#양치기 보다는 개념의 중요성을 깨닫게 됨.
class Solution:
    def isValid(self, s: str) -> bool:
        ans = []
        start = ['(', '{', '[']
        end = [')', '}', ']']
        cnt_list = [0] * 3

        for i in range(len(s)):
            if s[i] == '\"':
                continue
            else:
                if s[i] in start:
                    ans.append(s[i])
                else:
                    if len(ans) == 0:
                        return False
                    else:
                        last = ans.pop()
                        if start[end.index(s[i])] != last:
                            return False
        else:
            if len(ans) != 0:
                return False
            else:
                return True
