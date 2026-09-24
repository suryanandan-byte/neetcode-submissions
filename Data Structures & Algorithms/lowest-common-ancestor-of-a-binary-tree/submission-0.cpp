/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
TreeNode* fun(TreeNode*root,int& p,int& q){
    if(root == nullptr || root->val == p || root->val == q)return root;
    TreeNode* left=fun(root->left,p,q);
    TreeNode* right=fun(root->right,p,q);
    if(left && right)return root;
    if(left)return left;
    return right;
}
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        return fun(root,p->val,q->val);
    }
};