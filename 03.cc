#include <cerrno>
#include <cstdio>
#include <cstdint>
#include <cctype>
#include <charconv>
#include <string>
#include <vector>
#include <system_error>
#include <utility>
#include <unordered_map>
#include <functional>

static std::vector<std::string> read_all(const char *fname)
{
    FILE *fp = fopen(fname, "rb");
    if (fp == NULL)
        throw std::system_error(errno, std::generic_category(), fname);

    int ch;
    std::string s;
    std::vector<std::string> vec;

    s.reserve(256);
    vec.reserve(256);

    while ((ch = fgetc(fp)) != EOF) {
        if (ch == '\n') {
            vec.push_back(s);
            s.clear();
        } else {
            if (ch == '.')
                ch = ' ';
            s += static_cast<char>(ch);
        }
    }

    fclose(fp);
    return vec;
}

static size_t get_number(const std::string &s, size_t x, uint64_t &out)
{
    const char *first = s.data() + x, *last = first;

    while (*last != '\0' && isdigit(*last))
        last++;

    std::from_chars(first, last, out);
    return static_cast<size_t>(last - first);
}

static bool check_symbol(const std::vector<std::string> &grid, size_t y,
                         size_t x, size_t num_size)
{
    bool has_neighbour = false;
    size_t y_start = y > 0 ? y - 1 : y;
    size_t y_end = y < grid.size() - 1 ? y + 1 : y;
    size_t x_start = x > 0 ? x - 1 : x;
    size_t x_end = x + num_size < grid[y].size() ? x + num_size : x;

    for (size_t dy = y_start; dy <= y_end; dy++) {
        for (size_t dx = x_start; dx <= x_end; dx++) {
            if (dy == y && dx == x)
                continue;
            if (ispunct(grid[dy][dx]))
                has_neighbour = true;
        }
    }

    return has_neighbour;
}

class phash {
public:
    template <class T1, class T2>
    size_t operator()(const std::pair<T1, T2> &K) const
    {
        return std::hash<T1>{}(K.first) ^ std::hash<T2>{}(K.second);
    }
};

static void check_number(size_t y, size_t x,
                         const std::vector<std::string> &grid,
                         std::unordered_map<std::pair<size_t, size_t>,
                                            uint64_t, phash> &num,
                         std::vector<uint64_t> &out)
{
    std::pair<size_t, size_t> coord;
    size_t y_start = y > 0 ? y - 1 : y;
    size_t y_end = y < grid.size() - 1 ? y + 1 : y;
    size_t x_start = x > 0 ? x - 1 : x;
    size_t x_end = x < grid[y].size() - 1 ? x + 1 : x;

    printf("Symbol at (%zu, %zu)\n", y, x);
    printf("y_start = %zu, y_end = %zu\n", y_start, y_end);
    printf("x_start = %zu, x_end = %zu\n", x_start, x_end);

    for (size_t dy = y_start; dy <= y_end; dy++) {
        for (size_t dx = x_start; dx <= x_end; dx++) {
            if (dy == y && dx == x)
                continue;
            coord = std::make_pair(dy, dx);
            if (num.find(coord) != num.end())
                printf("%lu\n", num[coord]);
        }
    }

    (void)out;
}

int main(int argc, char **argv)
{
    if (argc < 2) return 1;

    size_t x_step;
    uint64_t part1 = 0;
    std::vector<std::string> grid = read_all(argv[1]);

    std::vector<std::pair<size_t, size_t>> gear;
    std::unordered_map<std::pair<size_t, size_t>, uint64_t, phash> number;

    gear.reserve(256);
    number.reserve(256);

    for (size_t y = 0; y < grid.size(); y++) {
        size_t x = 0;
        const std::string &line = grid[y];
        while (x < line.size()) {
            const char ch = line[x];
            if (isdigit(ch)) {
                uint64_t num = 0;
                x_step = get_number(line, x, num);
                if (check_symbol(grid, y, x, x_step))
                    part1 += num;
                number[std::make_pair(y, x)] = num;
            } else {
                x_step = 1;
            }
            if (ch == '*')
                gear.push_back(std::make_pair(y, x));
            x += x_step;
        }
    }

    std::vector<size_t> temp;
    temp.reserve(16);

    for (const std::pair<size_t, size_t> &coord : gear) {
        const size_t y = coord.first;
        const size_t x = coord.second;
        check_number(y, x, grid, number, temp);
        if (temp.size() == 2)
            printf("(%zu, %zu)\n", y, x);
        temp.clear();
    }
//    printf("%lu\n", part1);
}
