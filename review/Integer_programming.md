# 整数规划（Integer Programming, IP）1 —— 入门与建模
## 1. 一段话总结
本文围绕**整数规划（Integer Programming, IP）** 展开入门介绍与建模教学，核心是在线性规划（Linear Programming, LP）基础上增加**决策变量（Decision Variables）的整数约束（Integer Constraints）**，明确其分为**纯整数规划（Pure Integer Programming, Pure IP）、混合整数规划（Mixed Integer Programming, MIP/MILP）、0-1整数规划（Binary Integer Programming, Binary IP）** 三大类，详细讲解了“问题分析-变量定义-目标函数（Objective Function）构建-约束条件（Constraints）设定-整数约束添加”的建模流程，介绍了**分支定界法（Branch and Bound Method）、割平面法（Cutting Plane Method）** 等核心求解算法及Python/MATLAB等工具实现，通过生产调度（Production Scheduling）、资源分配（Resource Allocation）、选址（Location Selection）等典型案例，展现其在制造、物流、金融等多领域的应用价值，同时强调直接对线性规划解四舍五入（Rounding）无法保证可行解（Feasible Solution）或最优解（Optimal Solution），需专用算法求解的关键要点。

---
## 2. 思维导图（mindmap）
```mindmap
## 一、核心概念
- 定义：线性规划（Linear Programming, LP）+决策变量（Decision Variables）整数约束（Integer Constraints）
- 核心特征：离散决策（Discrete Decision）、可行域（Feasible Region）有限
- 与线性规划区别：变量取值限制、求解方法（Solution Method）不同
## 二、分类
- 纯整数规划（Pure IP）：所有变量为非负整数（Non-negative Integers）
- 混合整数规划（MIP/MILP）：部分变量整数、部分连续（Continuous）
- 0-1整数规划（Binary IP）：变量仅取0或1（Yes/No决策）
## 三、建模流程（Modeling Process）
- 步骤1：问题分析（Problem Analysis）（明确目标、约束、决策维度）
- 步骤2：定义决策变量（Decision Variables）（整数/0-1/连续变量区分）
- 步骤3：构建目标函数（Objective Function）（最大化/最小化指标）
- 步骤4：设定约束条件（Constraints）（资源、逻辑、边界约束）
- 步骤5：添加整数约束（Integer Constraints）（明确变量取值类型）
## 四、求解方法（Solution Methods）
- 精确算法（Exact Algorithms）
  - 分支定界法（Branch and Bound Method）：分支枚举+定界剪枝（Pruning）
  - 割平面法（Cutting Plane Method）：添加线性约束剔除非整数解
  - 隐枚举法（Implicit Enumeration Method）：针对0-1规划，减少枚举量
- 启发式算法（Heuristic Algorithms）：遗传算法（Genetic Algorithm）、模拟退火（Simulated Annealing）（快速得近似解）
## 五、典型案例（Typical Cases）
- 生产计划问题（Production Planning Problem）：设备产能（Capacity）约束下的产量优化
- 资源分配问题（Resource Allocation Problem）：下料、机床分配（负载均衡Load Balancing）
- 选址问题（Location Problem）：物流中心建设与否（0-1变量）
- 指派问题（Assignment Problem）：任务-人员/设备匹配
## 六、工具与应用（Tools & Applications）
- 求解工具（Solution Tools）：MATLAB（intlinprog函数）、Python（PuLP库）
- 应用领域（Application Fields）：制造（Manufacturing）、物流（Logistics）、金融（Finance）、通信（Communication）、医疗（Medical Care）
```

---
## 3. 详细总结
### 一、整数规划基础概念
1. **定义**：整数规划是线性规划（Linear Programming, LP）的扩展形式，核心是在目标函数（Objective Function）和约束条件（Constraints）为线性的前提下，要求**全部或部分决策变量（Decision Variables）取整数值（Integer Values）** 的优化问题（Optimization Problem），用于解决现实中“个数”“是否选择”等离散决策（Discrete Decision）场景。
2. **核心特征**：
   - 决策变量离散化（Discretization），可行域（Feasible Region）为有限个整数点集合
   - 目标函数与约束条件仍保持线性（主流为线性整数规划，Linear Integer Programming）
   - 计算复杂度（Computational Complexity）高于线性规划，属于NP类问题（NP-hard Problem）
3. **与线性规划的关键区别**：
   - 变量取值：线性规划可连续取值（Continuous Values），整数规划受整数约束（Integer Constraints）
   - 求解结果：线性规划最优解可能为小数，整数规划需整数解（Integer Solution）
   - 求解方法：线性规划用单纯形法（Simplex Method），整数规划需专用算法（分支定界法等）
   - 关键提醒：直接对线性规划松弛问题（Relaxation Problem）的解四舍五入（Rounding），可能得到不可行解（Infeasible Solution）或非最优解（Non-optimal Solution）（例：松弛解x1=3/2、x2=10/3，舍入后4个候选点均非最优）

### 二、整数规划的三大类型
| 类型                         | 定义                                                   | 核心适用场景                                   | 典型案例                                                                                                                 |
| ---------------------------- | ------------------------------------------------------ | ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **纯整数规划（Pure IP）**    | 所有决策变量均为非负整数（Non-negative Integers）      | 需统计“数量”的决策问题                         | 背包问题（Knapsack Problem）（物品选取数量）、生产调度（Production Scheduling）（产品生产台数）                          |
| **混合整数规划（MIP/MILP）** | 部分变量为整数，其余为连续变量（Continuous Variables） | 离散选择+连续分配结合的问题                    | 物流中心选址（Logistics Center Location）（0-1变量）+ 运输量分配（Transportation Quantity Allocation）（连续变量）       |
| **0-1整数规划（Binary IP）** | 所有整数变量仅取0或1                                   | “是/否”“选/不选”的逻辑决策（Logical Decision） | 项目投资取舍（Project Investment Selection）、设备启停（Equipment Start/Stop）、任务分配（指派问题，Assignment Problem） |

