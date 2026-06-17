// Part 1
use std::char;
use std::collections::HashSet;

fn count_overlap(comp1: &str, comp2: &str) -> i32 {
    let comp1: HashSet<char> = comp1.chars().collect();
    let comp2: HashSet<char> = comp2.chars().collect();

    let mut overlap = comp1.intersection(&comp2);
    let letter = *overlap.next().unwrap();
    letter as i32 - 38 - 58 * letter.is_lowercase() as i32
}

pub fn run() {
    let compartments = crate::input::read(2022, 3);
    let mut total = 0;
    for c in compartments.lines() {
        let i = c.chars().count() / 2;
        let f = count_overlap(&c[0..i], &c[i..]);
        total += f;
    }
    println!("{}", total)
}
