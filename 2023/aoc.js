const fs = require('fs');
const request = require('sync-request');

function session() {
    return fs.readFileSync('.session', { encoding: 'utf8', flag: 'r' })
}

function input_for(day = undefined) {
    if (!day) {
        const now = new Date();
        day = now.getDate();
    }
    let req = request(
        'GET',
        `https://adventofcode.com/2023/day/${day}/input`,
        { headers: { cookie: `session=${session()}` } }
    )
    return req.body.toString().trim()
}

module.exports = input_for