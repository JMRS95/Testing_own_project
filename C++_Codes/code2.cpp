#include <iostream>
#include <string>

using namespace std;

void menu(){
    cout << "----------- MENU -----------\n";
    cout << "c: Count up to number 1000\n";
    cout << "h: Say hello\n";
    cout << "q: Quit\n";
}

bool condition(string input){
    if (input == "q"){
        cout << "Program finished";
        return false;
    }
    else if( input == "h"){
        cout << "Hello!\n";
    }
    else if( input == "c"){
        cout << "Counting up to number 1000:\n";
        for(int i {0};i<=1000;i++){
            cout << "Number: " << i << endl;
        }
    }
    else {
        cout << "Unknown option. Try again\n";
    }
    return true;
    }


int main() {
    string input {""};
    cout << "Initiating program':\n";
    bool cond {true};
    while (cond)
    {
        menu();
        cout << "Select an option: "; 
        cin >> input;
        cond = condition(input);
    }

    return 0;
}