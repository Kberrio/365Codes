import random
from midiutil import MIDIFile

# Define scales
SCALES = {
    'C_major': [60, 62, 64, 65, 67, 69, 71, 72],
    'G_major': [55, 57, 59, 60, 62, 64, 66, 67],
    'F_major': [53, 55, 57, 58, 60, 62, 64, 65],
}

def generate_melody(scale, num_notes):
    return [random.choice(scale) for _ in range(num_notes)]

def generate_chord_progression(scale):
    # Simple I-IV-V-I progression
    tonic = scale[0]
    subdominant = scale[3]
    dominant = scale[4]
    return [
        [tonic, tonic + 4, tonic + 7],
        [subdominant, subdominant + 4, subdominant + 7],
        [dominant, dominant + 4, dominant + 7],
        [tonic, tonic + 4, tonic + 7]
    ]

def create_midi(melody, chords, filename):
    midi = MIDIFile(2)  # 2 tracks
    track = 0
    time = 0
    midi.addTrackName(track, time, "Melody")
    midi.addTempo(track, time, 120)

    # Add melody
    for pitch in melody:
        midi.addNote(track, 0, pitch, time, 1, 100)
        time += 1

    # Add chords
    track = 1
    time = 0
    midi.addTrackName(track, time, "Chords")
    for chord in chords:
        for note in chord:
            midi.addNote(track, 0, note, time, 4, 80)
        time += 4

    # Write to disk
    with open(filename, "wb") as output_file:
        midi.writeFile(output_file)

def generate_music():
    scale_name = random.choice(list(SCALES.keys()))
    scale = SCALES[scale_name]
    
    melody = generate_melody(scale, 16)
    chords = generate_chord_progression(scale)
    
    create_midi(melody, chords, "generated_music.mid")
    print(f"Music generated in {scale_name} scale and saved as 'generated_music.mid'")

# Generate music
generate_music()