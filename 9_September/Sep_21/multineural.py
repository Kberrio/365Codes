import numpy as np
import mido
from mido import Message, MidiFile, MidiTrack

class NeuralNetwork:
    def __init__(self, input_nodes, hidden_nodes, output_nodes, learning_rate):
        self.input_nodes = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes
        self.learning_rate = learning_rate
        
        self.weights_ih = np.random.normal(0.0, pow(self.hidden_nodes, -0.5), (self.hidden_nodes, self.input_nodes))
        self.weights_ho = np.random.normal(0.0, pow(self.output_nodes, -0.5), (self.output_nodes, self.hidden_nodes))
        
        self.activation_function = lambda x : 1 / (1 + np.exp(-x))

    def train(self, inputs_list, targets_list):
        inputs = np.array(inputs_list, ndmin=2).T
        targets = np.array(targets_list, ndmin=2).T
        
        hidden_inputs = np.dot(self.weights_ih, inputs)
        hidden_outputs = self.activation_function(hidden_inputs)
        
        final_inputs = np.dot(self.weights_ho, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)
        
        output_errors = targets - final_outputs
        hidden_errors = np.dot(self.weights_ho.T, output_errors)
        
        self.weights_ho += self.learning_rate * np.dot((output_errors * final_outputs * (1.0 - final_outputs)), np.transpose(hidden_outputs))
        self.weights_ih += self.learning_rate * np.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)), np.transpose(inputs))

    def query(self, inputs_list):
        inputs = np.array(inputs_list, ndmin=2).T
        hidden_inputs = np.dot(self.weights_ih, inputs)
        hidden_outputs = self.activation_function(hidden_inputs)
        final_inputs = np.dot(self.weights_ho, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)
        return final_outputs

def generate_music(nn, num_notes=50):
    midi_file = MidiFile()
    track = MidiTrack()
    midi_file.tracks.append(track)

    track.append(Message('program_change', program=0, time=0))

    current_input = np.random.rand(12, 1)  # Start with random 12-note input
    for _ in range(num_notes):
        output = nn.query(current_input)
        note = int(np.argmax(output) * 127 / 11)  # Map to MIDI note range
        velocity = int(np.max(output) * 127)  # Use max activation as velocity
        
        track.append(Message('note_on', note=note, velocity=velocity, time=64))
        track.append(Message('note_off', note=note, velocity=velocity, time=64))
        
        current_input = np.roll(current_input, -1)
        current_input[-1] = [note / 127]  # Normalize and feed back as input

    midi_file.save('generated_music.mid')

def train_network(nn, epochs=1000):
    training_data = np.random.rand(100, 12)  # Generate random training data
    for _ in range(epochs):
        for data in training_data:
            inputs = data
            targets = np.roll(data, -1)  # Use shifted input as target
            nn.train(inputs, targets)

if __name__ == "__main__":
    nn = NeuralNetwork(12, 24, 12, 0.1)
    train_network(nn)
    generate_music(nn)
    print("Music generated and saved as 'generated_music.mid'")