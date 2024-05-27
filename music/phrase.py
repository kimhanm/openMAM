from core.object3D  import Object3D
from music.note     import Note
class Phrase(Object3D):
    # noteList: pitch,duration
    def __init__(self,noteList=[[0,0]]):
        super().__init__()
        time=0
        for note in noteList:
            if len(note) == 3:
                self.add(Note(note[0],time,time + note[1],visible=note[2]))
            elif len(note) == 4:
                self.add(Note(note[0],time,time + note[1],visible=note[2],color=note[3]))
            else:
                self.add(Note(note[0],time,time + note[1]))
            time += note[1]
    
            