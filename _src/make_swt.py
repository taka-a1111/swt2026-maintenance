"""SWO版の template.html から SWT版を作る（原稿_メンテナンス事務局_SWT_261109.docx の文言に合わせる）"""
import sys
p = sys.argv[1]
t = open(p, encoding='utf-8').read()
def rep(old, new, n=1):
    global t
    c = t.count(old)
    if c != n: raise SystemExit(f'置換数が違う: {old[:40]!r} {c}件（期待 {n}）')
    t = t.replace(old, new)
# 原稿の表記「サーバ」に合わせる（タイトル・説明文・本文すべて）
rep('サーバー', 'サーバ', 19)
rep('<title>メンテナンス事務局｜サーバ・ドメイン・メールの管理をまるごとサポート｜Science Web株式会社 SWO</title>',
    '<title>メンテナンス事務局｜サーバ・ドメイン・メールの管理をまるごとサポート｜サイエンスウェブ株式会社 SWT</title>')
rep('content="Science Web株式会社 SWO"', 'content="サイエンスウェブ株式会社 SWT"')
rep('content="大切なWeb環境を、ずっと安心して使い続けるために。', 'content="大切なWebサイトを、安心・安全に使い続けるために。')
rep('<p class="mt-catch">大切なWeb環境を、ずっと安心して使い続けるために。</p>',
    '<p class="mt-catch">大切なWebサイトを、安心・安全に使い続けるために。</p>')
rep('https://science-web.online/maintenance/', 'https://science-web.tokyo/maintenance/', 4)
rep('mailto:maintenance@science-web.online', 'mailto:maintenance@science-web.tokyo', 2)
rep('Web環境の安定運用を支える', 'システム環境の安定運用を支える')
rep('<a href="mailto:team-maintenance@science-web.online">team-maintenance@science-web.online</a>　佐藤・永田',
    '<a href="mailto:maintenance@science-web.tokyo">maintenance@science-web.tokyo</a>')
rep('Web環境のことでお困りのことがありましたら', 'システム環境のことでお困りのことがありましたら')
rep('<p class="ft-brand">Science Web株式会社</p>', '<p class="ft-brand">サイエンスウェブ株式会社</p>')
rep('© Science Web株式会社 All Rights Reserved.', '© サイエンスウェブ株式会社 All Rights Reserved.')
# 更新日は原稿が空欄（2026年　月　日）。初校は公開日で入れて確認に回す
rep('<time datetime="2026-10-26">2026年10月26日</time>', '<time datetime="2026-11-11">2026年11月11日</time>')
for w in ('SWO', 'science-web.online', 'Science Web', '佐藤', 'ずっと安心'):
    if w in t: raise SystemExit(f'旧商品の語が残っている: {w}')
open(p, 'w', encoding='utf-8').write(t)
print('ok')
