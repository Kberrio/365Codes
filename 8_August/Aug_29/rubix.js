const readline = require('readline');

class RubiksCube {
    constructor() {
        this.faces = {
            'front': Array(3).fill().map(() => Array(3).fill('R')),
            'back': Array(3).fill().map(() => Array(3).fill('O')),
            'left': Array(3).fill().map(() => Array(3).fill('G')),
            'right': Array(3).fill().map(() => Array(3).fill('B')),
            'top': Array(3).fill().map(() => Array(3).fill('W')),
            'bottom': Array(3).fill().map(() => Array(3).fill('Y'))
        };
    }

    display() {
        for (const [face, matrix] of Object.entries(this.faces)) {
            console.log(`${face.charAt(0).toUpperCase() + face.slice(1)}:`);
            matrix.forEach(row => console.log(row.join(' ')));
            console.log();
        }
    }

    rotateFace(face, direction) {
        const matrix = this.faces[face];
        if (direction === 'clockwise') {
            this.faces[face] = matrix[0].map((_, i) => matrix.map(row => row[i]).reverse());
        } else {
            this.faces[face] = matrix[0].map((_, i) => matrix.map(row => row[i])).reverse();
        }
    }

    move(face, direction = 'clockwise') {
        this.rotateFace(face, direction);
        
        if (face === 'front') {
            this._rotateAdjacent('top', 'right', 'bottom', 'left', 2, direction);
        } else if (face === 'back') {
            this._rotateAdjacent('top', 'left', 'bottom', 'right', 0, direction);
        } else if (face === 'left') {
            this._rotateAdjacent('top', 'front', 'bottom', 'back', 0, direction);
        } else if (face === 'right') {
            this._rotateAdjacent('top', 'back', 'bottom', 'front', 2, direction);
        } else if (face === 'top') {
            this._rotateAdjacent('back', 'right', 'front', 'left', 0, direction);
        } else if (face === 'bottom') {
            this._rotateAdjacent('front', 'right', 'back', 'left', 2, direction);
        }
    }

    _rotateAdjacent(f1, f2, f3, f4, idx, direction) {
        const temp = this.faces[f1].map(row => row[idx]);
        if (direction === 'clockwise') {
            for (let i = 0; i < 3; i++) {
                this.faces[f1][i][idx] = this.faces[f4][i][2-idx];
                this.faces[f4][i][2-idx] = this.faces[f3][2-i][2-idx];
                this.faces[f3][i][2-idx] = this.faces[f2][2-i][idx];
                this.faces[f2][i][idx] = temp[i];
            }
        } else {
            for (let i = 0; i < 3; i++) {
                this.faces[f1][i][idx] = this.faces[f2][i][idx];
                this.faces[f2][i][idx] = this.faces[f3][2-i][2-idx];
                this.faces[f3][i][2-idx] = this.faces[f4][2-i][2-idx];
                this.faces[f4][i][2-idx] = temp[2-i];
            }
        }
    }

    scramble(moves = 20) {
        const faces = Object.keys(this.faces);
        const directions = ['clockwise', 'counterclockwise'];
        for (let i = 0; i < moves; i++) {
            const randomFace = faces[Math.floor(Math.random() * faces.length)];
            const randomDirection = directions[Math.floor(Math.random() * directions.length)];
            this.move(randomFace, randomDirection);
        }
    }
}

function main() {
    const cube = new RubiksCube();
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    console.log("Welcome to the Rubik's Cube simulator!");
    console.log("Commands: 'move <face> [direction]', 'display', 'scramble', 'quit'");
    console.log("Faces: front, back, left, right, top, bottom");
    console.log("Directions: clockwise (default), counterclockwise");

    function promptUser() {
        rl.question("Enter command: ", (input) => {
            const command = input.toLowerCase().split(' ');

            if (command[0] === 'quit') {
                rl.close();
                return;
            } else if (command[0] === 'display') {
                cube.display();
            } else if (command[0] === 'scramble') {
                cube.scramble();
                console.log("Cube scrambled!");
            } else if (command[0] === 'move') {
                if (command.length < 2) {
                    console.log("Please specify a face to move.");
                } else {
                    const face = command[1];
                    const direction = command[2] || 'clockwise';
                    if (!Object.keys(cube.faces).includes(face)) {
                        console.log("Invalid face. Choose from: front, back, left, right, top, bottom");
                    } else if (!['clockwise', 'counterclockwise'].includes(direction)) {
                        console.log("Invalid direction. Choose either 'clockwise' or 'counterclockwise'");
                    } else {
                        cube.move(face, direction);
                        console.log(`Moved ${face} ${direction}`);
                    }
                }
            } else {
                console.log("Invalid command. Try 'move', 'display', 'scramble', or 'quit'");
            }

            promptUser();
        });
    }

    promptUser();
}

main();