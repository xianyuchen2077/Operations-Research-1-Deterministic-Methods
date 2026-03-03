### 2(a) Formulation of the Linear Programming (LP) Model  

#### Notation Definition  
- Let \( x_1 \) denote the number of units of Product 1 to produce.  
- Let \( x_2 \) denote the number of units of Product 2 to produce, with \( x_2 \leq 20 \) 


#### Objective Function  
To maximize the total profit \( Z \). Each unit of Product 1 generates a profit of $1, 

and each unit of Product 2 (up to 20 units) generates a profit of $2.
 Thus:  
\[
Z = 1 \cdot x_1 + 2 \cdot x_2
\]  


#### Constraints  
1. **Metal Frame Parts Constraint**: Each unit of Product 1 requires 1 unit of frame parts, and each unit of Product 2 requires 3 units of frame parts. The company has 200 units of frame parts in total. Hence:  
\[
x_1 + 3x_2 \leq 200
\]  

2. **Electrical Components Constraint**: Each unit of Product 1 requires 2 units of electrical components, and each unit of Product 2 requires 2 units of electrical components. The company has 300 units of electrical components in total. Thus:  
\[
2x_1 + 2x_2 \leq 300
\]  

3. **Non-negativity and Upper Limit for Product 2**: The production quantities cannot be negative, and the quantity of Product 2 cannot exceed 20 units. Therefore:  
\[
x_1 \geq 0, \quad x_2 \geq 0, \quad x_2 \leq 20
\]  


In summary, the complete linear programming model is:  
\[
\begin{cases}
\text{Maximize} & Z = x_1 + 2x_2 \\
\text{Subject to} & x_1 + 3x_2 \leq 200 \\
& 2x_1 + 2x_2 \leq 300 \\
& x_2 \leq 20 \\
& x_1 \geq 0, \quad x_2 \geq 0
\end{cases}
\]