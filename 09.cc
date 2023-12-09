#include <algorithm>
#include <cerrno>
#include <cstdint>
#include <cstdio>
#include <stdexcept>
#include <string>
#include <system_error>
#include <vector>

using i64 = int64_t;

static std::vector<std::string> read_all(const char *name)
{
    FILE *fp = fopen(name, "rb");
    if (fp == nullptr)
        throw std::system_error(errno, std::generic_category(), name);

    int ch;
    std::string temp;
    std::vector<std::string> vs;

    while ((ch = fgetc(fp)) != EOF) {
        if (ch == '\n') {
            vs.push_back(temp);
            temp.clear();
        } else {
            temp += static_cast<char>(ch);
        }
    }

    fclose(fp);
    return vs;
}

static void parse_input(const std::string line, std::vector<i64> &out)
{
    i64 v = 0;
    i64 sign = 1;

    for (char ch : line) {
        if (ch == ' ') {
            out.push_back(v * sign);
            v = 0;
            sign = 1;
        } else if (ch == '-') {
            sign = -1;
        } else {
            v *= 10;
            v += ch - '0';
        }
    }

    out.push_back(v * sign);
}

static i64 extrapolate(const std::vector<i64> in)
{
    i64 res = 0;
    std::vector<i64> tmp = in, tmp2;

    while (true) {
        if (std::all_of(tmp.begin(), tmp.end(), [](i64 i){ return i == 0; }))
            break;
        tmp2.clear();
        for (size_t i = 0; i < tmp.size() - 1; ++i)
            tmp2.push_back(tmp[i + 1] - tmp[i]);
        res += tmp[tmp.size() - 1];
        tmp = tmp2;
    }

    return res;
}

int main(int argc, char **argv)
{
    if (argc != 2)
        throw std::invalid_argument("input needed");

    i64 p1 = 0, p2 = 0;
    std::vector<i64> in;
    std::vector<std::string> lines = read_all(argv[1]);

    for (const std::string &line : lines) {
        in.clear();
        parse_input(line, in);
        p1 += extrapolate(in);
        std::reverse(in.begin(), in.end());
        p2 += extrapolate(in);
    }

    printf("%ld, %ld\n", p1, p2);
}
