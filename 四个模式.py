

import numpy as np
from itertools import combinations

# 编号为1到4的四个球
balls = [1, 2, 3, 4,5,6,7,8]

# 存储有效的分配方式
valid_assignments = []

import math


# 定义 G1 和 G2
G1 = math.sqrt(1.3)
G2 = math.sqrt(1.2)

# 根据 G1 和 G2 计算 g1 和 g2
g1 = math.sqrt(G1**2 - 1)
g2 = math.sqrt(G2**2 - 1)


x = 0

# 计算 CM11, CM13, CM15, CM17, CM18
CM11 = G1**2 * G2**2 + G2**2 * g1**2 + g1**2 * g2**2 + G1**2 * g2**2
CM13 = 2 * G1**2 * G2 * g2 + 2 * G2 * g1**2 * g2
CM15 = 2 * G1 * G2 * g1 * g2 * math.cos(2*x)
CM16 = -2 * G1 * G2 * g1 * g2 * math.sin(2*x)
CM18 = 2 * G1 * G2**2 * g1 * math.sin(2*x)
CM111 = 2 * G1 * g1 * g2**2 *math. cos(2*x)
CM17 = -2 * G1 * G2**2 * g1 * math.cos(2*x)
CM112 = -2 * G1 * g1 * g2**2 * math.sin(2*x)


A = np.array([
 [CM11, 0, CM13, 0, CM15, CM16, -CM17, CM18, 0, 0, 0, 0, CM15,-CM16,CM111,CM112],
 [0, CM11, 0, -CM13, -CM16, CM15, CM18, CM17, 0, 0, 0, 0, CM16,CM15,CM112,-CM111],
 [CM13, 0, CM11, 0, CM111, CM112, CM15, -CM16, 0, 0, 0, 0, -CM17,CM18, CM15,CM16],
 [0, -CM13, 0, CM11, CM112, -CM111, CM16, CM15, 0, 0, 0, 0, CM18,CM17,-CM16,CM15],
 [CM15, -CM16, CM111, CM112, CM11, 0, CM13, 0,CM15,CM16,-CM17,CM18, 0, 0, 0, 0],
 [CM16, CM15, CM112, -CM111, 0, CM11, 0, -CM13, -CM16, CM15, CM18,CM17, 0, 0, 0, 0],
 [-CM17, CM18, CM15, CM16, CM13, 0, CM11, 0, CM111, CM112,CM15,-CM16, 0, 0, 0, 0],
 [CM18, CM17, -CM16, CM15, 0, -CM13, 0, CM11, CM112, -CM111, CM16,CM15, 0, 0, 0, 0],
 [0, 0, 0, 0, CM15, -CM16, CM111, CM112, CM11, 0, CM13, 0, CM15,CM16, -CM17, CM18],
 [0, 0, 0, 0, CM16, CM15, CM112, -CM111, 0, CM11, 0, -CM13, -CM16,CM15, CM18, CM17],
 [0, 0, 0, 0, -CM17, CM18, CM15, CM16, CM13, 0, CM11, 0, CM111, CM112,CM15, -CM16],
 [0, 0, 0, 0, CM18, CM17, -CM16, CM15, 0, -CM13, 0, CM11,CM112, -CM111, CM16, CM15],
 [CM15, CM16, -CM17, CM18, 0, 0, 0, 0, CM15, -CM16, CM111, CM112, CM11, 0, CM13, 0],
 [-CM16, CM15, CM18, CM17, 0, 0, 0, 0, CM16, CM15, CM112, -CM111, 0,CM11, 0, -CM13],
 [CM111, CM112, CM15, -CM16, 0, 0, 0, 0, -CM17, CM18, CM15, CM16,CM13, 0, CM11, 0],
 [CM112, -CM111, CM16, CM15, 0, 0, 0, 0, CM18, CM17, -CM16, CM15,0, -CM13, 0, CM11]
 ])
# 遍历所有可能的组合
for i in range(1, len(balls)//2 + 1):
    for combo in combinations(balls, i):
        basket1 = list(combo)  # 选择的组合作为篮子1
        basket2 = [ball for ball in balls if ball not in basket1]  # 剩余的球作为篮子2
        
        # 确保两个篮子都不为空
        if len(basket2) > 0:
            # 确保篮子1是较小的篮子
            if len(basket1) <= len(basket2):
                # 对篮子1和篮子2中的球进行排序
                basket1.sort()
                basket2.sort()
                
                # 检查篮子1和篮子2的球数量是否相等
                if len(basket1) == len(basket2):
                    # 当数量相等时，篮子1中必须含有编号1的球
                    if 1 in basket1:
                        # 添加单位矩阵
                        N = len(balls)
                        identity_matrix = np.eye(2 * N)
                        # 遍历篮子1中的所有编号
                        for ball in basket1:
                            k = ball * 2  # 计算k
                            identity_matrix[k - 1, k - 1] = -1  # 将对应位置的值设为-1
                        
                        # 计算转置矩阵乘以A再乘以单位矩阵
                        result_matrix = identity_matrix.T @ A @ identity_matrix
                        print(f"ppt {len(valid_assignments) + 1}：{basket1}，{basket2}")
                       
                        valid_assignments.append((basket1, basket2, result_matrix))
                else:
                    # 当数量不相等时，允许篮子1中不含编号1的球
                    # 添加单位矩阵
                    N = len(balls)
                    identity_matrix = np.eye(2 * N)
                    # 遍历篮子1中的所有编号
                    for ball in basket1:
                        k = ball * 2  # 计算k
                        identity_matrix[k - 1, k - 1] = -1  # 将对应位置的值设为-1
                        
                    # 计算转置矩阵乘以A再乘以单位矩阵
                    
                    result_matrix = identity_matrix.T @ A @ identity_matrix
                    
                    print(f"ppt {len(valid_assignments) + 1}: {basket1}，{basket2}")
                 
                    valid_assignments.append((basket1, basket2, result_matrix))


# 定义自定义矩阵B（示例）
B = np.array([[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0]])


# 遍历存储有效分配方式的列表valid_assignments
for assignment in valid_assignments:
    result_matrix = assignment[2]  # 获取结果矩阵
    # 将自定义矩阵B与结果矩阵相乘
    intermediate_result = B @ result_matrix
    
    # 将结果乘以虚数i
    complex_result = intermediate_result * 1j
    
    # 求特征值
    eigenvalues = np.linalg.eigvals(complex_result)
    
    # 筛选出特征值的正实数部分
    positive_real_parts = [eig.real for eig in eigenvalues if eig.real > 0]
    
    # 如果存在正实数部分，则找到正实数部分的最小值
    min_positive_real_part = min(positive_real_parts) if positive_real_parts else None
    
 
    print(f"{min_positive_real_part},")

# 打印最终结果
