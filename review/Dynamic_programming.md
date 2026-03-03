# 确定性动态规划（Deterministic Dynamic Programming, DDP）
## 一、文档概述（Document Overview）
本文档聚焦**确定性动态规划（Deterministic Dynamic Programming, DDP）** 的核心理论与应用，先简要介绍作业2（LP建模与AI工具结合）的完成流程、运筹趣题擂台的使用规则，再系统讲解DDP的核心定义、要素、最优性原理（Principle of Optimality）、算法步骤，通过四皇后问题、确定性调度问题、旅行商问题（TSP）等案例验证方法有效性，延伸至近似算法——滚动算法（Rollout Algorithm），最后对比确定性与随机动态规划（Stochastic DP）的差异，并补充工业工程专业就业方向参考。文档核心逻辑为“定义→原理→算法→案例→拓展”，强调DDP与最短路径问题的等价性，以及其解决组合优化问题的核心思想。


## 二、核心概念与要素（Key Concepts & Elements）
### 1. 确定性有限状态有限时域问题（Deterministic Finite State Finite Horizon Problem）
- **定义（课件原文）**：  
  _“In all dynamic programming (DP) problems, the central object is a discrete-time dynamic system that generates a sequence of states under the influence of actions or controls. The system may evolve deterministically (this course) or randomly”_  
  通俗解释：在有限的时间步（决策点）内，系统状态在决策作用下确定性演化，目标是最小化累积成本的优化问题。

- **核心要素（课件原文87页）**：
  - 时间步（Time Index/Decision Epoch）：\(t=0,1,...,T\)，\(T\)为规划时域（Planning Horizon）；
  - 状态（State, \(S_t\)）：系统在时间\(t\)的状态，\(S_t \in \mathcal{S}\)（状态空间），捕捉决策所需全部信息；
  - 决策/控制变量（Decision/Control Variable, \(x_t\)）：\(x_t \in X_t(S_t)\)（可行决策集），依赖当前状态；
  - 转移函数（Transition Function, \(f_t\)）：\(S_{t+1}=f_t(S_t,x_t)\)，_“the state \(S_{t+1}\) is determined solely by state \(S_t\) and decision \(x_t\)”_（课件原文）；
  - 成本函数（Cost Function, \(c_t\)）：\(c_t(S_t,x_t)\)，时间\(t\)的即时成本；
  - 终端成本（Terminal Cost, \(c_T\)）：\(c_T(S_T)\)，时域结束时的终端状态成本；
  - 目标函数（Objective Function）：\(V(S_0;x_0,...,x_{T-1})=c_T(S_T)+\sum_{t=0}^{T-1}c_t(S_t,x_t)\)，最小化初始状态\(S_0\)对应的总成本（课件原文）。

- **等价性（课件原文）**：  
  _“A deterministic finite state finite horizon problem is equivalent to finding a shortest path from the initial nodes of the (acyclic) graph to the terminal node”_（与最短路径问题等价）。


## 三、最优性原理（Principle of Optimality）
### 1. 核心内容（课件原文45页）
> _“Let \({x_{0}^{*}, ..., x_{T-1}^{*}}\) be an optimal control sequence, which together with \(S_0\) determines the corresponding state sequence \({S_1, ..., S_T}\). Consider the tail subproblem whereby we start at \(S_{t}^{*}\) at time \(t\) and wish to minimize the cost-to-go. Then the truncated optimal control sequence \({x_{t}^{*}, ..., x_{T-1}^{*}}\) is optimal for this tail subproblem.”_

**通俗解释**：最优决策序列的任一截断部分，对其对应的子问题（从状态\(S_t^*\)开始的后续决策）而言，仍是最优决策序列。

### 2. 核心逻辑（课件原文46-48页）
- 原问题：从\(S_0\)出发，最小化全时域累积成本；
- 子问题：从最优状态序列中的\(S_t^*\)出发，最小化从\(t\)到\(T\)的累积成本；
- 若子问题存在更优决策序列，则替换后原问题总成本会降低，与原序列最优矛盾，故最优性原理成立。


