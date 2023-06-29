// 1.test
const assert = require('assert');
const calculateNumber = require('./1-calcul.js');

describe('calculateNumber', function () {
    describe('SUM operation', function () {
        it('should return the sum of rounded numbers', function () {
            const result1 = calculateNumber('SUM', 3.7, 2.1);
            assert.strictEqual(result1, 6);

            const result2 = calculateNumber('SUM', 1.4, 7.9);
            assert.strictEqual(result2, 9);
        });
    });

    describe('SUBTRACT operation', function () {
        it('should return the difference of rounded numbers', function () {
            const result1 = calculateNumber('SUBTRACT', 5.6, 0);
            assert.strictEqual(result1, 6);

            const result2 = calculateNumber('SUBTRACT', 4.8, -2.3);
            assert.strictEqual(result2, 7);
        });
    });

    describe('DIVIDE operation', function () {
        it('should return the division result of rounded numbers', function () {
            const result1 = calculateNumber('DIVIDE', 10, 4);
            assert.strictEqual(result1, 2.5);

            const result2 = calculateNumber('DIVIDE', 8, 0);
            assert.strictEqual(result2, 'Error');
        });
    });
});
