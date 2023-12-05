function createRelationFunc(funcDef) {
    let lines = funcDef.split('\n');
    let [sourceName, destName] = lines.shift().replace(/ map: ?/, '').split('-to-');
    let numbers = lines.map((line) => line.split(' ').map(Number));
    function mapTo(number) {
        for (let [dest, src, range] of numbers) {
            if (number >= src && src + range > number) {
                let offset = number - src;
                return [dest + offset, destName];
            };
        };
        return [number, destName];
    };

    return [sourceName, mapTo];
};

function part_1(input) {
    let fxBlocks = input.split('\n\n');
    let seeds = fxBlocks.shift().replace('seeds: ', '').split(' ').map(Number);
    let mappers = Object.fromEntries(fxBlocks.map(createRelationFunc));
    function mapSeed(number, from = 'seed') {
        if (!(from in mappers)) {
            return number;
        }
        return mapSeed(...mappers[from](number));
    };

    let mappedSeeds = seeds.map((seed) => mapSeed(seed));
    return Math.min(...mappedSeeds);
};

function createRangeRelationFunc(funcDef) {
    let lines = funcDef.split('\n');
    let [sourceName, destName] = lines.shift().replace(/ map: ?/, '').split('-to-');
    let numbers = lines.map((line) => line.split(' ').map(Number));

    function mapTo(elem) {
        let start, stop = elem;

        for (let [dest, src, range] of numbers) {
            if (number >= src && src + range > number) {
                let offset = number - src;
                return [dest + offset, destName];
            };
        };
        return [[start, stop], destName];
    };

    return [sourceName, mapTo];
};

function part_2(input) {

}

const input = require('./aoc.js')(5);
console.log(part_1(input));