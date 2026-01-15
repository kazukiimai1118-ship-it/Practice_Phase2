import os
from dotenv import load_dotenv
import google.generativeai as genai
import logging

# ログ設定: ファイルに追記モード(a)で書き込む
logging.basicConfig(
    filename='app_error_GeminiChat.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8',
    filemode='w' # w=上書き, a=追記。テストなので今回はwにする
)

class GeminiChat:
    def __init__(self, filename):
        """
        .envからAPIキーを読み込む。
        """
        try:
            load_dotenv()
            api_key = os.getenv("GEMINI_API_KEY")

            # 2. Geminiの設定
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel("gemini-2.5-flash")
            
            self.filename = filename
            self.history = []
            logging.info("GeminiChat initialized.")

        except Exception as e:
            logging.error(f"初期化失敗: {e}")
            raise # ここでプログラムを強制停止させる

    def send_message(self,text):
        """
        ユーザーの入力を受け取り、AIに投げる。返り値として回答を返す。
        """
        try:
            response = self.model.generate_content(f"{text}")
            self.history.append(text)
            logging.info(f"Question added: {text}")
            self.history.append(response.text)
            logging.info(f"Answer added: {response.text}")
            return(response.text)

        except Exception as e: # エラー内容を e という変数に入れる
            logging.error(f"Error occurred: {e}") # e の中身 (詳細) を記録する

# ...(importやクラス定義)...

def main ():
    # 1. インスタンス生成 (ファイル名は "mydb.txt"など)
    chat = GeminiChat("history.txt")
    print("AIとの会話を開始します (exitで終了)")

    while True:
        # ここにメニューを表示し、ユーザー入力を受けるロジックを書く
        prompt = input("Please input your prompts >>")

        if prompt == "exit" or prompt == "quit":
            # 終了する。
            print("Bye!")
            break

        # 2:追加
        else:
            response = chat.send_message(prompt)
            print(f"AI: {response}")


if __name__ == "__main__":
    main()

"""
import os
from dotenv import load_dotenv
import google.generativeai as genai

# 1. .envファイルから秘密のキーを読み込む
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# 2. Geminiの設定
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash")

# 3. AIにメッセージを送る
print("AIに接続中...")
response = model.generate_content("Pythonを勉強中の私に、一言励ましの言葉をください。")

# 4. 返事を表示
print("-" * 30)
print(response.text)
print("-" * 30)
"""