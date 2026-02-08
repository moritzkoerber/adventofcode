use std::fs;

pub fn run() {
    let p_input: String = fs::read_to_string("data/2022/day02.txt").unwrap();
    let mut outcomes_numeric = Vec::new();

    for game in p_input.lines() {
        if let Some((i, j)) = game.split_once(" ") {
            let (i, j): (i32, i32) = (
                i.as_bytes()[0] as i32 - 64,
                j.as_bytes()[0] as i32 - 64 - 23,
            );
            outcomes_numeric.push((i, j));
        }
    }

    // Part 1
    let mut total = 0;
    for (i, j) in &outcomes_numeric {
        let res = match j - i {
            -2 => 1,
            2 => -1,
            _ => j - i,
        };
        total = total + (res + 1) * 3 + j;
    }
    println!("{}", total);

    // Part 2
    let total: i32 = outcomes_numeric
        .iter()
        .map(|(i, j)| ((i + j) % 3) + 1 + (j - 1) * 3)
        .sum();
    println!("{}", total);
}
