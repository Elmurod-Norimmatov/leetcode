# ACCEPTED

class Solution:
    def checkRecord(self, s: str) -> bool:
        cnt_absent = 0
        max_late_rate = 0
        curr_late_cnt = 0
        
        for i in s:
            if i == 'A':
                cnt_absent += 1
                if cnt_absent >= 2:
                    return False

            if i == 'L':
                curr_late_cnt += 1
                if curr_late_cnt == 3:
                    return False
            else:
                curr_late_cnt = 0
                max_late_rate = max(max_late_rate, curr_late_cnt)

        max_late_rate = max(max_late_rate, curr_late_cnt)

        return cnt_absent < 2 and max_late_rate < 3