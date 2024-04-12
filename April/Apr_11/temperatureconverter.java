import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class TemperatureConverter extends JFrame {
    private JTextField celsiusField;
    private JTextField fahrenheitField;
    private JButton convertToCButton;
    private JButton convertToFButton;

    public TemperatureConverter() {
        createUI();
        setTitle("Temperature Converter");
        setSize(300, 150);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLocationRelativeTo(null); // Center the window
    }

    private void createUI() {
        // Create components
        celsiusField = new JTextField(10);
        fahrenheitField = new JTextField(10);
        convertToCButton = new JButton("To Celsius");
        convertToFButton = new JButton("To Fahrenheit");

        // Layout
        setLayout(new FlowLayout());
        add(new JLabel("Celsius:"));
        add(celsiusField);
        add(convertToCButton);
        add(new JLabel("Fahrenheit:"));
        add(fahrenheitField);
        add(convertToFButton);

        // Add action listeners
        convertToCButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                convertToFahrenheit();
            }
        });

        convertToFButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                convertToCelsius();
            }
        });
    }

    private void convertToCelsius() {
        try {
            double fahrenheit = Double.parseDouble(fahrenheitField.getText());
            double celsius = (fahrenheit - 32) * 5 / 9;
            celsiusField.setText(String.format("%.2f", celsius));
        } catch (NumberFormatException ex) {
            JOptionPane.showMessageDialog(this, "Invalid input", "Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    private void convertToFahrenheit() {
        try {
            double celsius = Double.parseDouble(celsiusField.getText());
            double fahrenheit = celsius * 9 / 5 + 32;
            fahrenheitField.setText(String.format("%.2f", fahrenheit));
        } catch (NumberFormatException ex) {
            JOptionPane.showMessageDialog(this, "Invalid input", "Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                new TemperatureConverter().setVisible(true);
            }
        });
    }
}
