import random

class RubiksCube:
    def __init__(self):
        self.faces = {
            'front': [['R' for _ in range(3)] for _ in range(3)],
            'back': [['O' for _ in range(3)] for _ in range(3)],
            'left': [['G' for _ in range(3)] for _ in range(3)],
            'right': [['B' for _ in range(3)] for _ in range(3)],
            'top': [['W' for _ in range(3)] for _ in range(3)],
            'bottom': [['Y' for _ in range(3)] for _ in range(3)]
        }

    def display(self):
        for face in self.faces:
            print(f"{face.capitalize()}:")
            for row in self.faces[face]:
                print(" ".join(row))
            print()

    def rotate_face(self, face, direction):
        if direction == 'clockwise':
            self.faces[face] = [list(row) for row in zip(*self.faces[face][::-1])]
        else:
            self.faces[face] = [list(row) for row in zip(*self.faces[face])][::-1]

    def move(self, face, direction='clockwise'):
        self.rotate_face(face, direction)
        
        if face == 'front':
            self._rotate_adjacent('top', 'right', 'bottom', 'left', 2, direction)
        elif face == 'back':
            self._rotate_adjacent('top', 'left', 'bottom', 'right', 0, direction)
        elif face == 'left':
            self._rotate_adjacent('top', 'front', 'bottom', 'back', 0, direction)
        elif face == 'right':
            self._rotate_adjacent('top', 'back', 'bottom', 'front', 2, direction)
        elif face == 'top':
            self._rotate_adjacent('back', 'right', 'front', 'left', 0, direction)
        elif face == 'bottom':
            self._rotate_adjacent('front', 'right', 'back', 'left', 2, direction)

    def _rotate_adjacent(self, f1, f2, f3, f4, idx, direction):
        temp = [self.faces[f1][i][idx] for i in range(3)]
        if direction == 'clockwise':
            for i in range(3):
                self.faces[f1][i][idx] = self.faces[f4][i][2-idx]
            for i in range(3):
                self.faces[f4][i][2-idx] = self.faces[f3][2-i][2-idx]
            for i in range(3):
                self.faces[f3][i][2-idx] = self.faces[f2][2-i][idx]
            for i in range(3):
                self.faces[f2][i][idx] = temp[i]
        else:
            for i in range(3):
                self.faces[f1][i][idx] = self.faces[f2][i][idx]
            for i in range(3):
                self.faces[f2][i][idx] = self.faces[f3][2-i][2-idx]
            for i in range(3):
                self.faces[f3][i][2-idx] = self.faces[f4][2-i][2-idx]
            for i in range(3):
                self.faces[f4][i][2-idx] = temp[2-i]

    def scramble(self, moves=20):
        faces = list(self.faces.keys())
        directions = ['clockwise', 'counterclockwise']
        for _ in range(moves):
            self.move(random.choice(faces), random.choice(directions))

def main():
    cube = RubiksCube()
    print("Welcome to the Rubik's Cube simulator!")
    print("Commands: 'move <face> [direction]', 'display', 'scramble', 'quit'")
    print("Faces: front, back, left, right, top, bottom")
    print("Directions: clockwise (default), counterclockwise")
    
    while True:
        command = input("Enter command: ").lower().split()
        if not command:
            continue
        
        if command[0] == 'quit':
            break
        elif command[0] == 'display':
            cube.display()
        elif command[0] == 'scramble':
            cube.scramble()
            print("Cube scrambled!")
        elif command[0] == 'move':
            if len(command) < 2:
                print("Please specify a face to move.")
                continue
            face = command[1]
            direction = command[2] if len(command) > 2 else 'clockwise'
            if face not in cube.faces:
                print("Invalid face. Choose from: front, back, left, right, top, bottom")
                continue
            if direction not in ['clockwise', 'counterclockwise']:
                print("Invalid direction. Choose either 'clockwise' or 'counterclockwise'")
                continue
            cube.move(face, direction)
            print(f"Moved {face} {direction}")
        else:
            print("Invalid command. Try 'move', 'display', 'scramble', or 'quit'")

if __name__ == "__main__":
    main()