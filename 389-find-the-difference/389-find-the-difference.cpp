class Solution {
public:
    void swap(char* x, char* y){
        char temp = *x;
        *x = *y;
        *y = temp;
    }

    string sort(string str){
        int n = str.length();
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n-i-1; j++){
                if(str[j] > str[j+1]) swap(&str[j], &str[j+1]);
            }
        }   
        return str;
    }
    char findTheDifference(string s, string t){
        int n = s.length();
        s = sort(s);
        t = sort(t);
        for(int i = 0; i < n; i++){
            if(s[i] == t[i]) continue;
            return t[i];
        }
        return t[n];
    }
};