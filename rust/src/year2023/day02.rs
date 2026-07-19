use regex::Regex;
use std::fs;

pub fn run() {
    let p_input = fs::read_to_string("data/2023/day02.txt")
        .unwrap_or_else(|err| panic!("couldn't read data: {}", err));
    let re = Regex::new(r"\b(\d+)\s(\w+)\b").unwrap();
    let mut total = 0;
    for (i, mut line) in p_input
        .lines()
        .map(|line| re.captures_iter(line))
        .enumerate()
    {
        if !line.any(|cubes| {
            cubes[1].parse::<u32>().unwrap() > 14
                || (cubes[1].parse::<u32>().unwrap() > 13) && &cubes[2] == "green"
                || (cubes[1].parse::<u32>().unwrap() > 12) && &cubes[2] == "red"
        }) {
            total = total + i + 1;
        }
    }

    println!("{}", total)
}
