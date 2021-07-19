from collections import deque


class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        if k == 1:
            return nums
        elif len(nums) <= k:
            return [max(nums)]
        else:
            dqu = deque()
            res = []
            # maintains deque containing index of k element
            # such that elements are in increasing order by index
            for idx in range(k):
                while dqu and nums[dqu[-1]] < nums[idx]:
                    dqu.pop()
                dqu.append(idx)
            res.append(nums[dqu[0]])

            for idx in range(k, len(nums)):

                while dqu and nums[dqu[-1]] < nums[idx]:
                    dqu.pop()
                dqu.append(idx)

                while dqu and idx - dqu[0] >= k:
                    dqu.popleft()

                res.append(nums[dqu[0]])

            return res