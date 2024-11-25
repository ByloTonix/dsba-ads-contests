#include <iostream>
#include <fstream>
#include <unordered_map>
#include <vector>

class Trie
{
public:
    std::unordered_map<char, Trie *> son;
    int value = 0;
};

std::string add(Trie *root, const std::string &var, int i)
{
    Trie *x = root;
    for (char c : var)
    {
        if (x->son.find(c) == x->son.end())
            x->son[c] = new Trie();
        x = x->son[c];
    }
    x->value += i;
    return std::to_string(x->value);
}

int main()
{
    Trie *root = new Trie();
    std::vector<std::string> arr;
    std::ifstream fin("incrementor.in");

    if (fin.is_open())
    {
        std::string line;
        while (std::getline(fin, line))
        {
            size_t space_pos = line.find(' ');
            std::string var = line.substr(0, space_pos);
            int value = std::stoi(line.substr(space_pos + 1));
            arr.push_back(add(root, var, value));
        }
        fin.close();
    }

    for (const auto &res : arr)
        std::cout << res << "\n";
}

#include <iostream>
#include <fstream>
#include <unordered_map>
#include <vector>

class TrieNode
{
public:
    std::unordered_map<char, TrieNode*> children;
    int value = 0;

    ~TrieNode()
    {
        for (auto &child: children)
            delete child.second;
    }

    int add(const std::string &key, int i)
    {
        TrieNode *node = this;
        for (char c: key)
        {
            if (node->children[c] == nullptr)
                node->children[c] = new TrieNode();
            node = node->children[c];
        }
        node->value += i;
        return node->value;
    }
};

std::pair<std::string, int> parseLine(const std::string &line)
{
    size_t pos = line.find(" ");
    std::string key = line.substr(0, pos);
    int value = std::stoi(line.substr(pos + 1));
    return {key, value};
}

int main()
{
    TrieNode root;
    std::vector<std::string> answer;
    std::ifstream input("incrementator.in");
    std::string line;

    while (std::getline(input, line))
    {
        auto [key, value] = parseLine(line);
        answer.push_back(std::to_string(root.add(key, value)));
    }

    for (const auto &el : answer)
        std::cout << el << "\n";

    return 0;
}
