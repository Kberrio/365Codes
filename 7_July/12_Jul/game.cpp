#include <SFML/Graphics.hpp>

int main()
{
    // Create the window
    sf::RenderWindow window(sf::VideoMode(800, 600), "Simple Sprite Game");

    // Load the sprite texture
    sf::Texture texture;
    if (!texture.loadFromFile("character.png"))
        return -1;

    // Create the sprite
    sf::Sprite sprite(texture);
    sprite.setPosition(400, 300);

    // Game loop
    while (window.isOpen())
    {
        sf::Event event;
        while (window.pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
                window.close();
        }

        // Move the sprite
        if (sf::Keyboard::isKeyPressed(sf::Keyboard::Left))
            sprite.move(-5, 0);
        if (sf::Keyboard::isKeyPressed(sf::Keyboard::Right))
            sprite.move(5, 0);
        if (sf::Keyboard::isKeyPressed(sf::Keyboard::Up))
            sprite.move(0, -5);
        if (sf::Keyboard::isKeyPressed(sf::Keyboard::Down))
            sprite.move(0, 5);

        // Clear the window
        window.clear(sf::Color::White);

        // Draw the sprite
        window.draw(sprite);

        // Display the window contents
        window.display();
    }

    return 0;
}