import torch

# x = torch.tensor([1, 2, 3, 4, 5])
# y = torch.tensor([10, 20, 30, 40, 50])

# condition = x > 3

# result = torch.where(condition, x, y)

# print(result)   # Output:tensor([10, 20, 30, 4, 5])

# t = torch.arange(0, 10, 2)
# print(t)    # Output:tensor([0, 2, 4, 6, 8])

# t = torch.arange(5, 0, -1)
# print(t)    # Output:tensor([5, 4, 3, 2, 1])

# v1=torch.tensor([1,2,3])
# v2=torch.tensor([4,5,6])
# result=torch.outer(v1,v2)
# print(result)

# t1=torch.tensor([[1,2,3],[4,5,6]])
# t2=torch.tensor([[7,8,9],[10,11,12]])
# result=torch.cat((t1,t2),dim=0)
# print(result)  

# result2=torch.cat((t1,t2),dim=1)
# print(result2)  

# t1 = torch.Tensor([1, 2, 3])
# t2 = t1.unsqueeze(0)
# print(t2)