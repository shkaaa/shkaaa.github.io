

def canSeePersonCount(heights):
    answer = [0] * len(heights)
    right = 0, 0
    stack = []
    for right in range(len(heights)):
    # 常规单调栈的模板
        while stack and heights[stack[-1]] < heights[right]:
            idx = stack.pop() # 出现了比 idx 更高的人
            answer[idx] += 1
            # 多了一个比stack[-1] 更高的人
        if stack:
            answer[stack[-1]] += 1
        stack.append(right)
    return answer

print(canSeePersonCount([1,2,3,4,5,6]))

            