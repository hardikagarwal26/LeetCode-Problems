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
    void dfs(TreeNode* node, int &ans, int depth) {
        if(!node) return;
        if(!node->left && !node->right) {
            ans = min(ans, depth);
            return;
        }
        dfs(node->left, ans, depth + 1);
        dfs(node->right, ans, depth + 1);
    }

    int minDepth(TreeNode* root) {
        if(!root) return 0;
        int ans = INT_MAX;
        dfs(root, ans, 1);
        return ans;
    }
};