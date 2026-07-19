pub mod day01;
pub mod day02;

pub fn run(day: &str) {
    match day {
        "01" => day01::run(),
        "02" => day02::run(),
        _ => {
            eprintln!("Day 2022/{day} not implemented");
            std::process::exit(1);
        }
    }
}
