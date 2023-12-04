function part_1(input) {
    let totalSum = 0;
    input = input.replaceAll(/ +/g, ' ');
    for (let [_, allowed, results] of input.matchAll(/Card +\d+: ([\d ]+) \| ([\d ]+)/g)) {
        allowed = allowed.split(' ').map(Number);
        results = results.split(' ').map(Number);
        let winning = results.filter((num) => allowed.includes(num));
        if (winning.length) totalSum = totalSum + (2 ** (winning.length - 1));

    };
    return totalSum;
};

function processInput(input) {
    let ret = [];
    for (let [_, card, allowed, results] of input.matchAll(/Card +(\d+): ([\d ]+) \| ([\d ]+)/g)) {
        allowed = allowed.split(' ').map(Number);
        results = results.split(' ').map(Number);
        ret[Number(card) - 1] = results.filter((num) => allowed.includes(num)).length;
    };
    return ret;
};

function part_2(input) {
    let preprocessed = processInput(input.replaceAll(/ +/g, ' '));
    let cache = Object.fromEntries(preprocessed.map((val, idx) => [idx, 1]));
    for (let key in preprocessed) {
        for (let i = Number(key); i < Number(key) + preprocessed[key]; i++) {
            cache[i + 1] = cache[i + 1] + cache[key];
        };
    };
    return Object.values(cache).reduce((a, b) => a + b);
};

const input = require('./aoc')(4);

console.log(part_1(input));
console.log(part_2(input));