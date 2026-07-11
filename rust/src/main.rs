mod input;
mod year2022;
mod year2023;

fn main() {
    let args: Vec<String> = std::env::args().collect();

    if args.len() != 3 {
        eprintln!("Usage: cargo run <year> <day>");
        eprintln!("Example: cargo run 2022 01");
        std::process::exit(1);
    }

    let year = args[1].as_str();
    let day = args[2].as_str();

    match year {
        "2022" => year2022::run(day),
        "2023" => year2023::run(day),
        _ => {
            eprintln!("Year {year} not implemented");
            std::process::exit(1);
        }
    }
}
