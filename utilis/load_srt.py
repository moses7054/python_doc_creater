
def load_srt(tpath):
    with open(tpath, 'r', encoding='utf-8') as file:
        srt_content = file.read()
    print("srt_content")
    return srt_content