### 三、整数规划建模步骤（核心流程）
1. **问题分析（Problem Analysis）**：明确决策目标（最大化利润/最小化成本等）、约束条件（资源限制、逻辑规则等）、决策维度（需选择的方案、分配的资源等）。
2. **定义决策变量（Decision Variables）**：
   - 纯整数变量：如“x_j为第j种切割方式的圆钢根数”（x_j≥0且为整数）
   - 0-1变量：如“y_i=1表示在i地建仓库，y_i=0表示不建”（Binary Variables）
   - 混合变量：如“z_ij为仓库i向客户j的运输量（连续变量），y_i为仓库i是否启用（0-1变量）”
3. **构建目标函数（Objective Function）**：以线性形式表示决策目标，如“最小化原材料使用量”“最大化总利润（Total Profit）”。
4. **设定约束条件（Constraints）**：
   - 资源约束（Resource Constraints）：如“机器加工时间≤可用时间（Available Time）”“原材料消耗量≤库存（Inventory）”
   - 逻辑约束（Logical Constraints）：如“不同时选择互斥方案（Mutually Exclusive Alternatives）”“至少选择k个方案”
   - 边界约束（Boundary Constraints）：变量的取值范围（如x≥0、y∈{0,1}）
5. **添加整数约束（Integer Constraints）**：明确标注变量的整数属性（纯整数/0-1），完成模型构建（Model Formulation）。

### 四、核心求解方法
#### 1. 精确算法（Exact Algorithms，保证最优解）
- **分支定界法（Branch and Bound Method）**：
  - 核心思路：将原问题分解为多个子问题（Subproblems）（分支，Branching），求解每个子问题的线性松弛解（Linear Relaxation Solution），通过上下界（Upper and Lower Bounds）判断剪枝（Pruning）非最优子问题，逐步缩小搜索范围。
  - 关键步骤：初始化（Initialization）→求解松弛问题→分支生成子问题→计算子问题上下界→剪枝→迭代（Iteration）直至找到最优整数解。
  - 适用场景：中小规模整数规划问题，是主流精确解法。
- **割平面法（Cutting Plane Method）**：
  - 核心思路：在松弛线性规划的可行域（Feasible Region）中添加“割平面（Cutting Plane）”（新的线性约束），逐步剔除非整数解，逼近整数解集的凸包（Convex Hull）。
  - 常见割平面类型：Gomory割（Gomory Cut）、Chvátal割（Chvátal Cut）等。
  - 适用场景：纯整数规划问题，无需分支枚举但割平面构造需技巧。
- **隐枚举法（Implicit Enumeration Method）**：
  - 核心思路：针对0-1规划，通过变量赋值优先级排序和目标函数上下界估计，隐式排除大量非最优解组合，减少枚举量（Enumeration Quantity）。

#### 2. 启发式算法（Heuristic Algorithms，快速得近似解）
| 算法类型                                           | 核心原理                                                               | 优点                                            | 缺点                                                                  |
| -------------------------------------------------- | ---------------------------------------------------------------------- | ----------------------------------------------- | --------------------------------------------------------------------- |
| 遗传算法（Genetic Algorithm）                      | 模拟自然选择与遗传变异（Genetic Mutation），迭代优化种群（Population） | 找到全局最优解（Global Optimal Solution）概率高 | 计算成本（Computational Cost）高，易过早收敛（Premature Convergence） |
| 模拟退火算法（Simulated Annealing）                | 借鉴物理退火过程，允许局部最优解（Local Optimal Solution）跳出         | 能避免局部最优陷阱                              | 参数调整复杂，运行时间（Running Time）长                              |
| 粒子群优化算法（Particle Swarm Optimization, PSO） | 模拟粒子群体协作搜索最优解                                             | 参数调整简单，适配连续/离散问题                 | 可能陷入局部最优解                                                    |

#### 3. 工具支持（Tool Support）
- MATLAB：`intlinprog`函数求解混合整数线性规划（Mixed-Integer Linear Programming, MILP），需输入目标函数系数、约束矩阵（Constraint Matrix）、整数变量索引。
- Python：`PuLP`库、`scipy.optimize`模块，支持模型构建与求解。
- 其他工具：Mathematica（`LinearProgram`函数）、专业求解器（Solver）（Gurobi、CPLEX）。

### 五、典型案例与应用场景
#### 1. 经典案例
- **合理下料问题（Cutting Stock Problem）**（纯整数规划）：m种零件需求（Demand），n种切割方式，目标最小化圆钢使用根数，约束为每种零件产量不低于需求量。
- **机床分配问题（Machine Allocation Problem）**（0-1规划）：n种零件分配至m台机床，目标最小化最大负载时间（Maximum Load Time），变量x_ij表示第i种零件是否由第j台机床加工（0-1）。
- **生产计划问题（Production Planning Problem）**（混合整数规划）：工厂生产甲、乙机床，利润分别为4000元/台、3000元/台，受A/B/C机器加工时间限制（A：10h/天、B：8h/天、C：7h/天），决策生产台数（整数）以最大化利润。

#### 2. 应用领域（Application Fields）
- 制造业（Manufacturing）：生产排程（Production Scheduling）、生产线平衡（Production Line Balancing）、换线优化（Line Change Optimization）。
- 物流供应链（Logistics and Supply Chain）：仓库选址（Warehouse Location）、车辆路径规划（Vehicle Routing Problem, VRP）、无人机配送航线决策。
- 金融（Finance）：投资组合选择（Portfolio Selection）、风险控制（Risk Control）、期权合约（Option Contract）买卖决策。
- 其他：通信网络频谱分配（Spectrum Allocation）、5G基站规划（5G Base Station Planning）、医护排班（Medical Staff Scheduling）、手术室调度（Operating Room Scheduling）。

### 六、建模与求解注意事项
1. 变量定义需精准：明确变量类型（整数/0-1/连续），避免因变量设定不当导致模型无解（Infeasible Model）或非最优。
2. 约束条件需完整：覆盖资源限制、逻辑规则（如互斥方案、固定成本（Fixed Cost））等，避免遗漏关键约束。
3. 避免直接四舍五入：线性规划松弛解的小数部分不能简单舍入，需通过专用算法求解整数解。
4. 大规模问题优化：可利用问题的数学结构（如总幺模性（Total Unimodularity））或分解方法（Dantzig-Wolfe分解）提升求解效率（Solution Efficiency）。

