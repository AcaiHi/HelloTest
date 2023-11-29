#include<iostream>
#include<algorithm>
#include<cstring>
#include<vector>
#include<map>
using namespace std;
using ll = long long;

signed main(){
  int t = 1;
  cin >> t;
  map<char, int>  m;
  while (t--) {
    char x; cin >> x;
    m[x] ++;
  }

  for (auto x : m)
    cout << x.first << " " << x.second << endl;
}
