-- ユーザー情報を格納するテーブルを作成
/**
 スキーマ情報：
 - id: INT64型の主キーで 、 NOT NULL 制約があります 。
 - name: STRING型で 、 ユーザー名を表します 。 NOT NULL 制約があります 。
 - email: STRING型で 、 メールアドレスを表します 。 NOT NULL 制約があります 。
 - password: STRING型で 、 パスワードを表します 。 NOT NULL 制約があります 。
 **/
CREATE
OR REPLACE TABLE `GITHUB_COPILOT_DEMO.users` (
  id INT64 NOT NULL,
  name STRING NOT NULL,
  email STRING NOT NULL,
  PASSWORD STRING NOT NULL,
);

-- ユーザー情報を格納するテーブルに5人分のデータを挿入
INSERT INTO
  `GITHUB_COPILOT_DEMO.users` (id, name, email, PASSWORD)
VALUES
  (
    1,
    'John Doe',
    'john.doe@example.com',
    'password1'
  ),
  (
    2,
    'Jane Smith',
    'jane.smith@example.com',
    'password2'
  ),
  (
    3,
    'Bob Johnson',
    'bob.johnson@example.com',
    'password3'
  ),
  (
    4,
    'Mary Williams',
    'mary.williams@example.com',
    'password4'
  ),
  (
    5,
    'David Lee',
    'david.lee@example.com',
    'password5'
  );
