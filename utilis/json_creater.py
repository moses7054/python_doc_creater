import json
import hashlib

def create_json_from_files(srt_path, md_path, prompt_text):
    try:
        # Read the content of the SRT file
        with open(srt_path, 'r', encoding='utf-8') as srt_file:
            srt_content = srt_file.read()
        
        # Read the content of the Markdown file
        with open(md_path, 'r', encoding='utf-8') as md_file:
            md_content = md_file.read()
        
        # Hash the prompt text
        prompt_hash = hashlib.sha256(prompt_text.encode('utf-8')).hexdigest()
        output_json_path = f"D:/coding/python_whisper_srt/static/{prompt_hash}.json"
        
        # Create a dictionary with the key-value pairs
        data = {
            "prompt": prompt_text,
            "srt": srt_content,
            "doc": md_content
        }
        
        # Write the dictionary to a JSON file
        with open(output_json_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
        
        print(f"JSON file created: {output_json_path}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# # Example usage:
# srt_file_path = 'example.srt'
# md_file_path = 'example.md'
# prompt_text = 'This is a sample prompt'

# create_json_from_files(srt_file_path, md_file_path, prompt_text)
