from pathlib import Path

def print_all_files(directory_path):
    # Pathオブジェクト化
    p = Path(directory_path)

    # インテレータ: その階層にあるものすべて (ファイルもフォルダも)
    for item in p.iterdir():
        if item.is_file():
            # ファイルの場合の処理
            print(f"File: {item.name}")
        elif item.is_dir():
            # ディレクトリの場合の処理 (ここが再帰ポイント！)
            print(f"Dir: {item.name}")
            print_all_files(item)

print_all_files(r"./.venv")