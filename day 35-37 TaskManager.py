import logging

# ログ設定: ファイルに追記モード(a)で書き込む
logging.basicConfig(
    filename='app_error_day35-37.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8',
    filemode='w' # w=上書き, a=追記。テストなので今回はwにする
)

class TaskManager:
    def __init__(self, filename):
        """
        タスクマネージャーを初期化する。
        :param filename: データを保存するファイル名
        """
        self.filename = filename
        self.tasks = []
        logging.info("TaskManager initialized.")

    def add_task(self,task):
        """
        タスクをリストに一つ追加する機能
        """
        self.tasks.append(task)
        logging.info(f"Task added: {task}")

    def save_tasks(self):
        """
        現在のself.tasksの内容をファイルに書き込む機能
        """
        with open(self.filename, mode="w", encoding='utf-8') as f:
            for task in self.tasks:
                # 3. タスクごとに改行をつけて書き込む
                f.write(f"{task}\n")
        
        # ログのXは len(self.tasks)を使うとカッコいい
        logging.info(f"Saved {len(self.tasks)} tasks to file.")

    def load_tasks(self):
        """
        タスクを一覧をファイルから読み込んでself.tasksに格納する機能
        """
        try:
            with open(self.filename, mode="r", encoding='utf-8') as f:
                # 1. 全行を読み込む
                lines = f.readlines()
                # 2. 各行の改行文字を消して、self.tasksに入れなおす
                # (例: 空のリストを作ってappendしていく、またはリスト内包表記)
                self.tasks = [line.strip() for line in lines]

            logging.info(f"Loaded {len(self.tasks)} tasks.")

        except FileNotFoundError:
            logging.warning("File not found. Created new task list.")
            self.tasks = [] # 明示的に空リストにする

    def delete_task(self, index):
        """
        タスクを完了または削除する機能
        """
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index) # 何を消したか保持しておくとログに出せる
            logging.info(f"Deleted task: {removed}")
        else:
            logging.warning(f"Invalid index: {index}")

# ...(importやクラス定義)...

def main ():
    # 1. インスタンス生成 (ファイル名は "mydb.txt"など)
    manager = TaskManager("mydb.txt")

    # 2. 起動時に既存データを読み込む
    manager.load_tasks()

    print("=== PFN Todo App (OOP Version) ===")

    while True:
        # ここにメニューを表示し、ユーザー入力を受けるロジックを書く
        selection = input("\nSelect: 1:List, 2:Add, 3:Delete, 4:Save&Exit >")

        if selection == "1":
            # 1:表示
            for i, task in enumerate(manager.tasks):
                print(f"{i + 1}. {task}")

        # 2:追加
        elif selection == "2":
            todo = input("Task name: ")
            manager.add_task(todo)
            print("Added!")

        # 3:削除
        elif selection == "3":
            for i, task in enumerate(manager.tasks):
                print(f"{i + 1}. {task}")

            del_input = input("Delete No?: ")
            try:
                # 入力を数字に変換し、0始まりにし直して渡す
                idx = int(del_input) - 1
                manager.delete_task(idx)
                print("Deleted!")
            except ValueError:
                print("数字を入力してください")

        # 4:保存して終了
        elif selection == "4":
            manager.save_tasks()
            print("Saved.Bye!")
            break

if __name__ == "__main__":
    main()

        

"""
# ファイルへの書き込み ('w'は上書きモード, 'a'は追記モード)
# encounting='utf-8' は日本語を扱う場合に必須です。
diary_content = input("今日の日記を書いてください: ")

with open('diary.txt', 'a', encoding='utf-8') as f:
    f.write(diary_content + "\n") # 改行コード \n を追加

print("保存しました。")

# ファイルの読み込み ('r' モード)
print("--- 過去の日記 ---")
with open('diary.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)
"""