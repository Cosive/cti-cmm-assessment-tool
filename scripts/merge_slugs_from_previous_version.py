import json
import sys

def merge_slugs(original_path, regenerated_path):
    try:
        # Load the JSON files
        with open(original_path, 'r') as f:
            orig = json.load(f)
        with open(regenerated_path, 'r') as f:
            regen = json.load(f)

        # Create a lookup map of ID -> Slug from the original file
        # We navigate through Objectives -> Practice Lists
        slug_map = {
            practice['id']: practice['slug'] 
            for domain in orig['objectives'].values() 
            for objective in domain.values() 
            for practice in objective['practices']
        }

        # Update the regenerated data using the lookup map
        for domain in regen['objectives'].values():
            for objective in domain.values():
                for practice in objective['practices']:
                    # Update slug if the ID exists in our map, else keep current or set empty
                    practice['slug'] = slug_map.get(practice['id'], practice.get('slug', ''))

        # Write the resulting JSON to stdout
        json.dump(regen, sys.stdout, indent=4)

    except Exception as e:
        sys.stderr.write(f"Error: {str(e)}\n")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.stderr.write("Usage: python merge_slugs.py <original_file> <regenerated_file>\n")
        sys.exit(1)
    
    merge_slugs(sys.argv[1], sys.argv[2])
