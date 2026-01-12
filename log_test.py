import logging

# 設定：ここを変えるだけで、表示するレベルやフォーマットを一括管理できる
logging.basicConfig(
    filename='app.log', # ★ファイル名を指定するだけ
    level=logging.DEBUG, # これを INFO に変えると、DEBUGが表示されなくなる
    format='%(asctime)s - %(levelname)s - %(message)s' # 時間 - レベル - メッセージ
    encoding='utf-8' # 日本語文字化け防止
    filemode='a' # w=上書き, a=追記.
)

print("--- Printの場合 ---")
print("変数の値は10です")
print("エラーが起きました！")

print("\n--- Loggingの場合 ---")
logging.debug("変数の値は10です")
logging.info("処理を開始します")
logging.warning("設定ファイルがありません。デフォルトを使います")
logging.error("データベース接続に失敗しました")