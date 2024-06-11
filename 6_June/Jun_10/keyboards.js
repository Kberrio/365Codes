document.addEventListener('DOMContentLoaded', () => {
    const outputDiv = document.getElementById('output');

    // Listen for keydown events
    document.addEventListener('keydown', (event) => {
        const keyName = event.key;
        outputDiv.textContent = `You pressed: ${keyName}`;
    });
});
