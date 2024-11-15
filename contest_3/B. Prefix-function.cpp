// def Pi(S):
//     n = len(S)
//     P, l, r = [0] * n, 0, 1
//     while r < len(S):
//         if S[l] == S[r]:
//             P[r], r, l = l + 1, r + 1, l + 1
//         elif l:
//             l = P[l - 1]
//         else:
//             P[r], r = 0, r + 1
//     return P

// print(*Pi(input()))

#include <iostream>
#include <vector>
#include <string>

void Pi(const std::string &S)
{
    int n = S.size();
    std::vector<int> P(n, 0);
    int l = 0, r = 1;
    while (r < n)
    {
        if (S[l] == S[r])
        {
            P[r] = l + 1;
            r++;
            l++;
        }
        else
        {
            if (l == 0)
            {
                P[r] = 0;
                r++;
            }
            else
                l = P[l - 1];
        }
    }
    for (size_t i = 0; i < P.size(); i++)
        std::cout << P[i] << " ";
    std::cout << std::endl;
}

int main()
{
    std::string s;
    std::cin >> s;
    Pi(s);
}
