# Next.js × FastAPI Starter
Next.js と FastAPI を組み合わせた最小構成の学習用プロジェクトです。

## プロジェクト概要
Next.js（フロントエンド）と FastAPI（バックエンド）の学習用プロジェクトです。
ブートキャンプ案件に参加する前の準備として、基礎を理解しながら記録しています。

---

## 学習記録

### Day1: フォルダ構成と Next.js プロジェクト作成
**実施内容**
- `frontend`, `backend`, `reports` フォルダを作成
- Next.js プロジェクトを `frontend` に作成
```bash
cd frontend
npx create-next-app@latest . --use-npm --yes
```
- `--use-npm` : npm を使用するため
- `--yes` : 質問をスキップしてデフォルト設定を適用

### 得た知識
- create-next-app にはインストール時の質問を省略できるオプションがある
- `--use-npm` により、チームでパッケージマネージャーを統一できる
- `--yes` により素早くセットアップできるが、実務では選択肢を確認して進めることも多い
- 実務では「なぜそのオプションを選んだのか」を説明できることが大事

### 確認

- [http://localhost:3000](http://localhost:3000) にアクセスし、Next.js 初期画面が表示されたことを確認


### Day2: FastAPI 最小API（GET /hello）
FastAPI プロジェクトを backend に作成し、GET /hello を返すAPIを実装
仮想環境の作成/有効化/インストール
```bash
cd backend
python -m venv .venv
.\.venv\Scripts\activate
pip install fastapi uvicorn[standard]
```
main.py 作成・起動
```python
from fastapi import FastAPI
app = FastAPI()

@app.get("/hello")
def hello():
  return {"message": "Hello from FastAPI!"}
```
```bash
uvicorn main:app --reload --port 8000
```

### 得た知識

FastAPI：アプリ本体（ルーティング/処理）

Uvicorn：ASGIサーバー（HTTPリクエスト→アプリ→レスポンス）

ASGI：サーバーとフレームワークをつなぐ共通規格（非同期対応）

/docs は自動生成のAPI UI（Swagger UI）

### 確認

- [x] [http://localhost:8000/hello](http://localhost:8000/hello) が 200/JSON
- [x] [http://localhost:8000/docs](http://localhost:8000/docs) が表示

### 用語メモ

- **venv**: プロジェクトごとにPython環境を分離する仕組み
- **ASGI**: 非同期対応のWebサーバー/フレームワーク間インターフェース
- **fetch**: ブラウザのAPIでHTTPリクエストを送信する関数
- **Response**: fetchが返すオブジェクト（ステータスコード、ヘッダー、ボディを含む）

### Day3: Next.js から FastAPI 呼び出し
**実施内容**
- `app/hello/page.tsx` を作成し、FastAPIの `/hello` API を fetch で呼び出した
- `await fetch(...)` と `await res.json()` を使い、サーバーのレスポンスを画面に表示

```tsx
export default async function HelloPage() {
  const res = await fetch("http://localhost:8000/hello", { 
    cache: "no-store" 
  });
  if (!res.ok) {
    return <pre>fetch failed: {res.status} {res.statusText}</pre>;
  }
  const data = await res.json();
  return <pre>{JSON.stringify(data, null, 2)}</pre>;
}
```

**得た知識**
- `await fetch("URL")` = サーバーに注文して「外箱（Responseオブジェクト）」を受け取る
- `await res.json()` = 外箱を開けて中身（JSONデータ）を取り出す
- `fetch` と `res.json()` は基本的にセットで使う
- エラー時には `if (!res.ok) { ... }` でチェックできる

**確認**
- [x] [http://localhost:3000/hello](http://localhost:3000/hello) で FastAPI の JSON を表示できた

### 今後の予定

Day4: 簡単な CRUD 機能を追加し、フロントとバックの連携を確認