## 四、确定性DP算法（DDP Algorithm）
### 1. 核心思路
基于最优性原理，分两步：**逆向计算最优值函数（Optimal Value Function）** → **正向构造最优决策序列**。

### 2. 算法步骤（课件原文54页）
#### （1）逆向计算最优值函数（Backward Induction）
- 初始化：终端时刻\(T\)的最优值函数等于终端成本：  
  \[V_T^*(S_T) = c_T(S_T), \quad \forall S_T\]
- 递推：从\(t=T-1\)逆向至\(t=0\)，每个状态的最优值函数为“当前成本+下一状态最优值函数”的最小值：  
  \[V_t^*(S_t) = \min_{x_t \in X_t(S_t)} \left[ c_t(S_t,x_t) + V_{t+1}^*(f_t(S_t,x_t)) \right], \quad \forall S_t\]

#### （2）正向构造最优决策序列（Forward Construction）
- 初始状态\(S_0\)：选择使递推公式取最小值的决策\(x_0^*\)：  
  \[x_0^* \in \arg\min_{x_0 \in X_0(S_0)} \left[ c_0(S_0,x_0) + V_1^*(f_0(S_0,x_0)) \right]\]
- 递推：由状态转移函数计算下一状态\(S_{t+1}^*=f_t(S_t^*,x_t^*)\)，再选择\(x_{t+1}^*\)，直至\(t=T-1\)。


## 五、典型案例（Typical Cases）
### 1. 四皇后问题（Four Queens Problem）
- **问题描述（课件原文25页）**：_“Place four queens on a 4x4 chessboard so that no queen can attack another”_；
- **DP建模思路**：将放置过程分为4个阶段（每阶段放1个皇后），状态为“已放置皇后的位置”，决策为“下一皇后的放置列”，转移函数为“更新已放置位置”，成本函数为“是否冲突”（冲突则成本无穷大）；
- **核心作用**：验证DP解决组合优化问题的有效性，通过状态剪枝避免无效解。

### 2. 确定性调度问题（Deterministic Scheduling Problem）
- **问题描述（课件原文39页）**：4个操作（A,B,C,D），B需在A后，D需在C后，求最小切换成本；
- **DP建模**：
  - 状态\(S_t\)：已完成的操作集合（如\(\{A,C\}\)）；
  - 决策\(x_t\)：下一可执行的操作（如B或D）；
  - 转移函数\(f_t(S_t,x_t)=S_t \cup \{x_t\}\)；
  - 最优结果：通过逆向计算得最优值函数，正向构造最优调度序列，最小总成本为5。

### 3. 旅行商问题（Traveling Salesman Problem, TSP）
- **问题描述**：从A出发，访问所有城市后返回A，最小化总距离；
- **DP建模**：
  - 状态\(S_t\)：当前所在城市+已访问城市集合；
  - 决策\(x_t\)：下一访问的未访问城市；
- **拓展应用**：结合滚动算法（Rollout Algorithm），以“最近邻启发式（Nearest Neighborhood）”为基础启发式，通过一步前瞻优化，将TSP总成本从30降至13（课件原文82-87页）。


## 六、近似算法：滚动算法（Rollout Algorithm）
### 1. 核心背景（课件原文77页）
- 维数灾难（Curse of Dimensionality）：状态空间随城市数呈指数增长（_Exponential growth!!!_），精确DP不可行；
- 核心思路：用**启发式函数（Heuristic Function）** 近似最优值函数\(V_{t+1}^*\)，避免逆向全量计算。

### 2. 一步前瞻滚动算法（Rollout with One-step Lookahead）
- **步骤（课件原文79-80页）**：
  1. 选择基础启发式（如TSP的最近邻）；
  2. 对当前状态\(S_t\)，枚举所有可行决策\(x_t\)；
  3. 计算每个决策对应的“当前成本+启发式预测的后续成本”；
  4. 选择最小成本对应的决策作为最优决策；
- **优势（课件原文案例验证）**：TSP中，滚动算法效果显著优于基础启发式，接近精确DP结果。


