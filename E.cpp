#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

using PII = pair<int, int>;
#define x first
#define y second
#define mp make_pair

int main(){
    int n; cin >> n;
    vector<pair<int, PII> > v;

    while (n--) {
        int x, y ,z;
        cin >> x >> y >> z;

        v.push_back(mp(z, mp(x, y)));
    }

    sort(v.begin(), v.end());

    for (auto x : v) {
        cout << x.second.first << ' ' << x.second.second << ' ' << x.first << endl;
    }
}