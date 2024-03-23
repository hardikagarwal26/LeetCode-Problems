/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int getHeight(TreeNode* root) {
        if(root == nullptr) return 0;
        int lH = getHeight(root->left);
        int rH = getHeight(root->right);
        if(lH == -1 || rH == -1 || abs(lH - rH) > 1) return -1;
        int height = 1 + max(lH, rH);
        return height;
    }

    bool isBalanced(TreeNode* root) {
        if(root == nullptr) return true;
        if(getHeight(root) == -1) return false;
        return true;
    }
};