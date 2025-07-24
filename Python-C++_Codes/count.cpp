#include <iostream>
using namespace std;

int main(){
    // Message
    std::cout << "Running C++ program:\n\n";

    // Limit number (N)
    int N {450000000};

    // Loop
    int i {0};
    while(i<N){
        i++;
    }

    // Message
    std::cout << "Counted up to number "<< i << "\n";
    return 0;
}