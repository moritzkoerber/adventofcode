use std::env;

#[path = "2022/mod.rs"]
mod year2022;

// #[path = "2023/mod.rs"]
// mod year2023;

fn main() {
    let args: Vec<String> = env::args().collect();

    if args.len() < 2 {
        eprintln!("Usage: cargo run <year>/<day> or cargo run <year> <day>");
        eprintln!("Example: cargo run 2022/01");
        std::process::exit(1);
    }

    let (year, day) = if args[1].contains('/') {
        let parts: Vec<&str> = args[1].split('/').collect();
        if parts.len() != 2 {
            eprintln!("Invalid format. Use: cargo run <year>/<day>");
            std::process::exit(1);
        }
        (parts[0], parts[1])
    } else if args.len() >= 3 {
        (args[1].as_str(), args[2].as_str())
    } else {
        eprintln!("Usage: cargo run <year>/<day> or cargo run <year> <day>");
        std::process::exit(1);
    };

    match (year, day) {
        // 2022
        ("2022", "01") => year2022::day01::run(),
        ("2022", "02") => year2022::day02::run(),

        // 2023
        // ("2023", "01") => year2023::day01::run(),
        _ => {
            eprintln!("Day {}/{} not implemented", year, day);
            std::process::exit(1);
        }
    }
}
