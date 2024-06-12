class Solution:
    def lemonadeChange(self, bills):
        five_bills = 0
        ten_bills = 0

        for bill in bills:
            if bill == 5:
                five_bills += 1
            elif bill == 10:
                if five_bills == 0:
                    return False
                five_bills -= 1
                ten_bills += 1
            else:  # bill == 20
                if ten_bills > 0 and five_bills > 0:
                    ten_bills -= 1
                    five_bills -= 1
                elif five_bills >= 3:
                    five_bills -= 3
                else:
                    return False

        return True

