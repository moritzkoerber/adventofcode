use std::env;

mod year2022;

fn main() {
    let args: Vec<String> = env::args().collect();

    if args.len() != 3 {
        eprintln!("Usage: cargo run <year> <day>");
        eprintln!("Example: cargo run 2022 01");
        std::process::exit(1);
    }

    let year = args[1].as_str();
    let day = args[2].as_str();

    match (year, day) {
        // 2022
        ("2022", "01") => year2022::day01::run(),
        ("2022", "02") => year2022::day02::run(),
        ("2022", "03") => year2022::day03::run(),
        ("2022", "08") => year2022::day08::run(),

        // 2023
        // ("2023", "01") => year2023::day01::run(),
        _ => {
            eprintln!("Day {}/{} not implemented", year, day);
            std::process::exit(1);
        }
    }
}