---
## 4. 关键问题
### 问题1：整数规划与线性规划的核心区别是什么？实际应用中为何不能直接对线性规划的解四舍五入得到整数规划解？
**答案**：
- 核心区别有两点：一是变量取值限制，线性规划（Linear Programming, LP）决策变量可连续取值（Continuous Values），整数规划（Integer Programming, IP）要求全部或部分变量取整数值（Integer Values）（纯整数/0-1/混合）；二是求解方法（Solution Method），线性规划可用单纯形法（Simplex Method）直接求解，整数规划需用分支定界法（Branch and Bound Method）等专用算法。
- 实际应用中不能直接四舍五入的原因是：1. 舍入后的解可能违反约束条件（Constraints）（如机器加工时间超过可用时间（Available Time）），导致不可行解（Infeasible Solution）；2. 即使可行，也可能不是整数规划的最优解（Optimal Solution）（例：线性规划松弛解x1=3/2、x2=10/3，舍入后4个候选点均非最优）；3. 整数规划的可行域（Feasible Region）是离散点集合，而非连续区域，四舍五入无法保证落在可行域内或最优位置。

### 问题2：0-1整数规划的核心特点是什么？请举例说明其在“物流中心选址”问题中的建模思路。
**答案**：
- 0-1整数规划（Binary Integer Programming, Binary IP）的核心特点是决策变量（Decision Variables）仅取0或1，能精准刻画“是/否”“选/不选”的二元逻辑决策（Binary Logical Decision），适用于互斥方案选择、固定成本（Fixed Cost）处理等场景。
- 物流中心选址问题的建模思路：
  - 1. 定义0-1变量y_i（i=1,2,…,m），y_i=1表示在第i地建设物流中心（Logistics Center），y_i=0表示不建设；
  - 2. 定义连续变量x_ij，表示从物流中心i向客户j的运输量（Transportation Quantity）；
  - 3. 目标函数（Objective Function）：最小化总成本（Total Cost）（建设成本（Construction Cost）×y_i + 运输成本（Transportation Cost）×x_ij）；
  - 4. 约束条件（Constraints）：
    - ① 每个客户j的需求量（Demand）被完全满足（∑x_ij = d_j）；
    - ② 物流中心i的运输量不超过其最大容量（Maximum Capacity）（∑x_ij ≤ C_i×y_i，y_i=0时x_ij=0）；
    - ③ y_i∈{0,1}，x_ij≥0。

### 问题3：分支定界法求解整数规划的核心步骤是什么？其“剪枝”操作的作用是什么？
**答案**：
- 分支定界法（Branch and Bound Method）的核心步骤：
  - 1. 初始化（Initialization）：将原整数规划问题作为初始问题，求解其线性松弛问题（Linear Relaxation Problem）；
  - 2. 分支（Branching）：若松弛解为非整数，选择一个非整数变量，构建两个子问题（Subproblems）（变量≤向下取整值、变量≥向上取整值）；
  - 3. 定界（Bounding）：求解每个子问题的松弛解，得到各子问题的上下界（Upper and Lower Bounds）（目标函数的可能范围）；
  - 4. 剪枝（Pruning）：若子问题的下界≥当前已知的最优整数解的上界，剔除该子问题（无更优解）；
  - 5. 迭代（Iteration）：重复分支、定界、剪枝步骤，直至所有子问题被处理，当前已知的最优解即为原问题的最优整数解（Optimal Integer Solution）。
- “剪枝”操作的核心作用是排除不可能存在更优解的子问题，减少搜索范围（Search Range），降低计算复杂度（Computational Complexity），避免穷举所有可能的整数组合（尤其变量较多时，穷举不可行）。

---

# 整数规划（Integer Programming, IP）2 —— 求解算法
## 一、文档概述（Document Overview）
本文档聚焦整数规划的**求解算法（Solution Algorithms）**，基于前期整数规划建模基础，通过“理论推导+案例验证”系统讲解三大核心解法：**LP松弛（LP Relaxation）、分支定界法（Branch and Bound Method）、割平面法（Cutting Plane Method）**，并延伸至**Chvátal-Gomory不等式（Chvátal-Gomory Inequality）** 这一通用理论工具。文档以Tatham投资、服务中心选址、生产优化等案例为载体，强调“整数约束带来的求解特殊性”，驳斥“直接舍入LP解”的误区，最终形成“松弛-分支-切割”的完整求解逻辑链。


## 二、IP与LP的核心差异及LP松弛的基础作用
### 1. IP与LP的本质区别（Key Differences Between IP and LP）
| 维度                      | 线性规划（Linear Programming, LP）        | 整数规划（Integer Programming, IP）                                 |
| ------------------------- | ----------------------------------------- | ------------------------------------------------------------------- |
| 变量取值                  | 连续值（Continuous Values）               | 部分/全部为整数（Integer Values）或0-1值                            |
| 可行域（Feasible Region） | 连续凸集（Continuous Convex Set）         | 离散整数点集合（Discrete Integer Point Set）                        |
| 最优解特性                | 必在顶点（Extreme Point）处               | **_Optimal IP solutions are NOT necessarily CPF/BF’s_**（课件原文） |
| 求解复杂度                | 多项式时间（Polynomial Time，如单纯形法） | NP-难（NP-hard），解数量呈**_Exponential growth_**（课件原文）      |

### 2. LP松弛的定义与作用（Definition and Role of LP Relaxation）
- **定义**：去掉IP中的整数约束，得到的线性规划问题称为原IP的**LP松弛问题（LP Relaxation）**，记为：
  原IP：\(\max c^T x, s.t. Ax \leq b, x \in \mathbb{Z}^n_+\)
  LP松弛：\(\max c^T x, s.t. Ax \leq b, x \in \mathbb{R}^n_+\)
- **核心作用**：
  1. 提供**上界（Upper Bound, UB）/下界（Lower Bound, LB）**：对最大化问题，LP松弛的最优目标值\(z^{LP,*}\)是IP最优值\(z^{IP,*}\)的 **_upper bound_**（课件原文）；若找到IP可行解，其目标值为\(z^{IP,*}\)的 **_lower bound_**（课件原文）。
     ▶ 案例验证：文档中0-1规划案例（\(\max 9x_1+5x_2+6x_3+4x_4\)）的LP松弛最优解为\(x_1=5/6, x_2=1, x_3=0, x_4=1\)，\(z^{LP,*}=16.5\)，确为\(z^{IP,*}\)的UB。
  2. 验证IP可行性：若LP松弛无解，则原IP必无解。
  3. 辅助判断整数解：若LP松弛的最优解满足整数约束，则该解即为原IP的最优解。

