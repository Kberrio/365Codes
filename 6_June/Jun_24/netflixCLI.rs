use std::io::{self, Write};

#[derive(Debug)]
struct Show {
    title: String,
    genre: String,
    rating: f32,
}

fn main() {
    let shows = vec![
        Show {
            title: "Stranger Things".to_string(),
            genre: "Science Fiction".to_string(),
            rating: 8.7,
        },
        Show {
            title: "The Witcher".to_string(),
            genre: "Fantasy".to_string(),
            rating: 8.2,
        },
        Show {
            title: "Breaking Bad".to_string(),
            genre: "Crime Drama".to_string(),
            rating: 9.5,
        },
        Show {
            title: "Money Heist".to_string(),
            genre: "Action".to_string(),
            rating: 8.3,
        },
        Show {
            title: "The Crown".to_string(),
            genre: "Historical Drama".to_string(),
            rating: 8.6,
        },
    ];

    println!("Welcome to the Netflix CLI!");
    loop {
        println!("\n1. Search by title");
        println!("2. List all shows");
        println!("3. Exit");
        print!("Please choose an option: ");
        io::stdout().flush().unwrap();

        let mut choice = String::new();
        io::stdin().read_line(&mut choice).unwrap();
        let choice = choice.trim();

        match choice {
            "1" => search_by_title(&shows),
            "2" => list_all_shows(&shows),
            "3" => {
                println!("Goodbye!");
                break;
            },
            _ => println!("Invalid choice, please try again."),
        }
    }
}

fn search_by_title(shows: &[Show]) {
    print!("Enter the title to search for: ");
    io::stdout().flush().unwrap();

    let mut title = String::new();
    io::stdin().read_line(&mut title).unwrap();
    let title = title.trim().to_lowercase();

    let mut found = false;
    for show in shows {
        if show.title.to_lowercase().contains(&title) {
            println!("{:?}", show);
            found = true;
        }
    }

    if !found {
        println!("No show found with the title: {}", title);
    }
}

fn list_all_shows(shows: &[Show]) {
    for show in shows {
        println!("{:?}", show);
    }
}
