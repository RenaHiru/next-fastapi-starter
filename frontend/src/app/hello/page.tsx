export default async function HelloPage() {
  const res = await fetch("http://localhost:8000/hello", { cache: "no-store" });
  if (!res.ok) {
    return <pre>fetch failed: {res.status} {res.statusText}</pre>;
  }
  const data = await res.json();
  return <pre>{JSON.stringify(data, null, 2)}</pre>;
}

// ページの役割
// HelloPageはFastAPIからデータを取ってきて表示するのが目的
// APIからJSONを取得して画面に表示する

// appディレクトリはサーバコンポーネントが基本
// サーバ側でfetchを実行できるので
// asyncfunctionにしてawaitfetch(...)が書ける
// 失敗したらif(!res.ok)で処理
// 成功したらres.json()でJSONを取得 ReactではJSXで{...}埋め込み
// 生のJSONだと見にくいので、JSON.stringify(data, null, 2)で整形
// 思考の流れまとめ
// ページの目的を一文で定義する
// データを取るタイミング → サーバーで非同期処理
// エラー処理を先に考える
// 正常データの扱い方を考える（JSON → 表示）
// JSXで返す
// 👉 「目的 → データ取得 → エラー処理 → 表示」の順に考えると自然にこのコードになる。

// MDNで fetch の基礎 → async/await を理解

// Reactで「非同期にデータを取って表示する」練習

// Next.js公式の「Data Fetching」を読む

// 実際にFastAPIをバックエンドにして動かす