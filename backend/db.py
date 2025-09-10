from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
# 「設計図」を作るための親クラス テーブルと、Pythonのクラス繋ぐObject-Relational Mapper
# ORMは翻訳機 pythonコード命令SQL文に翻訳する　デクララティブベースはクラス
# sessionmaker 設計図とやりとりするセッションの工場 エンジン　DBとやりとりするための接続

# SQLite のDBファイル（backend/app.db）が自動で作られます
DATABASE_URL = "sqlite:///./app.db"
# sqlite:///直接ファイルのパス 
# SQLiteデータベースに接続します。そして、ここから先はファイルへの道筋（パス）を書きます


# SQLite では check_same_thread=False が必要
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)

# セッション（DB と会話する「窓口」）
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# トランザクションの制御　autocommit=false 変更が確定されることがない
# パフォーマンスの最適化autoflush=false データベースの変更を自動的にフラッシュしない

# モデル（テーブル定義）の親クラス
class Base(DeclarativeBase):
    pass
  
# 作るが何もしない