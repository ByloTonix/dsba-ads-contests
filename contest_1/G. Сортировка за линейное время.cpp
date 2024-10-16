#include <iostream>
#include <algorithm>

typedef unsigned long long int64;
typedef unsigned int int32;

unsigned int cur = 0;
const int MAX_SIZE = 50000;
const unsigned int BASE = 256;

inline int64 nextRand24(const int64 &a, const int64 &b)
{
    cur = cur * a + b;
    return (cur >> 8);
}

inline int64 nextRand32(const int64 &a, const int64 &b)
{
    return (nextRand24(a, b) << 8) ^ nextRand24(a, b);
}

void countSort(int64 arr[], const int32 &n, const int64 &exponent)
{
    int64 count[BASE] = {0};
    int64 *temp = new int64[n];

    for (size_t i = 0; i < n; i++)
        count[(arr[i] / exponent) % BASE]++;

    for (size_t i = 1; i < BASE; i++)
        count[i] += count[i - 1];

    for (int i = n - 1; i >= 0; i--)
    {
        int64 index = (arr[i] / exponent) % BASE;
        temp[--count[index]] = arr[i];
    }

    for (size_t i = 0; i < n; i++)
        arr[i] = temp[i];

    delete[] temp;
}

void radixSort(int64 arr[], const int32 &n)
{
    int64 max = *std::max_element(arr, arr + n);

    for (int64 exp = 1; max / exp > 0; exp *= BASE)
        countSort(arr, n, exp);
}

int main()
{
    int64 t;
    std::cin >> t;

    int64 n, a, b;
    std::cin >> n >> a >> b;
    int64 arr[MAX_SIZE];

    while (t-- > 0)
    {
        for (int64 i = 0; i < n; i++)
            arr[i] = nextRand32(a, b);

        radixSort(arr, n);

        int64 answer = 0;
        for (int64 i = 0; i < n; i++)
            answer += arr[i] * (i + 1);

        std::cout << answer << "\n";
    }
}
