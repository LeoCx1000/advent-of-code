function part_1(input) {
    let lookup = { red: 12, green: 13, blue: 14 };
    var possible = 0;
    for (line of input.split(/\r|\n/)) {
        let invalid = false;
        for (thing of line.matchAll(/(\d+) (\w+)/gm)) {
            [_, number, colour, ..._] = thing;
            if (number > lookup[colour])
                invalid = true;
        };
        if (!invalid) {
            [_, id, ..._] = line.match(/Game (\d+):/)
            possible = possible + Number(id);
        };
    };
    return possible;
};

function part_2(input) {
    var ret = 0;
    for (line of input.split(/\r|\n/)) {
        let cubes = { red: [], green: [], blue: [] };
        for (thing of line.matchAll(/(\d+) (\w+)/gm)) {
            [_, number, colour, ..._] = thing;
            cubes[colour].push(Number(number))
        };

        ret = ret + (Math.max(...cubes.red) * Math.max(...cubes.green) * Math.max(...cubes.blue))

    };
    return ret;
};
const input_for = require('./aoc.js')
const input = input_for(2)

console.log(part_1(input))
console.log(part_2(input))