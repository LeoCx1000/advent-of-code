function getMatrix(input) {
    let matrix = []
    for (let line of input.split('\n'))
        matrix.push(line.split(''))
    return matrix;
};

function charAt(arr, y, x) {
    try {
        return arr[y][x];
    } catch (error) {
        return undefined;
    };
};

function hasAdjacentSpecialChar(matrix, yIdx, start, end) {
    let num = matrix[yIdx].slice(start, end).join('');
    for (let i = start - 1; i < end + 1; i++) {
        let chars = [
            charAt(matrix, yIdx - 1, i),
            charAt(matrix, yIdx, i),
            charAt(matrix, yIdx + 1, i)
        ];
        if (chars.some(char => char && !char.match(/\d|\./))) {
            return Number(num);
        };
    };
};

function part_1(input) {
    let matrix = [];
    let found = [];

    for (let line of input.split('\n'))
        matrix.push(line.split(''))

    for (let yIdx in matrix) {
        yIdx = Number(yIdx);
        let start = NaN;

        for (let xIdx in matrix[yIdx]) {
            xIdx = Number(xIdx);

            if (matrix[yIdx][xIdx].match(/\d/)) {
                if (isNaN(start)) { start = xIdx }
            } else if (!isNaN(start)) {
                let num = hasAdjacentSpecialChar(matrix, yIdx, start, xIdx);
                if (num) found.push(num);
                start = NaN;
            };
        };

        if (!isNaN(start)) {
            // End of string
            let num = hasAdjacentSpecialChar(matrix, yIdx, start, matrix[yIdx].length);
            if (num) found.push(num)
        };
    };

    return found.reduce((a, b) => a + b);
};

function singleLineNumbers(matrix, yIdx, xIdx) {
    let line = matrix[yIdx].slice(xIdx - 3, xIdx + 4).join('');
    let ret = [];
    for (let match of line.matchAll(/\d+/g)) {
        ret.push([
            Number(match[0]),
            Number(match.index) + xIdx - 3,
            Number(match.index + match[0].length - 1) + xIdx - 3,
        ]);
    };
    return ret;
};

function getAdjacentNumbers(matrix, y, x) {
    let numbers = [];
    let points = [x - 1, x, x + 1];
    for (let idx of [y - 1, y, y + 1]) {
        for (let [num, start, end] of singleLineNumbers(matrix, idx, x)) {
            if (points.includes(end) || points.includes(start))
                numbers.push(num);
        };
    };
    return numbers;
}

function part_2(input) {
    let matrix = getMatrix(input);
    let found = [];

    for (let yIdx = 0; yIdx < matrix.length; yIdx++) {
        for (let xIdx = 0; xIdx < matrix[yIdx].length; xIdx++) {

            if (matrix[yIdx][xIdx] !== '*')
                continue;

            numbers = getAdjacentNumbers(matrix, yIdx, xIdx);
            if (numbers.length == 2) {
                found.push(numbers[0] * numbers[1]);
            };

        };
    };

    return found.reduce((a, b) => a + b, 0);
};

const input = require('./aoc.js')(3);
console.log(part_1(input));
console.log(part_2(input));

// It's 1 AM and this shit's got something wrong... Time to sleep, kill me.

// 11am: Oh my god, I just woke up and noticed the stupid mistake I had made...
// I should not program while I am exhausted just "for the challenge". Fuck me dude.