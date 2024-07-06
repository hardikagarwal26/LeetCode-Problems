class Solution {
public:
    int passThePillow(int n, int time) {
        int turn=time / (n-1);
        int pos=time % (n-1);
        if(turn%2){
            return n-pos;
        }
        return pos+1;
    }
};