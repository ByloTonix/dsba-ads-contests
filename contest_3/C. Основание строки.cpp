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
  std::cout << n - P[n - 1];
}

int main()
{
  std::string s;
  std::cin >> s;
  Pi(s);
}
