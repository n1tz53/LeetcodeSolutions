class Solution:

    def trap(self, height: List[int]) -> int:

        last_height = []
        position = []
        water = 0

        for idx, height in enumerate(height):
            if not last_height or last_height[-1] >= height:
                last_height.append(height)
                position.append(idx)
            else:
                while last_height and last_height[-1] < height:
                    h = last_height.pop()
                    pos = position.pop()
                    if last_height:
                        water += (min(height, last_height[-1]) - h) * (idx - position[-1] - 1)
                last_height.append(height)
                position.append(idx)
        return water