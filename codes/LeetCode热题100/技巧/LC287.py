"""
思路：
比较直观的做法是使用哈希表维护元素的出现次数，然后遍历哈希表，返回出现次数大于等于 2 的元素。
然而这种做法使用了 O(n) 的空间，不符合题意。
本题始终需要维护每个元素和对应的索引，方便知道重复元素出现在哪些位置，即建立 i -> nums[i] 的映射，
例如 nums = [1,3,4,2]，映射关系为 0 -> 1, 1 -> 3, 2 -> 4, 3 -> 2，
如果从下标 0 出发，根据映射关系可以得到这样一个序列：0 -> 1 -> 3 -> 2 -> 4 -> null，这和链表非常像。
在链表里如何找重复元素？
例如 nums = [1,3,4,2,2]，映射关系为 0 -> 1，1 -> 3，2 -> 4，3 -> 2，4 -> 2，
如果从下标 0 出发，根据映射关系可以得到序列：0 -> 1 -> 3 -> 2 -> 4 -> 2 -> 4 -> ……，
分析得知，如果数组存在重复元素，映射关系一定会存在多对一，对应序列生成的链表一定存在环！
这就转换成了 LC142.环形链表II，因此本题同样可以使用快慢指针：
1.数组中有一个重复的整数 <=> 链表中存在环
2.找到数组中的重复整数 <=> 找到链表的环入口
链表使用快慢指针与数组使用快慢指针的对应关系：
slow = slow.next <=> slow = nums[slow]
fast = fast.next.next <=> fast = nums[nums[fast]]
"""

from collections import defaultdict
from typing import List


class Solution287:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        slow = nums[slow]
        fast = nums[nums[fast]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        cur = 0
        while cur != slow:
            cur = nums[cur]
            slow = nums[slow]
        return cur

        # mp = defaultdict(int)
        # for x in nums:
        #     mp[x] += 1
        # for k, v in mp.items():
        #     if v >= 2:
        #         return k
