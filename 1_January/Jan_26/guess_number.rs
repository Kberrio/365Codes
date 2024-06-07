use std::io;
use rand::Rng;
use std::cmp::Ordering;

fn main() {
    println!("Welcome to the Guess the Number game!");
    
    let secret_number = rand::thread_rng().gen_range(1..101);

    loop {
        println!("Please guess a number between 1 and 100: ");

        let mut guess = String::new();

        io::stdin()
            .read_line(&mut guess)
            .expect("Failed to read line");

        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => {
                println!("Invalid input. Please enter a valid number.");
                continue;
            }
        };

        println!("You guessed: {}", guess);

        match guess.cmp(&secret_number) {
            Ordering::Less => println!("Too small! Try again."),
            Ordering::Greater => println!("Too big! Try again."),
            Ordering::Equal => {
                println!("Congratulations! You guessed the number correctly: {}", secret_number);
                break;
            }
        }
    }
}
