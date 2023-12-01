function getFirstNumber(line) {
    for (let i = 0; i < line.length; i++) {
        if (!line[i].match(/\d/)) continue
        return line[i]
    }
}

function reverse(line) {
    return line.split('').reverse().join('')
}

function part_1(input) {
    let numbers = [];
    for (line of input.split('\n')) {
        let first = getFirstNumber(line)
        let last = getFirstNumber(reverse(line))
        numbers.push(Number(`${first}${last}`))
    }
    return numbers.reduce((p, c) => p + c)
}

const lookup = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'];
let regExpString = lookup.join('|')

const normalFinder = RegExp(`(${regExpString})`)
const reversedFinder = RegExp(`(${reverse(regExpString)})`)


function part_2(input) {
    let numbers = [];
    for (line of input.split('\n')) {
        let first = getFirstNumber(line.replace(normalFinder, (m, lit) => lookup.indexOf(lit)))
        let last = getFirstNumber(reverse(line).replace(reversedFinder, (_, lit) => lookup.indexOf(reverse(lit))))
        numbers.push(Number(`${first}${last}`))
    }
    return numbers.reduce((p, c) => p + c)
}

const input_for = require('./aoc.js')
const input = input_for(1)

console.log(part_1(input))
console.log(part_2(input))