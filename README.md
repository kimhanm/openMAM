# About
A simple music animation engine based on Lee Stemkoski's "Developing Graphics Frameworks with Python and OpenGL" video series.

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
2. edit parameters in `tests/music/01-midi-import.py`
3. run with `python -m tests.music.01-midi-import`
Default key bindings: `w,a,s,d` for movement, `space/control` for up/down, `shift` for sprint, `h,j,k,l` for turning.



# Roadmap
The goal is to be able to specify animation information inside musescore for easy editing and playback.
Animation information such as color, geometry, etc could be added directly in musescore and exported via musicXML.
- Timed Objects
- musicXML parser

