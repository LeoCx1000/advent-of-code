function parseInput(input) {
    let toNumbers = (line) => line.split(': ')[1].split(' ').map(Number);
    let [times, distances] = input.replaceAll(/ +/g, ' ').split('\n').map(toNumbers);
    return times.map((elem, idx) => [elem, distances[idx]]);
}

function part_1(input) {
    let raceDiffs = [];
    for (let [index, [time, distance]] of parseInput(input).entries()) {
        raceDiffs[index] = 0;
        for (let i = 0; i <= time; i++) {
            let travel = (time - i) * i;
            if (travel > distance) {
                raceDiffs[index]++;
            }
        };
    };
    return raceDiffs.reduce((x, y) => (x * y));
};

const input = require('./aoc.js')(6);
console.log(part_1(input));

// lol
console.log(part_1(input.replaceAll(/ +/g, '').replaceAll(':', ': ')));