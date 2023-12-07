/* Visit https://adventofcode.com/2023/day/6 to get your input */

#include <stdio.h>
#include <stdint.h>

static uint64_t solve(uint64_t time, uint64_t distance)
{
    uint64_t win = 0;
    for (uint64_t tm = 0; tm <= time; tm++) {
        if (tm * (time - tm) > distance)
            win++;
    }
    return win;
}

int main(void)
{
    uint64_t p1 = 1, p2;
    const uint64_t p1_time[] = { /* INPUT */ };
    const uint64_t p1_distance[] = { /* INPUT */ };
    const uint64_t p2_time = /* INPUT */;
    const uint64_t p2_distance = /* INPUT */;

    for (size_t i = 0; i < sizeof(p1_time) / sizeof(*p1_time); i++)
        p1 *= solve(p1_time[i], p1_distance[i]);
    p2 = solve(p2_time, p2_distance);

    printf("%lu %lu\n", p1, p2);
}
