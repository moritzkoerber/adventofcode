pub fn run() {
    // Part 1
    let p_input = crate::input::read(2022, 4);
    let assignments = p_input.lines().map(|line| {
        line.split(&['-', ','])
            .map(|value| value.parse::<u8>().unwrap())
            .collect::<Vec<_>>()
    });

    let part1 = assignments
        .clone()
        .filter(|x| {
            (x[0] <= x[2]) && (x[1] >= x[3]) || (x[2] <= x[0]) && (x[3] >= x[1])
        })
        .count();
    println!("{part1}");

    // Part 2
    let part2 = assignments
        .clone()
        .filter(|x| (x[0] >= x[2] || x[1] >= x[2]) && (x[0] <= x[3] || x[1] <= x[3]))
        .count();

    println!("{part2}")
}