### 3. 直接舍入LP解的误区（Pitfalls of Rounding LP Solutions）
文档明确指出，对LP松弛解直接舍入（Rounding）会导致两大问题：
1. **_May result in infeasible solutions_**（课件原文）：如上述0-1规划案例中，将\(x_1=5/6\)舍入为1时，代入约束\(6x_1+3x_2+5x_3+2x_4=6×1+3×1+0+2×1=11>10\)，导致不可行。
2. **_May be far away from the optimal solution_**（课件原文）：文档中生产优化案例（\(\max x_1+5x_2\)）的LP松弛最优解为\(x_1=2, x_2=1.8\)，舍入为\((2,1)\)（目标值7），但IP最优解为\((0,2)\)（目标值10），差距显著。


## 三、核心解法一：分支定界法（Branch and Bound Method）
### 1. 算法核心思想（Core Idea）
分支定界法是IP的 **_“Implicit” enumeration_**（隐式枚举）与 **_Divide and conquer_**（分而治之）结合的精确算法（课件原文），通过“分支拆分解空间、定界缩小范围、剪枝排除无效子问题”，避免穷举所有整数组合。

### 2. 关键术语（Key Terminology）
- **分支（Branching）**：选择LP松弛解中的 **_non-integer solutions_**（非整数变量），将原问题拆分为两个子问题（课件原文）。例如，若\(x_1=5/6\)非整数，则分支为\(x_1 \leq 0\)和\(x_1 \geq 1\)。
- **定界（Bounding）**：对每个子问题，求解其LP松弛，得到子问题IP最优值的UB（记为\(\bar{z}_k\)），即 **_\(\bar{z}_k = z_k^{LP,*} = \max \{c^T x | x \in S_k\}\)_**（课件原文，\(S_k\)为子问题的可行域）。
- **剪枝（Fathoming/Pruning）**：对最大化问题，满足以下任一条件的子问题可被剪枝（停止分支）：
  - **F1（Bound Pruning）**：\(\bar{z}_k \leq \underline{z}\)（\(\underline{z}\)为当前全局LB），即子问题无更优解；
  - **F2（Infeasibility Pruning）**：子问题的LP松弛无解，原IP子问题亦无解；
  - **F3（Optimality Pruning）**：子问题的LP松弛解为整数，该解即为子问题的IP最优解，需 **_update incumbent solution and (global) lower bound \(\underline{z}\) by \(z_k^{IP,*}\)_**（课件原文，incumbent solution为当前全局最优IP解）。
- **最优性差距（Optimality Gap）**：衡量当前解与最优解的接近程度，公式为 **_\(Optimality gap = (bound – incumbent) / incumbent\)_**（课件原文）。例如，当UB=16、LB=9时，差距为\((16-9)/9≈77.78\%\)。

### 3. 完整求解步骤（Complete Solution Steps）
以文档中0-1规划案例（\(\max 9x_1+5x_2+6x_3+4x_4\)）为例，步骤如下：
1. **初始化（Initialization）**：求解原IP的LP松弛，得\(x^{LP,*}=(5/6,1,0,1)\)，\(z^{LP,*}=16.5\)（UB=16.5）；初始化LB=-∞，incumbent solution无。
2. **分支（Branching）**：选择非整数变量\(x_1\)，拆分为子问题1（\(x_1 \leq 0\)）和子问题2（\(x_1 \geq 1\)）。
3. **求解子问题1**：LP松弛解为\((0,1,0,1)\)（整数解），\(z=9\)，触发F3：更新incumbent=(0,1,0,1)，LB=9。
4. **求解子问题2**：LP松弛解为\((1,4/5,0,4/5)\)，\(z=7.2\)，触发F1（7.2 ≤ 9），剪枝。
5. **迭代与进一步分支**：若子问题2的LP松弛解为\(z=16.2\)（大于LB=9），则继续对非整数变量\(x_2\)分支（\(x_2 \leq 0\)和\(x_2 \geq 1\)），重复定界与剪枝，直至所有子问题处理完毕。
6. **终止（Termination）**：当所有子问题被剪枝，incumbent solution即为原IP的最优解，文档案例最终得\(x^{IP,*}=(1,1,0,0)\)，\(z^{IP,*}=14\)

### 4. 搜索策略（Search Strategies）
- **深度优先搜索（Depth First Search）**：优先处理最深层的子问题，**_find a first feasible solution_**（快速获得初始LB，课件原文）。
- **最佳边界优先搜索（Best-bound First Search）**：优先处理\(\bar{z}_k\)最大的子问题，**_avoid branching on any node where \(\bar{z}_k \leq z^{IP,*}\)_**（减少无效分支，课件原文）。


## 四、核心解法二：割平面法（Cutting Plane Method）
### 1. 基础定义（Basic Definitions）
- **有效不等式（Valid Inequality）**：**_A valid inequality for a set of integer solution S is one that is satisfied by all solutions in S_**（对所有IP可行解成立的不等式，课件原文）。  
- **割平面（Cutting Plane）**：对IP的LP松弛，若有效不等式 **_is not satisfied by \(x^{LP,*}\)_**（不满足LP松弛最优解），则该不等式为割平面（课件原文）。其作用是“切割”LP松弛的非整数可行域，保留所有IP可行域，逐步逼近整数解。

### 2. 多面体公式化（Polyhedral Formulation）
文档引入多面体概念辅助理解割平面的几何意义：
- **多面体（Polyhedron）**：**_\(P \subset \mathbb{R}^n\) is a set of the form \(\{x \in \mathbb{R}^n | Ax \leq b\}\)_**（课件原文）。
- **强公式化（Stronger Formulation）**：对IP可行解集合S，若两个多面体\(P_1\)和\(P_2\)均包含S（即\(S \subset P_1, S \subset P_2\)），且 **_\(P_1 \subset P_2\)_**，则\(P_1\)是更强的公式化（课件原文），其LP松弛解更接近IP解。
- **理想公式化（Ideal Formulation）**：**_A formulation is ideal if each extreme point of P is in S_**（多面体的所有顶点均为IP可行解，课件原文），此时LP松弛解即为IP最优解。

