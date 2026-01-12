import logging

# ログ設定: ファイルに追記モード(a)で書き込む
logging.basicConfig(
    filename='app_log_error_research.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8',
    filemode='w' # w=上書き, a=追記。テストなので今回はwにする
)

def divide(a, b):
    logging.info(f"割り算開始: {a} / {b}")
    try:
        result = a / b
        logging.info(f"計算成功: {result}")
        return result
    except Exception as e:
        # logging.errorだけでは詳細が足りないことがあるが、まずはここから
        logging.error(f"計算エラー発生: {e}")
        return None

# テスト実行
divide(10, 2)
divide(5, 0) # バグの引き金
divide(20, 4)