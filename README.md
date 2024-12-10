# About
A simple MIDI animation engine based on Lee Stemkoski's "Developing Graphics Frameworks with Python and OpenGL" video series.
Inspired by Stephen Malinowski's (proprietary) software http://www.musanim.com/.

 ![openMAM-demo-gernsheim-op-66](https://github.com/user-attachments/assets/8f6db687-5ec9-400b-a885-3e79e435b84d)
 
Excerpt from Friedrich Gernsheim's Op. 66 String Quartet (see https://imslp.org/wiki/String_Quartet_No.4,_Op.66_(Gernsheim,_Friedrich)) for score and shameless transcription self-plug)

## Installation
Ensure python and pip are installed.
```bash
git clone https://github.com/kimhanm/openMAM.git && cd openMAM

# create virtual environment and activate
python3 -m venv .ve
source .ve/bin/activate

pip install --requirement requirements.txt
```

## Usage
1. save midi file to `./midi/`.
2. edit parameters in `tests/music/03-multiple-parts.py`
3. run with `python -m tests.music.03-multiple-parts`
Default key bindings: `w,a,s,d` for movement, `space/control` for up/down, `shift` for sprint, `h,j,k,l` for turning, `p` for pause/unpause.


# Roadmap
The goal is to be able to specify animation information inside musescore for easy editing and playback.
Animation information such as color, geometry, etc could be added directly in musescore and exported via musicXML.
- [X] Timed Objects
- [ ] Note Effects
- musicXML parser

