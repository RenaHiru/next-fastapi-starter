import uuid
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, DateTime
from datetime import datetime
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

# ORM
class Item(Base):
    __tablename__ = "items"

    # UUID を主キーとして利用（自動生成）idカラムを定義
    # idはpythonクラス属性　Mapped型ヒント 
    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4  # 新規レコード作成時に自動でUUIDを生成
    )

    # 必須の名前（最大100文字）
    name: Mapped[str] = mapped_column(String(100))

    # 任意の説明（最大255文字、NULL可）
    description: Mapped[str | None] = mapped_column(String(255), nullable=True)

    # 作成時刻（サーバ側で自動設定：UTC）
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
