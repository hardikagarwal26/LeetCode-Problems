class Solution {
public:
    int countStudents(vector<int>& students, vector<int>& sandwiches) {
        vector<int> req(2, 0);
        for (const int& student : students)
            req[student]++;

        for (const int& sandwich : sandwiches) {
            if (req[sandwich] == 0)
                return req[1 - sandwich];
            else
                req[sandwich]--;
        }

        return 0;
    }
};