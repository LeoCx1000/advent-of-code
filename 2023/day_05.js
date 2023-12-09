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

//     \\\   //Ʌ\\   ///  //Ʌ\\    |||\\\  ||\\\  |||  |||  ||\\\  |||   //I\\
//      \\\ /// \\\ ///  ///_\\\   || ///  |||\\\ |||  |||  |||\\\ |||  ||| =w
//       \\V//   \\V//  ///---\\\ ||| \\\  ||| \\\|||  |||  ||| \\\|||  \\XX//
//       This code does not work, and does not resolve part two. I gave up on
//            that, and worked on this ascii art instead! woo hoo ADHD.

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
                    console.log(`Source range ${srcStart}-${srcStart + range} is in range ${start}-${end}`);
                    // source is subset of the range
                    // 1. Take the first part (not in the source range) and put it at the end of the stack.
                    // 2. map start and end, using the range that is mappable
                    // 3. Take the second part (not in the source range) and put it at the end of the stack.
                    processedRanges.push([destStart + (srcStart - start), destStart + (srcStart - start) + range]);
                    if (start !== srcStart) {
                        console.log('start pushing', [start, srcStart]);
                        rangeList.push([start, srcStart]);
                    }
                    if (end !== srcStart + range - 1) {
                        console.log('end pushing', [srcStart + range, end]);
                        rangeList.push([srcStart + range, end]);
                    }
                    break;
                }
                else if (startInSource && endInSource) {
                    console.log(`range ${start}-${end} is in source range ${srcStart}-${srcStart + range}. Converting into ${destStart}-${destStart + range}`);
                    // range is subset of the source range
                    console.log('processed range', [destStart + (start - srcStart), destStart + (end - srcStart)]);
                    processedRanges.push([destStart + (start - srcStart), destStart + (end - srcStart)]);
                    break;
                }
                // Else split the range, put the non-mapped portion at the end of the queue.
                else if (sourceStartInRange) {
                    console.log(`source range ${srcStart}-${srcStart + range} starts within range ${start}-${end}. Converting into ${destStart}-${destStart + range}`);
                    console.log('processed range', [destStart + (srcStart - start), destStart + range]);

                    // The start of the range is in the source range, but not the end, so
                    // the second half will go unmapped.
                    console.log('half pushing st', [srcStart + range, end]);
                    rangeList.push([start, srcStart - 1]);
                    processedRanges.push([destStart, destStart + (srcStart - start + range)]);

                    break;
                } else if (sourceEndInRange) {
                    console.log(`source range ${srcStart}-${srcStart + range} ends within range ${start}-${end}. Converting into ${destStart}-${destStart + range}`);
                    // The end of the source range is in the range, but not the start, so
                    // the second half will go unmapped.
                    rangeList.push([srcStart + range + 1, end]);
                    console.log('half pushed', [srcStart + range + 1, end]);

                    processedRanges.push([destStart + (start - srcStart), destStart + range]);
                    console.log('processed', [destStart + (start - srcStart), destStart + range]);
                    break;
                }
                // If the range did not map to any source and it is the last map, add it to processedRanges as it is.
                if (i === mapRanges.length - 1) {
                    console.log(`skipping range ${start}-${end}, could not fit within`, mapRanges);
                    console.log('processed range', [start, end]);
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
        console.log('\n\nprocessing from', from, 'with', ranges.length, 'ranges\n\n');
        if (!(from in functions))
            return ranges;
        return mapRanges(...functions[from](ranges));
    };

    let seedRanges = [];

    for (let i = 0; i < allSeedList.length; i += 2) {
        if (i % 2 === 0)
            seedRanges.push([allSeedList[i], allSeedList[i] + allSeedList[i + 1] - 1]);
    }
    let mappedSeeds = mapRanges(seedRanges);

    console.log(reduceRanges(mappedSeeds));

    return Math.min(...mappedSeeds.map((range) => range[0]));
};


const input = `seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4`;
console.log(part_1(input));
console.log(part_2(input));

// expected output: 37384986