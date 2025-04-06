from agent import AgentChordKnowledgeCreator
import json
import os

example_chords = ["madd9sus4b5", "7", "maj7", "m7b5"]
DATA_PATH = './data/'

for chord in example_chords:
    file_path = f"{DATA_PATH}{chord.lower()}.json"
    
    if os.path.exists(file_path):
        print(f'Skipping {chord}, analysis already exists.')
        continue
    
    chord_data = AgentChordKnowledgeCreator.get_chords(chord)
    
    with open(file_path, 'a', encoding='utf-8') as f:
        json.dump(chord_data, f, ensure_ascii=False, indent=4)
    
    print(f'Chord analysis for {chord} has been saved to {file_path}')