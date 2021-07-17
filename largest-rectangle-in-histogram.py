class Solution:

    def largestRectangleArea(self, heights: List[int]) -> int:

        last_heights = []
        position = []
        result = 0

        for idx, height in enumerate(heights + [0]):
            # maintain stack of increasing height
            if not last_heights or last_heights[-1] <= height:
                last_heights.append(height)
                position.append(idx)
            else:
                # find the rightmost largest area possible for any height
                while last_heights and last_heights[-1] >= height:
                    h = last_heights.pop()
                    pos = position.pop()
                    result = max(result, (idx - pos) * h)
                last_heights.append(height)
                position.append(pos)

        return result
