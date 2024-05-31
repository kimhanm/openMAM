import xml.etree.ElementTree as ET
import copy
import os
import subprocess

input_file = 'test.musicxml'
backend = 'lilypond'
#backend = 'musescore'

base_name = os.path.splitext(os.path.basename(input_file))[0]

tree = ET.parse(input_file)
root = tree.getroot()
tempo = 120 # default if not specified
metronome = root.find('.//sound[@tempo]')
if metronome is not None:
    tempo = int(metronome.attrib['tempo'])
beat_duration = 60 / tempo

xml_output_dir = 'xml'
ly_output_dir = 'ly'
png_output_dir = 'png'
os.makedirs(xml_output_dir, exist_ok=True)
os.makedirs(ly_output_dir, exist_ok=True)
os.makedirs(png_output_dir, exist_ok=True)

notes = root.findall('.//note')

timestamps = []
time = 0

# generate xml file and add duration to timestamp file
with open(f'{base_name}-timestamps.txt', 'w') as file:
    for i in range(len(notes)):
        new_tree = copy.deepcopy(tree)
        new_root = new_tree.getroot()
        
        # make notes invisible using print-object attribute
        for note in new_root.findall('.//note'):
            if new_root.findall('.//note').index(note) > i:
                note.set('print-object', 'no')

        xml_file = os.path.join(xml_output_dir, f'{base_name}-{i+1:03}.musicxml')
        new_tree.write(xml_file, encoding='UTF-8', xml_declaration=True)
        
        # convert musicxml files to png with specified backend
        png_output_file = os.path.join(png_output_dir, f'{base_name}-{i+1:03}.png')
        if backend == 'lilypond':
            ly_file = os.path.join(ly_output_dir, f'{base_name}-{i+1:03}.ly')
            subprocess.run(['musicxml2ly', '-o', ly_file, xml_file])
            #subprocess.run(['lilypond', '--png', '-o', png_output_file, ly_file])
            subprocess.run(['lilypond', '--png', '-o', png_output_dir, ly_file])
        if backend == 'musescore':
            subprocess.run(['mscore', '-o', png_output_file, xml_file])

        
        duration = int(notes[i].find('duration').text)
        time += duration * beat_duration #/ 480 # 480 divisions per beat
        timestamps.append(time)

        file.write(f"file '{png_output_file}'\n")
        if i > 0:
            file.write(f"duration {time - timestamps[i-1]}\n")
        else:
            file.write(f"duration {time}\n")




#subprocess.run(['ffmpeg', '-f', 'concat',
#                '-safe', '0',
#                '-i', f'{base_name}-timestamps.txt',
#                '-vsync', 'vfr',
#                '-pix_fmt', 'yuv420p',
#                f'{base_name}.mp4'
#                ])

