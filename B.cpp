#include<iostream>
#include<algorithm>
#include<cstring>
#include<vector>
using namespace std;
using ll = long long;

signed main(){
    float x, y, z; cin >> x >> y >> z;
    float now = 0;
    float cnt = 0;
    // while (now < x) {
    //     now  = max(0, now - z);
    //     now += y;
    //     cnt++;
    // }

    cout << (x - y) / (y - z) + 1;
}
