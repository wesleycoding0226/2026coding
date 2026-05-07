#week11-5.py
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def helper(root, level):
            if root==None: return
            if len(ans) <= level:
                ans.append( root.val )
            else:
                ans[level] = root.val

            helper(root.left, level+1)
            helper(root.right, level+1)

        helper(root, 0)
        return ans
