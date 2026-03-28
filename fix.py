import json
import glob

for filepath in glob.glob('**/*.ipynb', recursive=True):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
       
        if 'metadata' in data and 'widgets' in data['metadata']:
            del data['metadata']['widgets']
            
            
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=1)
            print(f" Fixed: {filepath}")
    except Exception as e:
        pass

print(" All notebooks cleaned and ready for GitHub!")
