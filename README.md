# ImageEditor

簡単な画像編集用アプリ。フォルダー内のファイルを一括で処理します。

## ダウンロード

最新バージョンは以下のリンクからダウンロードできます。

Windows: [ダウンロード](https://github.com/yuu-s23/ImageEditor/releases/download/v1.0.0/ImageEditor_win.zip)

Mac: [ダウンロード](https://github.com/yuu-s23/ImageEditor/releases/download/v1.0.0/ImageEditor_mac.zip)

## 機能一覧

- 画像圧縮  
  1~100のレベルで設定できます
- 画像のリサイズ
- 画像名をランダムな英字10文字への変更
- EXIF情報の削除

## アプリ化方法

アプリ化にはPyInstallerを利用しています。

### Windows

`file_version_info.txt`にバージョンを記載します。

```txt
1.0.0
```

以下のコマンドを順に実行します。

```bash
create-version-file metadata.yml --outfile file_version_info.txt
```

```bach
pyinstaller ImageEditor_win.spec
```

### Mac

バージョンを変更します。

```txt:ImageEditor_mac.spec
...
app = BUNDLE(coll,
             ...
             version='1.0.0',
             ...
           )
```

以下のコマンドを実行します。

```bash
pyinstaller ImageEditor_mac.spec
```

## 注意点

- Windows環境では日本語フォルダーを選択すると失敗します

## ライセンス

MIT License