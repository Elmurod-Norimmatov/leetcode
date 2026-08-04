# ACCEPTED

class Solution:
    def countSegments(self, s: str) -> int:
        cnt = 0
        segment_len = 0
        for i in s:
            if i == ' ':
                if segment_len != 0:
                    cnt += 1
                    segment_len = 0
            else:
                segment_len += 1

        if segment_len != 0:
            cnt += 1

        return cnt