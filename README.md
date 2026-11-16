# Algo-lab

算法学习仓库：笔记、模板、题解。

## 目录

| 路径 | 内容 |
|------|------|
| `算法笔记.md` | 基础技巧 / 搜索 / 贪心 / 数据结构 / 动态规划 / 数论，附哈希表考试要点 |
| `模板/` | 15 个纯函数模板，无依赖 |
| `洛谷/` `Codeforces/` `LeetCode/` `DLU-Hydro/` | 各平台题解，文件名即题号 |
| `Practice/` | 随手练习 |

## 模板

| 文件 | 主要函数 |
|------|----------|
| `输入输出.py` | 各类读入与输出写法对照 |
| `二分.py` | `lower_bound` `upper_bound` `binary_search` `binary_answer_min` `binary_answer_max` |
| `前缀和差分.py` | `build_prefix` `range_sum` `build_prefix_2d` `rect_sum` `add_range` `restore_diff` |
| `排序.py` | 多关键字排序、逆序对 |
| `DFS模板.py` | `permutations` `combinations` `subsets` `grid_dfs` |
| `BFS.py` | `bfs_shortest` `flood_fill` `bfs_1d` |
| `背包.py` | `knapsack01` `knapsack_complete` `knapsack_count` `knapsack01_2d` |
| `LIS.py` | `lis_n2` `lis_nlogn` `lis_nonstrict` |
| `埃氏筛.py` | `build_primes` `is_prime` |
| `试除法.py` | `is_prime` |
| `数论.py` | `gcd` `lcm` `fast_pow` `factorize` `divisor_count` `divisor_sum` |
| `组合数.py` | `comb_table` `comb_mod` `comb_small` |
| `并查集.py` | `class DSU`（路径压缩 + 按秩合并） |
| `双指针.py` | `two_sum_sorted` `shortest_subarray_sum` `longest_unique_substring` |
| `单调栈队列.py` | `next_greater` `largest_rectangle` `sliding_max` |

## 约定

- 标准输入输出，无第三方依赖，按 Python 3.8 兼容编写。
- 读入写 `input = lambda: sys.stdin.readline().strip()`；百万级数据用 `sys.stdin.buffer.read().split()`。
- 多行输出先累积再统一写出。
- 取模只用于累加值与最终结果，不用于循环上界、数组下标和比较。
