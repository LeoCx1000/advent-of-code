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


/**
 * The `part_2` function takes an input string and performs a series of range mappings and reductions
 * to determine the minimum value in a set of mapped ranges.
 * @param ranges - The `ranges` parameter is an array of arrays, where each inner array represents a
 * range. Each inner array contains two elements: the start and end values of the range.
 * @returns The function `part_2` returns the minimum value from the mapped seeds.
 */
function reduceRanges(ranges) {
    console.log('reducing', ranges.length, 'ranges');
    // Sort ranges by start
    ranges.sort((a, b) => a[0] - b[0]);

    let reducedRanges = [ranges[0]];

    for (let i = 1; i < ranges.length; i++) {
        let lastRange = reducedRanges[reducedRanges.length - 1];
        let currentRange = ranges[i];

        // If the current range overlaps or is adjacent with the last range, merge them
        if (currentRange[0] <= lastRange[1] + 1) {
            lastRange[1] = Math.max(lastRange[1], currentRange[1]);
        } else {
            // If not, add the current range to reducedRanges
            reducedRanges.push(currentRange);
        }
    }

    return reducedRanges;
}

function createRangeRelationFunc(funcDef) {
    let lines = funcDef.split('\n');
    let [sourceName, destName] = lines.shift().replace(/ map: ?/, '').split('-to-');
    let mapRanges = lines.map((line) => line.split(' ').map(Number));

    function mapTo(rangeList) {
        console.log(rangeList);
        let processedRanges = [];

        while (rangeList.length) {
            let [start, end] = rangeList.shift();
            // todo: the math is wrong somehow. I need to think...

            // for each range, loop the mapper, slice it and sum.
            for (let i = 0; i < mapRanges.length; i++) {
                let [destStart, srcStart, range] = mapRanges[i];

                let sourceStartInRange = (srcStart >= start) && (srcStart < end);
                let sourceEndInRange = ((srcStart + range) >= start) && ((srcStart + range) < end);
                let startInSource = (start >= srcStart) && (start < (srcStart + range));
                let endInSource = ((end) >= srcStart) && (end < (srcStart + range));

                if (sourceStartInRange && sourceEndInRange) {
                    // source is subset of the range
                    // 1. Take the first part (not in the source range) and put it at the end of the stack.
                    // 2. map start and end, using the range that is mappable
                    // 3. Take the second part (not in the source range) and put it at the end of the stack.
                    processedRanges.push([destStart + (srcStart - start), destStart + (srcStart - start) + range]);
                    if (start !== srcStart)
                        rangeList.push([start, srcStart]);
                    if (end !== srcStart + range)
                        rangeList.push([srcStart + range, end]);
                    break;
                }
                else if (startInSource && endInSource) {
                    // range is subset of the source range
                    processedRanges.push([destStart + (start - srcStart), destStart + (end - srcStart)]);
                    break;
                }
                // Else split the range, put the non-mapped portion at the end of the queue.
                else if (sourceStartInRange) {
                    // The start of the range is in the source range, but not the end, so
                    // the second half will go unmapped.
                    rangeList.push([srcStart + range, end]);
                    processedRanges.push([destStart + (srcStart - start), destStart + range]);
                    break;
                } else if (sourceEndInRange) {
                    // The end of the range is in the source range, but not the start, so
                    // the first half will go unmapped.
                    rangeList.push([start, srcStart]);
                    processedRanges.push([destStart, destStart + (srcStart - start + range)]);
                    break;
                }
                // If the range did not map to any source and it is the last map, add it to processedRanges as it is.
                if (i === mapRanges.length - 1) {
                    processedRanges.push([start, end]);
                    break;
                }
            }
        }

        return [processedRanges, destName];
    }

    return [sourceName, mapTo];
};

function part_2(input) {
    let [allSeedList, ...FunctionDefs] = input.trim().split('\n\n');
    allSeedList = allSeedList.replace('seeds: ', '').split(' ').map(Number);
    let functions = Object.fromEntries(FunctionDefs.map(createRangeRelationFunc));

    function mapRanges(ranges, from = 'seed') {
        console.log('processing from', from, 'with', ranges.length, 'ranges');
        if (!(from in functions))
            return ranges;
        return mapRanges(...functions[from](ranges));
    };

    let seedRanges = [];

    for (let i = 0; i < allSeedList.length; i += 2) {
        if (i % 2 === 0)
            seedRanges.push([allSeedList[i], allSeedList[i] + allSeedList[i + 1]]);
    }
    let mappedSeeds = mapRanges(seedRanges);

    console.log(reduceRanges(mappedSeeds));

    return Math.min(...mappedSeeds.map((range) => range[0]));
};

function createRelationFuncBF(funcDef) {
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

function part_2BruteForce(input) {
    let fxBlocks = input.split('\n\n');
    let seeds = fxBlocks.shift().replace('seeds: ', '').split(' ').map(Number);
    let mappers = Object.fromEntries(fxBlocks.map(createRelationFuncBF));
    function mapSeed(number, from = 'seed') {
        if (!(from in mappers)) {
            return number;
        }
        return mapSeed(...mappers[from](number));
    };

    let mappedSeeds = seeds.map((seed) => mapSeed(seed));
    return Math.min(...mappedSeeds);
};
const input = require('./aoc.js')(5);
console.log(part_1(input));
console.log(part_2(input));

// expected output: 37384986