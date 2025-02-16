// დაბრუნებული მასივი გადაეცით ფუნქციას რომელსაც დაარქმევთ calculateAverage ამ ფუნქციაში გამოითვლით იმ რიცხვების საშუალოს რომელიც მოთავსებულია სიაში, მიღებული საშულა დააბრუნეთ ფუნქციიდან

function calculateAverage(numbersArray) {
    if (numbersArray.length === 0) return 0; // Avoid division by zero
    const sum = numbersArray.reduce((acc, num) => acc + num, 0);
    return sum / numbersArray.length;
}