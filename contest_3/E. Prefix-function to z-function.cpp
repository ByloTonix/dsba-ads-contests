#include <iostream>
#include <vector>

int main()
{
    int n;
    std::cin >> n;
    std::vector<int> k(n);
    for (size_t i = 0; i < n; i++)
        std::cin >> k[i];

    std::vector<int> Z(n, 0);

    for (size_t i = 1; i < n; i++)
    {
        if (k[i])
            Z[i - k[i] + 1] = k[i];
    }

    int i = 1;
    while (i < n)
    {
        int j = 1;
        while (j < Z[i])
        {
            int v = std::min(Z[j], Z[i] - j);
            if (v < Z[i + j])
                break;
            Z[i + j] = v;
            j++;
        }
        i += j;
    }

    for (int num : Z)
        std::cout << num << " ";
    std::cout << std::endl;
}
