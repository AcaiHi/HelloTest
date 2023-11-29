#include<iostream>
#include<algorithm>
#include<cstring>
#include<vector>
using namespace std;
using ll = long long;

signed main(){
    int n; cin >> n;
    int q[n]; for (auto &it : q) cin >> it;
    int t; cin >> t;
    int s[t]; for (auto &it : s) cin >> it;

    int res = 0;
    for (auto x : s) {
        int f = x % 13 == 6;
        for (auto y : q) {
            
            if (x + 1 == y && (((x) / 13) == (y / 13)))
                f = 1;
            if (x - 1 == y &&( ((x) / 13) == (y / 13)))
                f = 1;
            
        }
        // cout << f << ' ' << x << endl;
        res += f;
    }

    cout << res;
}