### 3. Gomory割平面法（Gomory Cutting Plane Method）
#### （1）适用场景
针对标准型IP：\(\max c^T x, s.t. Ax = b, x \geq 0, x \in \mathbb{Z}^n\)，是最经典的割平面构造方法。

#### （2）核心步骤（Core Steps）
1. **求解LP松弛**：设LP松弛的最优基矩阵为B，基变量\(x_B = B^{-1}b - B^{-1}Nx_N\)，记\(\bar{A} = B^{-1}A\)，\(\bar{b} = B^{-1}b\)。
2. **选择非整数基变量**：若\(x_B(i)\)（第i个基变量）为非整数，取其对应的约束方程：
   **_\(x_{B(i)} + \sum_{j \in N} \bar{a}_{ij}x_j = \bar{b}_i\)_**（课件原文，N为非基变量索引集）。
3. **构造割平面**：
   - 对系数\(\bar{a}_{ij}\)和右端项\(\bar{b}_i\)向下取整（记为\(\lfloor \cdot \rfloor\)），利用\(x \geq 0\)推导有效不等式：
     **_\(x_{B(i)} + \sum_{j \in N} \lfloor \bar{a}_{ij} \rfloor x_j \leq \lfloor \bar{b}_i \rfloor\)_**（课件原文）。
   - 验证割平面性质：该不等式不满足\(x^{LP,*}\)（因\(\bar{b}_i\)非整数，\(\lfloor \bar{b}_i \rfloor < \bar{b}_i\)，且非基变量\(x_N=0\)），故为有效割平面。
4. **迭代求解**：将割平面加入原LP松弛，重新求解；若新LP松弛解为整数，即为IP最优解；否则重复步骤2-3，直至得到整数解。

#### （3）案例验证（文档生产优化案例）
IP问题：\(\max 4x_1 - x_2, s.t. 7x_1-2x_2 \leq14, x_2 \leq3, 2x_1-2x_2 \leq3, x_1,x_2 \geq0, x \in \mathbb{Z}^2\)  
1. 初始LP松弛最优解：\(x_1=20/7, x_2=3\)，\(z^{LP,*}=59/7≈8.43\)（非整数）。  
2. 选择基变量\(x_1\)，其约束方程为：**_\(x_1 + \frac{1}{7}s_1 + \frac{2}{7}s_2 = \frac{20}{7}\)_**（\(s_1,s_2\)为松弛变量）。  
3. 构造割平面：向下取整得\(x_1 + 0·s_1 + 0·s_2 \leq 2\)（即\(x_1 \leq 2\)）。  
4. 加入割平面后求解新LP松弛：得\(x_1=2, x_2=0.5\)（仍非整数），继续构造割平面\(x_1 - x_2 \leq1\)，最终得整数解\(x_1=2, x_2=1\)，\(z^{IP,*}=7\)。


## 五、通用理论工具：Chvátal-Gomory不等式（C-G Inequality）
### 1. 定义与推导（Definition and Derivation）
对IP可行解集合\(S = P \cap \mathbb{Z}^n\)（\(P\)为LP松弛可行域），任取非负向量\(u \geq 0\)，对LP松弛的约束\(Ax \leq b\)左乘u得：  
**_\(u^T Ax \leq u^T b\)_**（对所有\(x \in P\)成立）。  
因\(x \in \mathbb{Z}^n\)且\(u^T A, u^T b\)为实数，向下取整后推导有效不等式：  
**_\(\lfloor u^T A \rfloor x \leq \lfloor u^T b \rfloor\)_**（对所有\(x \in S\)成立，课件原文），此即为Chvátal-Gomory不等式。

### 2. 与Gomory割的关系（Relationship with Gomory Cuts）
- **Gomory割是C-G不等式的特例**：当\(u\)取基矩阵逆\(B^{-1}\)的某一行时，C-G不等式退化为Gomory割平面。  
- **通用性定理**：文档引用核心定理：**_Every valid inequality for \(S=P \cap \mathbb{Z}^n\), where \(P=\{Ax \leq b, x \geq0\}\), can be obtained by applying the Chvátal-Gomory procedure a finite number of times_**（课件原文，即所有IP的有效不等式均可通过有限次C-G过程生成）。


## 六、关键结论与注意事项（Key Conclusions and Notes）
1. **IP求解的核心逻辑**：通过LP松弛建立上下界，利用分支定界法拆分解空间，结合割平面法缩小可行域，最终高效找到整数最优解。  
2. **算法选择依据**：  
   - 小规模IP（变量≤20）：优先用分支定界法（保证全局最优）；  
   - 大规模IP（变量≥50）：可结合割平面法预处理，或用启发式算法（如遗传算法）快速获取近似解。  
3. **文档案例的共性启示**：无论是Tatham投资（0-1规划）、服务中心选址（设施布局）还是生产优化（混合整数规划），IP建模的核心是“用整数变量刻画离散决策”，求解的核心是“通过松弛与切割平衡最优性与效率”。


## 七、核心术语中英文对照表（Glossary）
| 中文术语             | 英文术语                          | 文档原文标识           |
| -------------------- | --------------------------------- | ---------------------- |
| 整数规划             | Integer Programming (IP)          | 全文核心概念           |
| LP松弛               | LP Relaxation                     | 第二章核心定义         |
| 分支定界法           | Branch and Bound Method           | 第三章核心算法         |
| 割平面法             | Cutting Plane Method              | 第四章核心算法         |
| Gomory割平面法       | Gomory Cutting Plane Method       | 第四章重点方法         |
| Chvátal-Gomory不等式 | Chvátal-Gomory (C-G) Inequality   | 第五章通用工具         |
| 可行解               | Feasible Solution                 | 第二章基础概念         |
| 最优解               | Optimal Solution                  | 第二章基础概念         |
| 上界/下界            | Upper Bound (UB)/Lower Bound (LB) | 第二章定界基础         |
| 剪枝                 | Fathoming/Pruning                 | 第三章分支定界关键步骤 |
| 当前最优解           | Incumbent Solution                | 第三章剪枝条件F3       |
| 最优性差距           | Optimality Gap                    | 第三章性能衡量指标     |
| 多面体公式化         | Polyhedral Formulation            | 第四章割平面几何基础   |
| 强公式化             | Stronger Formulation              | 第四章多面体性质       |

