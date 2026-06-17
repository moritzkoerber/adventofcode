// Part 1 + 2
use std::char;
use std::collections::HashSet;

fn count_overlap<const N: usize>(compartments: [&str; N]) -> i32 {
    let mut comp1: HashSet<char> = compartments[0].chars().collect();
    for part in &compartments[1..] {
        let comp2: HashSet<char> = part.chars().collect();
        comp1 = comp1.intersection(&comp2).copied().collect();
    }

    let letter = comp1.into_iter().next().unwrap();
    letter as i32 - 38 - 58 * letter.is_lowercase() as i32
}

pub fn run() {
    let compartments = crate::input::read(2022, 3);

    let mut total = 0;
    for c in compartments.lines() {
        let i = c.chars().count() / 2;
        let f = count_overlap([&c[0..i], &c[i..]]);
        total += f;
    }
    println!("{}", total);

    total = 0;
    let lines: Vec<&str> = compartments.lines().collect();
    let l = lines.len();
    for i in (0..l).step_by(3) {
        let f = count_overlap([lines[i], lines[i + 1], lines[i + 2]]);
        total += f
    }
    println!("{}", total);
}
