import mido

class Note:
    def __init__(self, note, start_time, duration, velocity):
        self.note = note
        self.start_time = start_time
        self.duration = duration
        self.velocity = velocity

    def __repr__(self):
        return f"Note(note={self.note}, start_time={self.start_time}, duration={self.duration}, velocity={self.velocity})"


def parse_midi(file_path):
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
                    notes.append(Note(msg.note, start_time, duration, velocity))

    return notes