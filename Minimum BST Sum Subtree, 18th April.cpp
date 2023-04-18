vector<int> help(Node* root,int target,int &ans){
        if(!root)return {1,0,0,INT_MAX,INT_MIN};
        vector<int> l = help(root->left,target,ans);
        vector<int> r = help(root->right,target,ans);
        if(root->data<=l[4] || root->data>=r[3])return {0,0,0,0,0};
        int sum = root->data+l[2]+r[2];
        int n = 1+l[1]+r[1];
        if(l[0]==1 && r[0]==1 && sum==target){
            ans=min(ans,n);
        }
        return {l[0]&r[0],n,sum,min(l[3],root->data),max(r[4],root->data)};
        
    }
    int minSubtreeSumBST(int target, Node *root) {
        // code here
        int ans = INT_MAX;
        vector<int> temp = help(root,target,ans);
        if(temp[0]==1 and temp[2]==target){
            ans=min(ans,temp[1]);
        }
        if(ans==INT_MAX)return -1;
        return ans;
    }
