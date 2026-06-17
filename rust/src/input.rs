use std::fs;

pub fn read(year: u16, day: u8) -> String {
    fs::read_to_string(format!("data/{year}/day{day:02}.txt")).unwrap_or_else(|err| {
        panic!("failed to read input for {year}/day{day:02}: {err}")
    })
}
