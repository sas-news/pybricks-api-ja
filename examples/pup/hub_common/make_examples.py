#!/usr/bin/env python3
"""Generates hub-specific examples from common template script."""

import pathlib

# ビルド用ディレクトリを作る。
dir_path = pathlib.Path(__file__).parent
build_path = dir_path / "build"
build_path.mkdir(exist_ok=True)

# 変換対象のスクリプト一覧を取得する。
file_paths = [f for f in dir_path.glob("*.py") if f.stem != "make_examples"]

# テンプレートスクリプトをすべて処理する
for file_path in file_paths:
    with open(file_path) as template:
        # 1行目にハブの情報が書かれている
        hubs = template.readline().strip().split()[3:]

        print("Converting", template.name, "to", hubs)

        for hub in hubs:
            # ハブ別の出力スクリプトのパス。
            gen_path = build_path / (file_path.stem + "_" + hub.lower() + ".py")

            # 読み取り位置を戻してヘッダ行を飛ばす。
            template.seek(0)
            template.readline()

            # 出力先スクリプトを開く:
            with open(gen_path, "w") as dest_file:
                # スクリプトを1行ずつ読む。
                for line in template:
                    # ハブ名があれば置き換える。
                    dest_file.writelines(line.replace("ThisHub", hub))
