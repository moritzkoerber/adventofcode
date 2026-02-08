// Part 1 + 2
use std::fs;

pub fn run() {
    let p_input: String = fs::read_to_string("data/2022/day01.txt").unwrap();
    let mut calories_by_elf: Vec<u32> = p_input
        .split("\n\n")
        .map(|block| block.lines().map(|line| line.parse::<u32>().unwrap()).sum())
        .collect();

    calories_by_elf.sort_unstable_by(|a, b| b.cmp(a));

    println!("{}", calories_by_elf[0]);
    println!("{}", calories_by_elf.iter().take(3).sum::<u32>());
}
