# Python
## Part 1
import re

with open("data.txt") as f:
    blueprints = [list(map(int, re.findall(r"\d+", e))) for e in f.read().splitlines()]


def solve(
    blueprint: list,
    time_limit: int,
) -> int:
    (
        ore_r_cost,
        clay_r_cost,
        obs_r_cost1,
        obs_r_cost2,
        geo_r_cost1,
        geo_r_cost2,
    ) = blueprint

    solved = {}

    max_o_r, max_c_r, max_obs_r = (
        max(clay_r_cost, obs_r_cost1, geo_r_cost1),
        obs_r_cost2,
        geo_r_cost2,
    )

    def dfs(
        o_r: int,
        c_r: int,
        obs_r: int,
        geo_r: int,
        ore: int,
        clay: int,
        obs: int,
        geo: int,
        time_left: int,
    ) -> int:
        if time_left == 0:
            return geo

        key = (o_r, c_r, obs_r, geo_r, ore, clay, obs, geo, time_left)
        if key in solved:
            return solved[key]

        try_solve = [0]

        if ore >= geo_r_cost1 and obs >= geo_r_cost2:
            res = dfs(
                o_r,
                c_r,
                obs_r,
                geo_r + 1,
                ore - geo_r_cost1 + o_r,
                clay + c_r,
                obs - geo_r_cost2 + obs_r,
                geo + geo_r,
                time_left - 1,
            )

            solved[key] = res
            return res

        if ore >= ore_r_cost and o_r < max_o_r:
            build_ore = dfs(
                o_r + 1,
                c_r,
                obs_r,
                geo_r,
                ore - ore_r_cost + o_r,
                clay + c_r,
                obs + obs_r,
                geo + geo_r,
                time_left - 1,
            )
            try_solve.append(build_ore)

        if ore >= clay_r_cost and c_r < max_c_r:
            build_clay = dfs(
                o_r,
                c_r + 1,
                obs_r,
                geo_r,
                ore - clay_r_cost + o_r,
                clay + c_r,
                obs + obs_r,
                geo + geo_r,
                time_left - 1,
            )
            try_solve.append(build_clay)

        if ore >= obs_r_cost1 and clay >= obs_r_cost2 and obs_r < max_obs_r:
            build_obs = dfs(
                o_r,
                c_r,
                obs_r + 1,
                geo_r,
                ore - obs_r_cost1 + o_r,
                clay - obs_r_cost2 + c_r,
                obs + obs_r,
                geo + geo_r,
                time_left - 1,
            )
            try_solve.append(build_obs)

        res = max(
            dfs(
                o_r,
                c_r,
                obs_r,
                geo_r,
                ore + o_r,
                clay + c_r,
                obs + obs_r,
                geo + geo_r,
                time_left - 1,
            ),
            *try_solve,
        )
        solved[key] = res
        return res

    return dfs(
        o_r=1,
        c_r=0,
        obs_r=0,
        geo_r=0,
        ore=0,
        clay=0,
        obs=0,
        geo=0,
        time_left=time_limit,
    )


quality_level = sum(solve(blueprint, 24) * idx for idx, *blueprint in blueprints)
print(quality_level)


## Part 2
geodes = 1
for _, *blueprint in blueprints[:3]:
    geodes *= solve(blueprint, 32)

print(geodes)
