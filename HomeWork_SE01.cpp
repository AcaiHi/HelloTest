#include<iostream>

class Student {
private:
    
    int ID;
    int EN;
    int Math;
    int res;
    int dres;
    
    void setRes();
    void setDres();
    void setID(int x);
    void setEN(int x);
    void setMath(int x);

public:
    Student(int x, int y, int z){
        setID(x);
        setEN(y);
        setMath(z);
    }
    void input_data();
    void show_data();
};

// 在類的外部實現成員函數
void Student::setRes() {
    res = EN + Math;
}

void Student::setDres() {
    dres = (EN + Math) / 2;
}

void Student::setID(int x) {
    ID = x;
}

void Student::setEN(int x) {
    EN = x;
}

void Student::setMath(int x) {
    Math = x;
}

void Student::show_data() {
    setRes();
    setDres();
    std::cout << "您的學號為: " << ID << std::endl;
    std::cout << "總分: " << res << " 平均為 " << dres << std::endl;
}

void Student::input_data(){
    int x;
    std::cout << "輸入學號: "; std::cin >> x;
    setID(x);
    std::cout << "輸入英文成績: "; std::cin >> x;
    setEN(x);
    std::cout << "輸入數學成績: "; std::cin >> x;
    setMath(x);
}

void GetData(int &x, int &y, int &z) {
    std::cout << "輸入學號: "; std::cin >> x;
    std::cout << "輸入英文成績: "; std::cin >> y;
    std::cout << "輸入數學成績: "; std::cin >> z;
}
int main() {
    int x, y, z; GetData(x, y, z);
    Student tt = Student(x, y, z);
    tt.show_data();
    return 0;
}
