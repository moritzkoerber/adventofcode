// Part 1
use std::collections::HashSet;
use std::fs;

pub fn run() {
    let input = fs::read_to_string("data/2022/day08.txt").unwrap();
    let p_input: Vec<Vec<i16>> = input
        .lines()
        .map(|line| {
            line.chars()
                .map(|c| c.to_digit(10).unwrap() as i16)
                .collect()
        })
        .collect();

    let mut visible: HashSet<(usize, usize)> = HashSet::new();

    let v = p_input.len();
    let h = p_input[0].len();

    for i in 0..v {
        let mut max_t: i16 = -1;
        for j in 0..h {
            if p_input[i][j] as i16 > max_t {
                visible.insert((i, j));
            }
            max_t = max_t.max(p_input[i][j] as i16);
        }

        let mut max_t: i16 = -1;
        for j in (0..h).rev() {
            if p_input[i][j] as i16 > max_t {
                visible.insert((i, j));
            }
            max_t = max_t.max(p_input[i][j] as i16);
        }
    }

    for j in 0..h {
        let mut max_t: i16 = -1;
        for i in 0..v {
            if p_input[i][j] as i16 > max_t {
                visible.insert((i, j));
            }
            max_t = max_t.max(p_input[i][j] as i16);
        }

        let mut max_t: i16 = -1;
        for i in (0..v).rev() {
            if p_input[i][j] as i16 > max_t {
                visible.insert((i, j));
            }
            max_t = max_t.max(p_input[i][j] as i16);
        }
    }
    println!("{}", visible.len());

    let mut scenic: u32 = 0;

    for i in 1..(v - 1) {
        for j in 1..(h - 1) {
            let tree = p_input[i][j];
            let mut r = 0;
            let mut l = 0;
            let mut d = 0;
            let mut u = 0;

            // right
            for idx in j + 1..h {
                r += 1;
                if tree <= p_input[i][idx] {
                    break;
                }
            }

            // left
            for idx in (0..j).rev() {
                l += 1;
                if tree <= p_input[i][idx] {
                    break;
                }
            }

            // down
            for idx in i + 1..v {
                d += 1;
                if tree <= p_input[idx][j] {
                    break;
                }
            }

            // up
            for idx in (0..i).rev() {
                u += 1;
                if tree <= p_input[idx][j] {
                    break;
                }
            }

            scenic = scenic.max(r * l * d * u)
        }
    }

    println!("{}", scenic);
}
