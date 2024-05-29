import mido
from music.note import Note


def parse_midi(file_path,scaling_factor=1/500,properties={}):
    midi = mido.MidiFile(file_path)
    notes = []
    note_on_events = {}
    current_time = 0

    for track in midi.tracks:
        current_time = 0
        for msg in track:
            current_time += msg.time
            if msg.type == 'note_on' and msg.velocity > 0:
                note_on_events[(msg.note, msg.channel)] = (current_time, msg.velocity)
            elif (msg.type == 'note_off' or (msg.type == 'note_on' and msg.velocity == 0)):
                if (msg.note, msg.channel) in note_on_events:
                    start_time, velocity = note_on_events.pop((msg.note, msg.channel))
                    duration = current_time - start_time
                    # rescale ms to s
                    notes.append(Note(msg.note, start_time * scaling_factor, duration * scaling_factor, velocity,properties=properties))

    return notes