#include <iostream>
#include <cstdio>
#include<vector>
using namespace std;


vector<vector<int>> two_sum_On(vector<int> &arr, int S)
{
    vector<vector<int>> outputList;
    vector<int> outsingle=vector<int>(2);
    for (int item: arr)
        for (int item2: arr) 
        {
            if (item!=item2 and item+item2==S)
            {
              outsingle[0] = item;
              outsingle[1] = item2;
              outputList.push_back(outsingle);
            }
        }
    return outputList;
}

int main() {
    vector<int> arr = vector<int>{3,5,2,-4,8,11};
    vector<vector<int>> out = two_sum_On(arr, 7);
    for (auto item: out)
        cout<<item[0] << ' ' << item[1] << '\n';
    return 0;
}
