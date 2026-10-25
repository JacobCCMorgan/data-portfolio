"""Render theme navigation from the project catalog; no project code is copied."""
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STATUS = {'in_progress':'In progress', 'implementation_complete':'Implemented; acceptance pending', 'planned':'Planned', 'deferred':'Not started', 'released':'Released', 'accepted':'Accepted'}
STATUS_ZH = {'in_progress':'實作中', 'implementation_complete':'已完成實作，待驗收', 'planned':'已規劃', 'deferred':'尚未開始', 'released':'已發布，待驗收', 'accepted':'已驗收'}


def project_table(items):
    lines=['| Project | Question and scope | Role / level | Status | Repository |', '|---|---|---|---|---|']
    for p in items:
        url=p.get('repository_url')
        link=f'[Open project]({url})' if url else 'Not published'
        lines.append(f"| **{p['project_id']}** {p['title_en']} | {p['business_question']} | {p['role']} / {p['level']} | {STATUS[p['status']]} | {link} |")
    return lines


def build():
    catalog=json.loads((ROOT/'project_catalog.json').read_text())
    projects=catalog['projects']; themes=catalog['themes']
    (ROOT/'themes').mkdir(exist_ok=True)
    main=['# Fleet Data Portfolio', '',
          'Projects organized around fleet and connected-vehicle business problems. Each implemented project has its own repository with source code, data preparation, validation, results and reproduction instructions. This repository provides navigation only.', '',
          '## Current work', '']
    active=[p for p in projects if p['status'] in {'in_progress','implementation_complete','released','accepted'}]
    main += project_table(active)
    main += ['', '## Explore by business topic', '', '| Topic | Questions covered | Projects |', '|---|---|---|']
    for t in themes:
        ps=[p for p in projects if p['primary_theme']==t['theme_id']]
        main.append(f"| [{t['title_en']}](themes/{t['slug']}.md) | {t['scope_en']} | {len(ps)} |")
        page=[f"# {t['title_en']}", '', t['scope_en'], '', f"中文分類：{t['title_zh']}", '', '[All topics](../README.md)', '', '## Projects', '']
        page += project_table(ps)
        related=[p for p in projects if t['theme_id'] in p.get('secondary_themes',[]) and p['primary_theme']!=t['theme_id']]
        if related:
            page += ['', '## Related projects', ''] + project_table(related)
        page += ['', 'Each project has one primary topic. Cross-links lead to the same project repository; they do not represent extra implementations.', '']
        (ROOT/'themes'/f"{t['slug']}.md").write_text('\n'.join(page))
    main += ['', '## How to read the portfolio', '',
             '- **Released / Accepted:** a versioned implementation and its evidence are available in the linked repository.',
             '- **Implemented; acceptance pending:** the implementation is available at its verified repository link; final review remains open.',
             '- **In progress:** implementation is underway; current results and remaining work are identified in that repository.',
             '- **Planned / Not started:** the question is cataloged; it is not a completed project or a claim of operational impact.',
             '- Project IDs are stable. Role, level and topic describe the intended scope, not a professional credential.', '',
             'The catalog retains 47 project IDs across 11 business topics. Eight projects form the first implementation batch; the other 39 remain deferred. Work advances one complete project at a time.', '',
             '## Reuse and data boundaries', '',
             'Data provenance, permitted uses and limitations are documented in each project. Synthetic demonstrations test explicitly designed scenarios; their results are not presented as measured customer or company savings.', '',
             'The index does not host production customer data, credentials or duplicate copies of project implementations.', '',
             '## Maintain the index', '',
             'Edit `project_catalog.json`, preserve Project IDs, and run `python scripts/build_index.py`. Add a repository URL only after the repository exists and its access has been verified.', '',
             '[中文導覽](README.zh-TW.md)', '']
    (ROOT/'README.md').write_text('\n'.join(main))
    zh=['# 車隊資料專案作品索引', '',
        '依業務主題瀏覽各案。完整程式、資料、測試、報告與重跑步驟保存在各案獨立 repository；此處只提供導覽。', '',
        '## 目前進行中的專案', '']
    for p in active:
        link=f"[專案 repository]({p['repository_url']})" if p.get('repository_url') else '尚未發布 repository'
        zh += [f"- **{p['project_id']} {p['title_zh']}**：{STATUS_ZH[p['status']]}。{link}。"]
    zh += ['', '## 業務主題', '', '| 分類 | 專案數 |', '|---|---|']
    for t in themes:
        zh.append(f"| [{t['title_zh']}](themes/{t['slug']}.md) | {sum(p['primary_theme']==t['theme_id'] for p in projects)} |")
    zh += ['', '已保留原 47 案與 11 個主題的對照。未開始的專案保留規劃狀態；不把規劃文件、空 repository 或相同程式的複製計為已完成作品。', '',
           '同一案可出現在不同主題的相關連結，仍只有一個主要 repository。DA／DE／DS、職級及技術為標籤，優先級不作公開導覽分類。', '',
           '各案會區分公開、合成與衍生資料，並交代分析能支持與不能支持的結論。', '']
    (ROOT/'README.zh-TW.md').write_text('\n'.join(zh))
    return {'projects':len(projects),'themes':len(themes),'active_projects':len(active)}


if __name__=='__main__':
    print(json.dumps(build()))
