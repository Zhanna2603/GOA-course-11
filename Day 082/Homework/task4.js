// შექმენით form სადაც გექნებათ 3 შესატანი ველი, სახელი, ემაილი და პაროლი, თქვენი დავალეება როდესაც ფორმა დადასტურდება წამოიღთ ჯავასკრიპტში დადასტურებული მნიშნელობები ინპუთებიდან, შექმენით მასივი სახელად dataBase  ხოლო ყოველი დადასტურებული ინფორმაცია შეინახეთ ამ მასივში ობიექტის სახით, დააუმატეთ უსაფრთხოების ფუნქციონალი სადაც გამოიყენებთ for ციკლს, სანამ დაემატება მასივში ობიექტი იქამდე შეამოწმეთ არსებობს თუ არა ისეთი ობიექტი მასივში რომელიც ტოლია ახლად დადასტურებული ფორმის ემაილის, თუ ტოლია ალერტით გამოუტანეთ რომ ექაუნთი არსებობს, თუ არაა ტოლი მაშინ ალერტით გამოუტანეთ რომ ექაუნთი წარმატებით შექიმნა

let dataBase = [];

// Function to validate the form and add data to the database
function validateForm(event) {
    event.preventDefault(); // Prevent form submission

    // Get values from the form inputs
    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const password = document.getElementById('password').value.trim();

    // Validate inputs (basic validation)
    if (!name || !email || !password) {
        alert('Please fill out all fields.');
        return;
    }

    // Check if the email already exists in the database
    let emailExists = false;
    for (let i = 0; i < dataBase.length; i++) {
        if (dataBase[i].email === email) {
            emailExists = true;
            break;
        }
    }

    if (emailExists) {
        alert('An account with this email already exists.');
    } else {
        // Create a new user object
        const newUser = { name, email, password };
        
        // Add the new user to the database
        dataBase.push(newUser);

        // Display success message
        alert('Account created successfully!');

        // Log the database to the console for verification
        console.log('Updated Database:', dataBase);
    }
}

// Attach the form submission
document.getElementById('registrationForm').addEventL