## 七、确定性与随机DP的对比（Deterministic vs. Stochastic DP）
| 维度                 | 确定性DP（DDP）                                | 随机DP（SDP）                                                            |
| -------------------- | ---------------------------------------------- | ------------------------------------------------------------------------ |
| 转移函数（课件原文） | \(S_{t+1}=f_t(S_t,x_t)\)（无随机干扰）         | \(S_{t+1}=f_{t+1}(S_t,x_t,W_{t+1})\)（含随机干扰\(W_{t+1}\)）            |
| 成本函数             | \(c_t(S_t,x_t)\)（确定成本）                   | \(c_t(S_t,x_t,W_{t+1})\)（随机成本，需计算期望）                         |
| 目标函数（课件原文） | \(\min \sum_{t=0}^{T-1}c_t(S_t,x_t)+c_T(S_T)\) | \(\min E_W\left[ \sum_{t=0}^{T-1}c_t(S_t,x_t,W_{t+1})+c_T(S_T) \right]\) |
| 核心差异             | 状态演化确定，无期望计算                       | 状态演化随机，需考虑干扰的概率分布                                       |


## 八、核心术语中英文对照表（Key Terms Glossary）
| 中文术语                   | 英文术语                                          | 文档原文标识 |
| -------------------------- | ------------------------------------------------- | ------------ |
| 确定性动态规划             | Deterministic Dynamic Programming (DDP)           | 核心算法     |
| 确定性有限状态有限时域问题 | Deterministic Finite State Finite Horizon Problem | 核心问题定义 |
| 状态变量                   | State Variable (\(S_t\))                          | 核心要素     |
| 决策/控制变量              | Decision/Control Variable (\(x_t\))               | 核心要素     |
| 转移函数                   | Transition Function (\(f_t\))                     | 核心要素     |
| 成本函数                   | Cost Function (\(c_t\))                           | 核心要素     |
| 终端成本                   | Terminal Cost (\(c_T\))                           | 核心要素     |
| 最优值函数                 | Optimal Value Function (\(V_t^*\))                | 算法核心     |
| 最优性原理                 | Principle of Optimality                           | 核心理论     |
| 滚动算法                   | Rollout Algorithm                                 | 近似算法     |
| 随机动态规划               | Stochastic Dynamic Programming (SDP)              | 拓展内容     |
| 旅行商问题                 | Traveling Salesman Problem (TSP)                  | 典型案例     |

## 九、课件重点整理（用来做cheatsheet）
以下是标红概念性英文原文与中文对照翻译（按文档出现顺序排列，术语统一、语义精准，公式保留原文）：

1. In all dynamic programming (DP) problems, the central object is a discrete-time dynamic system that generates a sequence of states under the influence of actions or controls.  
   所有动态规划（DP）问题的核心对象都是离散时间动态系统，该系统在动作或控制的影响下生成一系列状态。

2. In a deterministic DP problem, the transition function (or system equation) is \(S_{t+1}=f_{t}(S_{t},x_{t}),\, t=0,1,... ,T-1.\)  
   在确定性动态规划问题中，状态转移函数（或系统方程）为 \(S_{t+1}=f_{t}(S_{t},x_{t}),\, t=0,1,... ,T-1\)。

3. That is, the state \(S_{t+1}\) is determined solely by state \(S_{t}\) and decision \(x_{t}\)  
   即，状态 \(S_{t+1}\) 仅由当前状态 \(S_{t}\) 和决策 \(x_{t}\) 唯一确定。

4. A deterministic finite state finite horizon problem is equivalent to finding a shortest path from the initial nodes of the (acyclic) graph to the terminal node.  
   确定性有限状态有限时域问题等价于在（无环）图中寻找从初始节点到终端节点的最短路径。

5. Generally, combinatorial optimization problems can be formulated as deterministic finite state finite horizon optimal control problem.  
   通常，组合优化问题可转化为确定性有限状态有限时域最优控制问题。

6. The idea is to break down the solution (to the combinatorial optimization problems) into components, which can be computed sequentially.  
   其核心思想是将组合优化问题的解分解为可序贯计算的组件。

