class Character:

    def __init__(self, name, hp):
        self.name = name    # これが必要
        self.hp = hp        # これも必要     
    
    def introduce(self):
        print(f"私は{self.name}だ。HPは{self.hp}だ。")
    
class Wizard(Character):

    def __init__(self, name, hp, mp):
        # 1. 親クラス(Character)の __init__ を呼んで、名前とHPをセットしてもらう
        super().__init__(name, hp)

        # 2. 子クラス独自の MP をセットする
        self.mp = mp

    def cast_spell(self):
        self.mp = self.mp - 10
        print(f"魔法を唱えた!MPが10減った")

# --- クラスの定義の後にこれを追加して実行 ---

# 1. 魔法使いマーリンを作成
merlin = Wizard("Merlin", 100, 50)

# 2. 自己紹介させる
merlin.introduce()

# 3. 魔法を使わせる
merlin.cast_spell()

# 4. 本当に減ったか確認
print(f"現在のMP: {merlin.mp}")