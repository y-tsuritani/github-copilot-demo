-- クレジットカード利用明細を格納するテーブルを作成
/**
 スキーマ情報：
 - id: INT64型の主キーで 、 自動的にインクリメントされます 。
 - user_id: INT64型で 、 ユーザーIDを表します 。 NOT NULL 制約があります 。
 - date: DATE型で 、 取引が行われた日付を表します 。 NOT NULL 制約があります 。
 - amount: INT64型で 、 取引金額を表します 。 NOT NULL 制約があります 。
 - store: STRING 型で 、 取引が行われた店舗名を表します 。 NOT NULL 制約があります 。
 **/
CREATE
OR REPLACE TABLE `GITHUB_COPILOT_DEMO.transactions` (
  id INT64 NOT NULL,
  user_id INT64 NOT NULL,
  date DATETIME NOT NULL,
  amount INT64 NOT NULL,
  store STRING NOT NULL,
);

-- -- クレジットカード利用明細を格納するテーブルにデータを挿入
-- INSERT INTO
--   `GITHUB_COPILOT_DEMO.transactions` (id, user_id, date, amount, store)
-- VALUES
--   (1, 1, '2022-01-01T00:00:00', 1000, 'Store A'),
--   (2, 1, '2022-01-02T00:00:00', 2000, 'Store B'),
--   (3, 2, '2022-01-03T00:00:00', 3000, 'Store C'),
--   (4, 2, '2022-01-04T00:00:00', 4000, 'Store D'),
--   (5, 3, '2022-01-05T00:00:00', 5000, 'Store E');
