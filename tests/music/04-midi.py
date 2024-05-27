from midi.midi import Note, parse_midi
import mido

mido.set_backend('mido.backends.pygame')
print("Using backend: ")
print(mido.backend)

midi_file_path = './midi/chaconne.mid'
notes = parse_midi(midi_file_path)

for note in notes:
    print(note)