7. Let \({x_{0}^{*}, ..., x_{T-1}^{*}}\) be an optimal control sequence, which together with \(S_{0}\) determines the corresponding state sequence \({S_{1}, ..., S_{T}}\) via the system equation \(S_{t+1}=f_{t}(S_{t},x_{t}),\, t=0,1,... ,T-1.\)  
   设 \({x_{0}^{*}, ..., x_{T-1}^{*}}\) 为最优控制序列，该序列与初始状态 \(S_{0}\) 一起，通过系统方程 \(S_{t+1}=f_{t}(S_{t},x_{t}),\, t=0,1,... ,T-1\) 确定对应的状态序列 \({S_{1}, ..., S_{T}}\)。

8. Consider the subproblem (tail subproblem) whereby we start at \(S_{t}^{*}\) at time t and wish to minimize the “cost-to-go” from time t to time T \(c_{t}\left(S_{t}^{*}, x_{t}\right)+\sum_{m=t+1}^{T-1} c_{m}\left(S_{m}, x_{m}\right)+c_{T}\left(S_{T}\right)\) over \({x_{t}, ..., x_{T-1}}\) with \(x_{m} \in X_{m}(S_{m})\) , \(m=t, ..., T-1\) . Then the truncated optimal control sequence \({x_{t}^{*}, ..., x_{T-1}^{*}}\) is optimal for this tail subproblem.  
   考虑子问题（尾部子问题）：在时间t从状态 \(S_{t}^{*}\) 出发，在 \(x_{m} \in X_{m}(S_{m})\)（\(m=t, ..., T-1\)）的约束下，最小化从时间t到时间T的“后续成本” \(c_{t}\left(S_{t}^{*}, x_{t}\right)+\sum_{m=t+1}^{T-1} c_{m}\left(S_{m}, x_{m}\right)+c_{T}\left(S_{T}\right)\)。则截断后的最优控制序列 \({x_{t}^{*}, ..., x_{T-1}^{*}}\) 是该尾部子问题的最优解。

9. t : time index (decision epoch or stage)  
   t：时间索引（决策时刻或阶段）

10. T : finite planning horizon, i.e., number of times control is applied  
    T：有限规划时域，即控制的施加次数

11. \(S_{t}\) : state of the system at time t  
    \(S_{t}\)：系统在时间t的状态

12. \(S_{0}\) : initial state of the system  
    \(S_{0}\)：系统的初始状态

13. \(x_{t}\) : control or decision variable of the system at time t , \(x_{t} \in X_{t}(S_{t})\) , where \(X_{t}(S_{t})\) is the decision space  
    \(x_{t}\)：系统在时间t的控制或决策变量，\(x_{t} \in X_{t}(S_{t})\)，其中 \(X_{t}(S_{t})\) 为决策空间

14. \(f_{t}\) : transition function (or system equation) that describes the mechanism by which the state is updated, \(S_{t+1}=f_{t}(S_{t}, x_{t})\)  
    \(f_{t}\)：描述状态更新机制的状态转移函数（或系统方程），满足 \(S_{t+1}=f_{t}(S_{t}, x_{t})\)

15. \(c_{t}\) : cost function, \(c_{t}(S_{t}, x_{t})\)  
    \(c_{t}\)：成本函数，表达式为 \(c_{t}(S_{t}, x_{t})\)

16. \(c_{T}\) : terminal cost at the end of the horizon, \(c_{T}(S_{T})\)  
    \(c_{T}\)：时域结束时的终端成本，表达式为 \(c_{T}(S_{T})\)

17. \(V(S_{0})\) : value function (total cost) with respect to initial state \(S_{0}\)  
    \(V(S_{0})\)：关于初始状态 \(S_{0}\) 的值函数（总成本）

18. In finite horizon problems, a finite number of T time steps, indexed by time t (decision epochs or stages)  
    有限时域问题包含T个时间步，由时间t（决策时刻或阶段）索引

19. State of the system \(S_{t}\) at time t  
    系统在时间t的状态为 \(S_{t}\)

20. Control or decision variable \(x_{t} \in X_{t}(S_{t})\) at time t , which depends on \(S_{t}\)  
    时间t的控制或决策变量 \(x_{t} \in X_{t}(S_{t})\)，且依赖于当前状态 \(S_{t}\)

21. The system involves an additive cost function \(c_{t}(S_{t}, x_{t})\)  
    系统包含可加性成本函数 \(c_{t}(S_{t}, x_{t})\)

