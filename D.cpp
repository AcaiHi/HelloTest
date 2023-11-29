#include<iostream>
#include<map>
using namespace std;

int main(){

    int t; cin >> t;
    while (t--) {
        int n; cin >> n;
        string x; cin >> x;
        if (x == "123" || x == "Tom" || x == "DTGD") {
            cout << "123 Tom DTGD\n";
        } else if (x == "456" || x == "Cat" || x == "CSIE") {
            cout << "456 Cat CSIE\n";
        } else if (x == "789" || x == "Nana" || x == "ASIE") {
            cout << "789 Nana ASIE\n";
        } else if (x == "321" || x == "Lim" || x == "DBA") {
            cout << "321 Lim DBA\n";
        } else cout << "654 Won FDD\n";
    }
}