// Color Theory Program in Node.js

// RGB to Hex conversion function
function rgbToHex(r, g, b) {
    const toHex = (c) => {
        const hex = c.toString(16);
        return hex.length === 1 ? '0' + hex : hex;
    };

    return '#' + toHex(r) + toHex(g) + toHex(b);
}

// Complementary color function
function complementaryColor(hex) {
    // Remove '#' if present
    hex = hex.replace('#', '');

    // Convert hex to RGB
    const r = parseInt(hex.substring(0, 2), 16);
    const g = parseInt(hex.substring(2, 4), 16);
    const b = parseInt(hex.substring(4, 6), 16);

    // Calculate complementary color
    const compR = 255 - r;
    const compG = 255 - g;
    const compB = 255 - b;

    return rgbToHex(compR, compG, compB);
}

// Example usage
const inputColor = '#FF0000'; // Red color
const complementary = complementaryColor(inputColor);

console.log(`Input color: ${inputColor}`);
console.log(`Complementary color: ${complementary}`);
