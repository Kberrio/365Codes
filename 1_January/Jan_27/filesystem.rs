use std::collections::HashMap;
use std::io;
use std::io::Write;

#[derive(Debug)]
enum FileSystemEntity {
    File(String),
    Directory(HashMap<String, FileSystemEntity>),
}

fn main() {
    let mut root_directory: HashMap<String, FileSystemEntity> = HashMap::new();
    let mut current_directory: &mut HashMap<String, FileSystemEntity> = &mut root_directory;

    loop {
        print!("> ");
        io::stdout().flush().expect("Failed to flush stdout");

        let mut input = String::new();
        io::stdin()
            .read_line(&mut input)
            .expect("Failed to read input");

        let command = input.trim().to_lowercase();
        let parts: Vec<&str> = command.split(' ').collect();

        match parts[0] {
            "exit" => {
                println!("Exiting the file system simulation.");
                break;
            }
            "ls" => list_files_and_directories(&current_directory),
            "mkdir" => {
                if parts.len() < 2 {
                    println!("Usage: mkdir <directory_name>");
                } else {
                    create_directory(&mut current_directory, parts[1]);
                }
            }
            "touch" => {
                if parts.len() < 2 {
                    println!("Usage: touch <file_name>");
                } else {
                    create_file(&mut current_directory, parts[1]);
                }
            }
            "cd" => {
                if parts.len() < 2 {
                    println!("Usage: cd <directory_name>");
                } else {
                    match change_directory(&mut current_directory, parts[1]) {
                        Some(new_directory) => current_directory = new_directory,
                        None => println!("Directory not found."),
                    }
                }
            }
            _ => println!("Unknown command: {}", parts[0]),
        }
    }
}

fn list_files_and_directories(directory: &HashMap<String, FileSystemEntity>) {
    for (name, entity) in directory {
        match entity {
            FileSystemEntity::File(_) => println!("File: {}", name),
            FileSystemEntity::Directory(_) => println!("Directory: {}", name),
        }
    }
}

fn create_directory(
    directory: &mut HashMap<String, FileSystemEntity>,
    directory_name: &str,
) {
    directory.insert(
        directory_name.to_string(),
        FileSystemEntity::Directory(HashMap::new()),
    );
    println!("Directory '{}' created.", directory_name);
}

fn create_file(directory: &mut HashMap<String, FileSystemEntity>, file_name: &str) {
    directory.insert(
        file_name.to_string(),
        FileSystemEntity::File("".to_string()),
    );
    println!("File '{}' created.", file_name);
}

fn change_directory(
    directory: &mut HashMap<String, FileSystemEntity>,
    directory_name: &str,
) -> Option<&mut HashMap<String, FileSystemEntity>> {
    match directory.get_mut(directory_name) {
        Some(FileSystemEntity::Directory(new_directory)) => Some(new_directory),
        _ => None,
    }
}
