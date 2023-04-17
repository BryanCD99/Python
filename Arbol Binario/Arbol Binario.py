#Definition for a binary tree node
class TreeNode:
    def __init__(self,val = 0,left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

#My solution
def pre_order_traversal(root,n):
    if root:
        if(n == 0):
            print("Raiz: ", root.val)
        if (n == 1):
            print("izquierda: ", root.val)
        if (n == 2):
            print("derecha: ", root.val)
        pre_order_traversal(root.left,1)
        pre_order_traversal(root.right,2)

def SumOLeftLeaves(root: TreeNode):
    #pre_order_traversal(root,0)
    def dfs(node, is_left):
        if not node:
            return 0
        if node.left is None and node.right is None:
            #print(node.val)
            return node.val if is_left else 0
        return dfs(node.left, True) + dfs(node.right, False)
    return dfs(root, False)


#Create tree node
def CreateTree(arr):
    if arr is None or len(arr) == 0 or not arr[0].isnumeric():
        return None
    treeNodeQueue = []
    intergerQueue = []

    for a in arr:
        intergerQueue.append(a)

    treeNode = TreeNode(int(intergerQueue.pop(0)))
    treeNodeQueue.append(treeNode)

    while intergerQueue != []:
        leftVal = None if (intergerQueue == []) else intergerQueue.pop(0)
        rigthVal = None if (intergerQueue == []) else intergerQueue.pop(0)
        current = treeNodeQueue.pop(0)

        if leftVal and leftVal.isnumeric():
            left = TreeNode(int(leftVal))
            current.left = left
            treeNodeQueue.append(left)

        if rigthVal and rigthVal.isnumeric():
            right = TreeNode(int(rigthVal))
            current.right = right
            treeNodeQueue.append(right)

    return treeNode

if __name__ == "__main__":
    line = input()
    components = line.strip().split(",")
    root = CreateTree(components)

    print(SumOLeftLeaves(root))