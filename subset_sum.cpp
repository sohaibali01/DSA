#include <iostream>
#include <cstdio>
#include<vector>
using namespace std;


vector<vector<int>> two_sum_On2(vector<int> &arr, int S)
{
    vector<vector<int>> outputList;
    vector<int> outsingle=vector<int>(2);
    for (int item: arr)
        for (int item2: arr) 
        {
            if ( (item!=item2) && (item+item2==S))
            {
              outsingle[0] = item;
              outsingle[1] = item2;
              outputList.push_back(outsingle);
            }
        }
    return outputList;
}

vector<vector<int>> two_sum_Onlog2n(vector<int> arr, int S)
{
    vector<vector<int>> outputList;
    vector<int> outsingle=vector<int>(2);
    
    std::sort(arr.begin(), arr.end());
     
    for (int item: arr)
    {
        if (std::binary_search(arr.begin(), arr.end(), S-item))
        {
            if ( item!=S-item)
            {
              outsingle[0] = item;
              outsingle[1] = S-item;
              outputList.push_back(outsingle);
            }
        }
    }
    return outputList;
}

vector<vector<int>> two_sum_On(vector<int> arr, int S)
{
    vector<vector<int>> outputList;
    vector<int> outsingle=vector<int>(2);
    
    unordered_map<int,int> hashMap;

    for (int item: arr)
        hashMap[item] = S-item;
             
    for (int item: arr)
    {
        if (hashMap.find(S-item)!=hashMap.end())
        {
              outsingle[0] = item;
              outsingle[1] = S-item;
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
