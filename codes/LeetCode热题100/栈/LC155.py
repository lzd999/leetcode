"""
思路：
比较直观的做法是在维护栈的同时额外维护一个存放最小值的小顶栈：
调用 push 则将当前元素入栈，同时比较当前元素和小顶栈栈顶元素大小，小则入小顶栈；
调用 pop 则将当前元素出栈，同时弹出小顶栈栈顶元素；
调用 getMin 则直接返回小顶栈栈顶元素。
可以将当前元素与最小值元素合并为一个元组，这样在调用 getMin 时，直接返回元组中第二个元素即可。
"""

from math import inf


class MinStack:
    def __init__(self):
        # self.st = []
        # self.min_st = [inf]
        self.st = []

    def push(self, x: int) -> None:
        # self.st.append(x)
        # self.min_st.append(min(x, self.min_st[-1]))
        if not self.st:
            self.st.append((x, x))
        else:
            self.st.append((x, min(x, self.st[-1][1])))

    def pop(self) -> None:
        # self.st.pop()
        # self.min_st.pop()
        self.st.pop()

    def top(self) -> int:
        # return self.st[-1]
        return self.st[-1][0]

    def getMin(self) -> int:
        # return self.min_st[-1]
        return self.st[-1][1]