---

# 整数规划（Integer Programming, IP）3 —— 高级建模案例
## 一、文档概述（Document Overview）
本文档聚焦整数规划的**高级建模技术（Advanced Modeling Techniques）**，围绕**网络流问题（Network Flow Problems）、选址问题（Location Problems）、路径规划问题（Route Planning Problems）** 三大核心场景，通过10+经典案例（如最短路径、集合覆盖、TSP、VRP及其变体），系统讲解“问题拆解-决策变量定义-约束条件构建-目标函数确立”的完整建模流程。文档核心特色是**问题演进式建模**，从基础单主体路径规划（TSP）逐步扩展到多主体、带约束的复杂场景（PDPTW），并强调不同问题间的建模逻辑迁移，引用大量课件原文（下划线标注）强化理论严谨性。


## 二、核心问题模块与建模详解
### （一）网络流相关问题（Network Flow Related Problems）
#### 1. 最短路径问题（Shortest Path Problem）
- **问题描述（Problem Description）**：  
  _“Directed graph: \(G=(N, A)\); Distance (cost) of arc \((i, j) \in A\): \(c_{ij} ≥0\); Find the shortest distance (cost) path from the origin node (O) to the destination node (D)”_（课件原文）。  
  即给定有向图，寻找从起点O到终点D的最小成本路径。

- **核心建模要素**：
  - 数据（Data）：节点集\(N\)、边集\(A\)、边成本\(c_{ij}\)、起点O、终点D。
  - 决策变量（Decision Variables）：\(x_{ij}= \begin{cases}1, & 边(i,j)被选入路径 \\ 0, & 否则\end{cases}\)，\(x_{ij} \in \mathbb{B}\)（二元变量）。
  - 约束条件（Constraints）：  
    流量平衡约束（Flow Balance）：  
    \[\sum_{(j,k) \in A} x_{jk} - \sum_{(i,j) \in A} x_{ij} = \begin{cases}1, & j=O \text{（起点流出）} \\ 0, & j \in N \setminus\{O,D\} \text{（中间节点流量平衡）} \\ -1, & j=D \text{（终点流入）}\end{cases}\]
  - 目标函数（Objective Function）：\(\min \sum_{(i,j) \in A} c_{ij}x_{ij}\)（最小化总路径成本）。

- **关键知识点**：  
  最短路径问题是网络流问题的基础，其建模核心是“流量平衡约束”，且因满足**_Integral property_**（整数性质），线性规划解即为整数解（课件原文）。

#### 2. 切割下料问题（Cutting Stock Problem）
- **问题描述（Problem Description）**：  
  _“Supply: large rolls of paper (integer width W); Customer demand: \(b_i\) rolls of integer width \(w_i ≤W\); A large roll can be cut into smaller rolls: pattern; Goal: minimize the number of large rolls while satisfying customer demand”_（课件原文）。  
  即利用固定宽度的大卷材料，切割成满足客户需求的小卷，最小化大卷使用数量。

- **核心建模要素**：
  - 数据（Data）：大卷宽度\(W\)、客户需求（小卷宽度\(w_i\)、数量\(b_i\)）、切割模式（Pattern，指大卷的切割方案）。
  - 决策变量（Decision Variables）：设存在\(k\)种切割模式，\(y_k\)为第\(k\)种模式的使用次数（整数变量）；\(a_{ik}\)为第\(k\)种模式中包含小卷\(i\)的数量（非负整数）。
  - 约束条件（Constraints）：  
    需求满足约束：\(\sum_{k=1}^K a_{ik}y_k ≥b_i\)（\(\forall i\)，所有模式切割出的小卷\(i\)总数≥需求）；  
    模式可行性约束：\(\sum_{i=1}^m w_i a_{ik} ≤W\)（\(\forall k\)，单种模式切割总宽度≤大卷宽度）。
  - 目标函数（Objective Function）：\(\min \sum_{k=1}^K y_k\)（最小化大卷使用数量）。

- **关键知识点**：  
  切割模式的数量可能呈**_exponential growth_**（指数增长），是建模的核心挑战（课件原文），实际应用中需结合启发式算法筛选有效模式。


### （二）选址类问题（Location Problems）
#### 1. 集合覆盖问题（Set Covering Problem, SCP）
- **问题描述（Problem Description）**：  
  _“Locate a cost-minimizing set of facilities that cover all the demand nodes; A demand node is covered if it is within coverage distance C from a facility”_（课件原文）。  
  即在候选地址中选择设施位置，以最小成本覆盖所有需求节点（需求节点在设施覆盖距离内即为被覆盖）。

- **核心建模要素**：
  - 数据（Data）：网络\(G=(N,A)\)、需求节点集\(I \subset N\)、候选设施地址集\(J \subset N\)、设施建设成本\(f_j\)、节点间距离\(d_{ij}\)、覆盖距离\(C\)。
  - 辅助定义：\(a_{ij}= \begin{cases}1, & d_{ij} ≤C \text{（设施j覆盖节点i）} \\ 0, & 否则\end{cases}\)。
  - 决策变量（Decision Variables）：\(x_j= \begin{cases}1, & 候选地址j建设设施 \\ 0, & 否则\end{cases}\)，\(x_j \in \mathbb{B}\)。
  - 约束条件（Constraints）：  
    全覆盖约束：\(\sum_{j \in J} a_{ij}x_j ≥1\)（\(\forall i \in I\)，每个需求节点至少被1个设施覆盖）。  
    课件案例约束示例：\(x_A+x_B+x_D ≥1\)（节点A被设施A/B/D覆盖）、\(x_C+x_E+x_F ≥1\)（节点C被设施C/E/F覆盖）等。
  - 目标函数（Objective Function）：\(\min \sum_{j \in J} f_jx_j\)（最小化设施建设总成本）。

- **案例验证**：课件中美国500个大型县选址案例，覆盖距离300英里时，14个设施即可实现100%覆盖（课件原文）。

#### 2. 最大覆盖问题（Maximum Covering Problem, MCP）
- **问题描述（Problem Description）**：  
  _“Locate a set of facilities (maximum number P) that maximize the covered demands; A demand node is covered if within distance C from a facility”_（课件原文）。  
  与SCP的核心区别：设施数量有上限\(P\)，目标是最大化被覆盖的需求量（而非全覆盖）。

