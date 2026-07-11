use regex::Regex;
use std::collections::HashMap;
use std::fs;

pub fn run() {
    let p_input = fs::read_to_string("data/2023/day01.txt")
        .unwrap_or_else(|err| panic!("couldn't read data: {}", err));
    let re_part1 = Regex::new(r"\d").unwrap();

    let part1: u32 = p_input
        .lines()
        .map(|line| re_part1.find_iter(line).map(|m| m.as_str()))
        .map(|mut res| {
            let first = res.next().unwrap();
            let second = res.last().unwrap_or(first);
            format!("{}{}", first, second).parse::<u32>().unwrap()
        })
        .sum();
    println!("{part1}");

    let mut digits = HashMap::new();

    digits.insert(String::from("one"), "1");
    digits.insert(String::from("two"), "2");
    digits.insert(String::from("three"), "3");
    digits.insert(String::from("four"), "4");
    digits.insert(String::from("five"), "5");
    digits.insert(String::from("six"), "6");
    digits.insert(String::from("seven"), "7");
    digits.insert(String::from("eight"), "8");
    digits.insert(String::from("nine"), "9");

    let mut pattern = digits
        .keys()
        .map(String::as_str)
        .collect::<Vec<&str>>()
        .join("|");

    pattern.push_str(r"|\d");
    let re_part2 = Regex::new(&pattern).unwrap();

    let part2: u32 = p_input
        .lines()
        .map(|line| {
            let mut solution = Vec::new();
            for i in 0..line.len() {
                let s = re_part2.find(&line[i..]).map(|m| m.as_str()).unwrap_or("");
                if !s.is_empty() {
                    solution.push(digits.get(s).copied().unwrap_or(s))
                }
            }
            let first = solution.first().unwrap();
            let second = solution.last().unwrap_or(first);
            format!("{}{}", first, second).parse::<u32>().unwrap()
        })
        .sum();

    println!("{part2}");
}
