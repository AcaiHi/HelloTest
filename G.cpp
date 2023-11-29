#include<iostream>
#include<vector>

using namespace std;

int dx[] = {0, 1, -1, 0, 1, 1, -1, -1};
int dy[] = {1, 0, 0, -1, 1, -1, 1, -1};

bool in(int x, int y) {
    return x >= 0 && x < 8 && y >= 0 && y < 8;
}



int main(){
    int q[8][8];
    for(auto &x : q)
        for (auto &y : x) {
            cin >> y;
        }
    int n = 8;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (q[i][j] == 1) {
                for (int k = 0; k < 8; k++) {
                    int ddx = dx[k], ddy = dy[k];
                    int w = 0;
                    for (int a = i + ddx, b = j + ddy; in(a, b); a += ddx, b += ddy) {
                        
                        if (q[a][b] == 0 || q[a][b] == 3 || q[a][b] == 1) {
                            if (w && q[a][b] == 0)
                                q[a][b] = 3;
                            break;
                        } else if (q[a][b] == 2) w++;
                    }

                }
            }
            
        }
    }
    

    // for (int i = 0; i < 8; i++) {
    //     for (int j = 0; j < 8; j++)
    //         if (q[i][j] == 2) {
    //             for (int x = 0; x < 8; x++) {
    //                 int a = i + dx[x], b = dy[x];
    //                 int i_a = dx[x] * -1, i_b = dy[x] * -1;
    //                 if (!in(a, b)) continue;
    //                 if (q[a][b] == 0) {
    //                     cout << a << ' ' << b << endl;
    //                     cout << i_a << ' ' << i_b << ' ' << dx[x] << ' ' << dy[x] << endl;
    //                     int f = 0;
    //                     int _a = i + i_a, _b = j + i_b;
    //                     while (in(_a, _b) && !f && (q[_a][_b] == 2 || q[_a][_b] == 1)) {
    //                         if (q[_a][_b] == 1) {
    //                             f = 1; break;
    //                         }
    //                         _a += i_a, _b += i_b;
    //                     }
    //                     cout << _a  << _b << f << endl;
    //                     if (f) q[a][b] = 3;
    //                 }
                        
    //                 // else if (q[a][b] == 0) {
    //                 //     int f = 0;
    //                 //     int _a = i + i_a, _b = j + i_b;
    //                 //     while (in(_a, _b)) {
    //                 //         if (q[_a][_b] == '1') {
    //                 //             f = 1; break;
    //                 //         }
    //                 //         _a += i_a, _b += i_b;
    //                 //     }

    //                 //     if (f) q[a][b] = 3;
    //                 // }
    //             }
    //         }
    // }
    int cnt = 0;
    for(auto &x : q){
        for (auto &y : x) {
            if (y == 3) cnt++;
            // cout << y << ' ';
        } 
    }

    cout << cnt << endl;
}