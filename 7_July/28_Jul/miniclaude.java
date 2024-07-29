import java.util.Scanner;

public class MiniClaude {
    public static String respond(String input) {
        String lowercaseInput = input.toLowerCase();
        
        if (lowercaseInput.contains("hello") || lowercaseInput.contains("hi")) {
            return "Hello! How can I assist you today?";
        } else if (lowercaseInput.contains("how are you")) {
            return "I'm functioning well, thank you. How may I help you?";
        } else if (lowercaseInput.contains("bye") || lowercaseInput.contains("goodbye")) {
            return "Goodbye! Have a great day!";
        } else if (lowercaseInput.contains("name")) {
            return "I'm Mini Claude, a simple chatbot.";
        } else if (lowercaseInput.contains("weather")) {
            return "I'm sorry, I don't have access to real-time weather information.";
        } else {
            return "I'm not sure how to respond to that. Can you please rephrase or ask something else?";
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Mini Claude: Hello! I'm Mini Claude. How can I help you?");
        
        while (true) {
            System.out.print("You: ");
            String input = scanner.nextLine();
            
            if (input.equalsIgnoreCase("exit")) {
                System.out.println("Mini Claude: Goodbye!");
                break;
            }
            
            String response = respond(input);
            System.out.println("Mini Claude: " + response);
        }
        
        scanner.close();
    }
}