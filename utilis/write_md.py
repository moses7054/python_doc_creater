

def write_md(content, path):     
    file_path = path

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f'Content successfully written to {file_path}')