// 2.test
const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai');

describe('calculateNumber', function () {
    describe('SUM operation', function () {
        it('should return the sum of rounded numbers', function () {
            const result1 = calculateNumber('SUM', 3.7, 2.1);
            expect(result1).to.equal(6);

            const result2 = calculateNumber('SUM', 1.4, 7.9);
            expect(result2).to.equal(9);
        });
    });

    describe('SUBTRACT operation', function () {
        it('should return the difference of rounded numbers', function () {
            const result1 = calculateNumber('SUBTRACT', 5.6, 0);
            expect(result1).to.equal(6);

            const result2 = calculateNumber('SUBTRACT', 4.8, -2.3);
            expect(result2).to.equal(7);
        });
    });

    describe('DIVIDE operation', function () {
        it('should return the division result of rounded numbers', function () {
            const result1 = calculateNumber('DIVIDE', 10, 4);
            expect(result1).to.equal(2.5);

            const result2 = calculateNumber('DIVIDE', 8, 0);
            expect(result2).to.equal('Error');
        });
    });
});