- **核心建模要素**：
  - 新增数据：设施数量上限\(P\)、需求节点\(i\)的需求量\(h_i\)。
  - 新增决策变量：\(z_i= \begin{cases}1, & 需求节点i被覆盖 \\ 0, & 否则\end{cases}\)，\(z_i \in \mathbb{B}\)。
  - 新增约束：  
    设施数量约束：\(\sum_{j \in J} x_j ≤P\)；  
    覆盖逻辑约束：\(z_i ≤\sum_{j \in J} a_{ij}x_j\)（\(\forall i\)，节点i被覆盖的前提是覆盖它的设施已建设）。
  - 目标函数（Objective Function）：\(\max \sum_{i \in I} h_i z_i\)（最大化被覆盖的总需求量）。

- **案例验证**：同一美国县案例中，10个设施可覆盖97%需求，7个设施可覆盖88%需求（课件原文）。

#### 3. P-中心问题（P-Center Problem）
- **问题描述（Problem Description）**：  
  _“Locate a set of facilities (maximum number P) that minimize the maximum distance between a demand node and its closest facility”_（课件原文）。  
  核心目标：在最多建设\(P\)个设施的前提下，最小化“需求节点到最近设施的最大距离”（即最小化服务最差节点的距离）。

- **核心建模要素**：
  - 决策变量：设施选址变量\(x_j\)（同SCP）；新增\(w\)为“最大服务距离”（连续变量，需最小化）；\(y_{ij}= \begin{cases}1, & 需求节点i由设施j服务 \\ 0, & 否则\end{cases}\)。
  - 约束条件：  
    设施数量约束：\(\sum_{j \in J} x_j ≤P\)；  
    服务分配约束：\(\sum_{j \in J} y_{ij}=1\)（\(\forall i\)，每个节点仅由1个设施服务）；  
    距离约束：\(d_{ij}y_{ij} ≤w\)（\(\forall i,j\)，节点i的服务距离≤最大距离\(w\)）；  
    逻辑约束：\(y_{ij} ≤x_j\)（\(\forall i,j\)，节点i由设施j服务的前提是j已建设）。
  - 目标函数（Objective Function）：\(\min w\)（最小化最大服务距离）。

#### 4. P-中位数问题（P-Median Problem）
- **问题描述（Problem Description）**：  
  _“Locate a set of facilities (maximum number P) that minimize the total demand-weighted distance”_（课件原文）。  
  核心目标：在最多建设\(P\)个设施的前提下，最小化“需求节点到最近设施的加权总距离”（权重为节点需求量\(h_i\)）。

- **核心建模要素**：
  - 决策变量：设施选址变量\(x_j\)、服务分配变量\(y_{ij}\)（同P-中心）。
  - 约束条件：与P-中心一致（设施数量、服务分配、逻辑约束）。
  - 目标函数（Objective Function）：\(\min \sum_{i \in I} \sum_{j \in J} h_i d_{ij} y_{ij}\)（最小化需求加权总距离）。

- **P-中心与P-中位数的核心区别**（课件原文）：
  | 维度                 | P-中心问题                   | P-中位数问题                       |
  | -------------------- | ---------------------------- | ---------------------------------- |
  | 目标                 | 最小化最大服务距离           | 最小化加权总服务距离               |
  | 服务公平性           | 强调公平（无最差服务）       | 强调效率（总距离最优）             |
  | 案例结果（10个设施） | 最大距离373英里，覆盖率86.8% | 平均距离134.6英里，最大距离507英里 |


### （三）路径规划类问题（Route Planning Problems）
#### 1. 旅行商问题（Traveling Salesman Problem, TSP）
- **问题描述（Problem Description）**：  
  _“A sales agent starts from the office, visits each of the n customers exactly once, returns to the office; Find the route with the shortest total travel distance”_（课件原文）。  
  核心挑战：避免“子回路（Subtour）”（即仅访问部分节点形成的闭环）。

- **两大经典建模方法**：
  ##### （1）Dantzig-Fulkerson-Johnson（DFJ） formulation
  - 数据（Data）：节点集\(N\)、节点间距离\(d_{ij}\)；  
    辅助定义：\(\delta^+(S)=\{(i,j) \in A | i \in S, j \notin S\}\)（集合\(S\)的出边集），\(\delta^-(S)=\{(i,j) \in A | i \notin S, j \in S\}\)（集合\(S\)的入边集）。
  - 决策变量：\(x_{ij}= \begin{cases}1, & 访问节点i后立即访问节点j \\ 0, & 否则\end{cases}\)，\(x_{ij} \in \mathbb{B}\)。
  - 约束条件：  
    度约束：\(\sum_{j \in N} x_{ij}=1\)（\(\forall i\)，每个节点恰好有1条出边）；\(\sum_{i \in N} x_{ij}=1\)（\(\forall j\)，每个节点恰好有1条入边）；  
    子回路消除约束：\(\sum_{(i,j) \in \delta^+(S)} x_{ij} ≥1\)（\(\forall S \subset N, 2≤|S|≤n-1\)，任意非空真子集\(S\)至少有1条出边，避免子回路）。
  - 目标函数：\(\min \sum_{(i,j) \in A} d_{ij}x_{ij}\)。

  ##### （2）Miller-Tucker-Zemlin（MTZ） formulation
  - 核心改进：用“顺序变量”替代DFJ的指数级子回路约束，降低建模复杂度。
  - 新增决策变量：\(u_i\)为节点\(i\)在访问序列中的位置（整数变量，\(1≤u_i≤n\)）。
  - 子回路消除约束：\(u_i +1 -n(1-x_{ij}) ≤u_j\)（\(\forall i,j \neq1\)）；  
    逻辑：若\(x_{ij}=1\)（i后接j），则\(u_j ≥u_i+1\)，确保访问序列连续，无闭环。

- **历史里程碑**：Dantzig等（1954）首次用该模型求解49个城市的TSP，LP最优解为699（课件原文）。

#### 2. 车辆路径问题（Vehicle Routing Problem, VRP）
- **问题描述（Problem Description）**：  
  _“A homogeneous fleet of capacitated vehicles starts from the depot, serves each of the n customers (w/ demand) exactly once, returns to the depot; Find the shortest total travel distance”_（课件原文）。  
  核心是TSP的扩展：多车辆、带容量约束（单车辆服务的总需求量≤车辆容量\(Q\)）。

