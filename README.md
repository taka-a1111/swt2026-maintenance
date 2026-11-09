# swt2026-maintenance ビルド元

SWO版（taka-a1111/swo2026-maintenance の source _src）をもとに、_src/make_swt.py で原稿の文言に置き換えた template.html を作り、build.py で組み立てる。

python3 -I _src/build.py _src out/index.html（images/ は main から）
