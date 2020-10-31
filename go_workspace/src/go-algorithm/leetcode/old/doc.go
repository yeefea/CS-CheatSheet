package leetcode

/*
给定[left,right] inclusive,二等分数组[left,mid],[mid+1,right],要计算mid

以下4种写法是一样的,后2种比较好
(left+right)/2
(left+right)>>1
left+(right-left)/2
left+(right-left)>>1

[0]			=> mid=0 => [0],[]
[0,1]		=> mid=0 => [0],[1]
[0,1,2]		=> mid=1 => [0,1],[2]
[0,1,2,3]	=> mid=1 => [0,1],[2,3]
[0,1,2,3,4]	=> mid=2 => [0,1,2],[3,4]

左边的长度>=右边的长度
*/

/*
树和图深度优先遍历要用到栈，广度优先遍历要用到队列
*/