- **核心建模要素（以两索引车辆流模型为例）**：
  - 数据： depot（ depot节点0）、客户需求\(q_i\)（\(q_0=0\)）、车辆容量\(Q\)、车辆数量上限\(K\)。
  - 决策变量：\(x_{ij}= \begin{cases}1, & 某车辆行驶边(i,j) \\ 0, & 否则\end{cases}\)；\(u_i\)为车辆访问节点\(i\)后的剩余容量（或已装载量）。
  - 约束条件：  
    车辆数量约束：\(\sum_{j \in N} x_{0j} ≤K\)（从depot出发的车辆数≤\(K\)）；  
    客户访问约束：\(\sum_{j} x_{ji}=1\)且\(\sum_{j} x_{ij}=1\)（\(\forall i \neq0\)，每个客户恰好被访问1次）；  
    容量约束：\(u_i +q_j -Q(1-x_{ij}) ≤u_j\)（\(\forall i,j \neq0\)）；\(q_i ≤u_i ≤Q\)；  
    子回路消除：与容量约束结合，避免单车辆服务的节点形成子回路。
  - 目标函数：\(\min \sum_{(i,j) \in A} d_{ij}x_{ij}\)。

- **VRP的四大核心变体**：
  ##### （1）开放式车辆路径问题（Open VRP, OVRP）
  - 核心差异：_“Does not have to return to the depot”_（车辆无需返回depot，课件原文）。  
  - 建模调整：取消“车辆返回depot”的约束，仅保留“从depot出发”和“客户访问”约束。

  ##### （2）带时间窗车辆路径问题（VRP with Time Windows, VRPTW）
  - 核心新增约束：客户有服务时间窗\([e_i, l_i]\)（最早/最晚服务时间），车辆服务时间\(s_i\)、行驶时间\(t_{ij}\)。  
  - 新增决策变量：\(w_i\)为车辆开始服务节点\(i\)的时间。  
  - 时间约束：\(w_i ≥e_i\)且\(w_i ≤l_i\)（\(\forall i\)）；\(w_j ≥w_i +s_i +t_{ij} -W_{ij}(1-x_{ij})\)（\(\forall i,j\)，\(W_{ij}\)为足够大的常数）。

  ##### （3）带时间窗取送问题（Pickup and Delivery Problem with Time Windows, PDPTW）
  - 核心新增需求：客户分为取货节点（P）和送货节点（D），\(q_i=-q_{n+i}\)（取货量=送货量），且同一客户的取货必须先于送货。  
  - 新增约束：\(w_{n+i} ≥w_i +t_{i,n+i}\)（\(\forall i \in P\)，送货时间≥取货时间+行驶时间）；\(u_i^k +q_j -U_{ij}(1-x_{ij}^k) ≤u_j^k\)（车辆\(k\)的装载量约束）。

  ##### （4）三索引车辆流模型（Three-Index Vehicle Flow Model）
  - 决策变量扩展：\(x_{ij}^k\)（车辆\(k\)行驶边(i,j)）、\(u_i^k\)（车辆\(k\)访问节点\(i\)后的装载量）、\(w_i^k\)（车辆\(k\)服务节点\(i\)的时间）。  
  - 优势：更精准刻画单车辆的约束（容量、时间），避免两索引模型的冗余约束。


## 三、问题演进与核心建模逻辑（Problem Evolution & Core Logic）
### 1. 路径规划问题的演进链条（课件原文回顾）
\[
\text{TSP} \to \text{VRP} \to \text{OVRP} \to \text{VRPTW} \to \text{PDPTW}
\]
- 演进核心：从“单车辆、无约束、闭环”逐步扩展为“多车辆、带容量/时间窗/取送约束、开/闭环可选”。
- 建模逻辑迁移：子回路消除约束（TSP→VRP）→ 容量约束（VRP特有）→ 时间窗约束（VRPTW）→ 取送优先级约束（PDPTW）。

### 2. 高级建模的核心原则
1. **决策变量精准化**：根据问题特性选择变量类型（二元变量刻画“是/否”，整数变量刻画“数量”，连续变量刻画“距离/时间/容量”）。
2. **约束条件层次化**：基础约束（访问/需求/容量）→ 逻辑约束（服务分配→设施建设、取货→送货）→ 优化约束（子回路消除、时间窗）。
3. **目标函数聚焦化**：明确优化核心（最小成本/距离/最大覆盖/最小最大距离），避免多目标冲突。


## 四、核心概念中英文对照表（Key Concepts Glossary）
| 中文术语             | 英文术语                                              | 文档原文标识         |
| -------------------- | ----------------------------------------------------- | -------------------- |
| 最短路径问题         | Shortest Path Problem                                 | 第二章核心问题       |
| 切割下料问题         | Cutting Stock Problem                                 | 第二章核心问题       |
| 集合覆盖问题         | Set Covering Problem (SCP)                            | 第三章核心问题       |
| 最大覆盖问题         | Maximum Covering Problem (MCP)                        | 第三章核心问题       |
| P-中心问题           | P-Center Problem                                      | 第三章核心问题       |
| P-中位数问题         | P-Median Problem                                      | 第三章核心问题       |
| 旅行商问题           | Traveling Salesman Problem (TSP)                      | 第四章核心问题       |
| 车辆路径问题         | Vehicle Routing Problem (VRP)                         | 第四章核心问题       |
| 开放式车辆路径问题   | Open VRP (OVRP)                                       | VRP变体之一          |
| 带时间窗车辆路径问题 | VRP with Time Windows (VRPTW)                         | VRP变体之一          |
| 带时间窗取送问题     | Pickup and Delivery Problem with Time Windows (PDPTW) | VRP变体之一          |
| 子回路消除约束       | Subtour Elimination Constraints                       | TSP/VRP建模关键约束  |
| 流量平衡约束         | Flow Balance Constraints                              | 最短路径问题核心约束 |
| 时间窗约束           | Time Window Constraints                               | VRPTW/PDPTW核心约束  |
| DFJ建模方法          | Dantzig-Fulkerson-Johnson Formulation                 | TSP经典建模方法      |
| MTZ建模方法          | Miller-Tucker-Zemlin Formulation                      | TSP简化建模方法      |