// შექმენით ფუნქცია რომელსაც გადაეცემა 2 რიცხვი, start - end, თქვენი მოვალეობაა ამ რიცხვებს შორის ყველა რიცხვის გაგება და მასივში შეტანა, საბოლოოდ დააბრუნეთ მასივი

function generateNumbersArray(start, end) {
    let numbersArray = [];
    for (let i = start; i <= end; i++) {
        numbersArray.push(i);
    }
    return numbersArray;
}