22. Given initial state \(S_{0}\) , the total cost of a control sequence \({x_{0}, ..., x_{T-1}}\) is \(V(S_{0};x_{0},... ,x_{T-1})=c_{T}(S_{T})+\sum _{t=0}^{T-1}c_{t}(S_{t},x_{t})\)  
    给定初始状态 \(S_{0}\)，控制序列 \({x_{0}, ..., x_{T-1}}\) 的总成本为 \(V(S_{0};x_{0},... ,x_{T-1})=c_{T}(S_{T})+\sum _{t=0}^{T-1}c_{t}(S_{t},x_{t})\)

23. where \(c_{T}(S_{T})\) is the terminal cost of terminal state \(S_{T}\)  
    其中 \(c_{T}(S_{T})\) 是终端状态 \(S_{T}\) 的终端成本

24. \(V(S_{0} ; x_{0}, ..., x_{T-1})\) is well-defined, since \({x_{0}, ..., x_{T-1}}\) and \(S_{0}\) determines exactly \({S_{1}, ..., S_{T}}\)  
    \(V(S_{0} ; x_{0}, ..., x_{T-1})\) 定义良好，因为控制序列 \({x_{0}, ..., x_{T-1}}\) 和初始状态 \(S_{0}\) 可唯一确定状态序列 \({S_{1}, ..., S_{T}}\)

25. Minimize the total cost over all feasible sequences: optimal value as a function of \(S_{0}\) \(V^{*}(S_{0})=min _{x_{t} \in X_{t}(S_{t}), t=0, ..., T-1} V(S_{0} ; x_{0}, ..., x_{T-1})\)  
    在所有可行序列中最小化总成本：最优值作为初始状态 \(S_{0}\) 的函数，表达式为 \(V^{*}(S_{0})=min _{x_{t} \in X_{t}(S_{t}), t=0, ..., T-1} V(S_{0} ; x_{0}, ..., x_{T-1})\)

26. In a stochastic DP problem, the transition function (or system equation) is \(S_{t+1}=f_{t+1}(S_{t},X_{t}^{\pi }(S_{t}),W_{t+1}),\, t=0,1,... ,T-1.\)  
    在随机动态规划问题中，状态转移函数（或系统方程）为 \(S_{t+1}=f_{t+1}(S_{t},X_{t}^{\pi }(S_{t}),W_{t+1}),\, t=0,1,... ,T-1\)。

27. That is, the state \(S_{t+1}\) is determined by state \(S_{t}\) , decision \(x_{t}\) , and random disturbance \(W_{t+1}\)  
    即，状态 \(S_{t+1}\) 由当前状态 \(S_{t}\)、决策 \(x_{t}\) 和随机干扰 \(W_{t+1}\) 共同确定。

28. The system involves an additive cost function \(c_{t}(S_{t}, X_{t}^{\pi}(S_{t}), W_{t+1})\)  
    系统包含可加性成本函数 \(c_{t}(S_{t}, X_{t}^{\pi}(S_{t}), W_{t+1})\)

29. Given initial state \(S_{0}\) , the expected total cost under policy π is \(V^{\pi }(S_{0})=E_{W}[c_{T}(S_{T})+\sum _{t=0}^{T-1}c_{t}(S_{t},X_{t}^{\pi }(S_{t}),W_{t+1})]\)  
    给定初始状态 \(S_{0}\)，策略π下的期望总成本为 \(V^{\pi }(S_{0})=E_{W}[c_{T}(S_{T})+\sum _{t=0}^{T-1}c_{t}(S_{t},X_{t}^{\pi }(S_{t}),W_{t+1})]\)

30. Minimize the expected total cost over all policies: optimal value as a function of \(S_{0}\) \(V^{*}\left(S_{0}\right)=min _{\pi \in \Pi} V^{\pi}\left(S_{0}\right)\)  
    在所有策略中最小化期望总成本：最优值作为初始状态 \(S_{0}\) 的函数，表达式为 \(V^{*}\left(S_{0}\right)=min _{\pi \in \Pi} V^{\pi}\left(S_{0}\right)\)