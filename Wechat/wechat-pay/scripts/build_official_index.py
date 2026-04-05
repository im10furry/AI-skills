#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build a local index from key WeChat Pay official documentation pages."""

from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import re
import sys
from pathlib import Path
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/135.0.0.0 Safari/537.36"
)

DEFAULT_URLS = [
    "https://pay.weixin.qq.com/doc/v3/merchant/4012062524",
    "https://pay.weixin.qq.com/doc/v3/merchant/4012791870",
    "https://pay.weixin.qq.com/doc/v3/merchant/4012791869",
    "https://pay.weixin.qq.com/doc/v3/merchant/4012076498",
    "https://pay.weixin.qq.com/doc/v3/merchant/4012075249",
    "https://pay.weixin.qq.com/doc/v3/merchant/4012075420",
    "https://pay.weixin.qq.com/doc/v3/merchant/4012081606",
    "https://pay.weixin.qq.com/doc/v3/merchant/4012365342",
    "https://pay.weixin.qq.com/doc/v3/merchant/4012068443",
    "https://pay.weixin.qq.com/doc/v3/merchant/4013070158",
    "https://pay.weixin.qq.com/doc/v3/merchant/4015478291",
    "https://pay.weixin.qq.com/doc/v3/merchant/4012791832",
    "https://pay.weixin.qq.com/doc/v3/merchant/4012791874",
    "https://pay.weixin.qq.com/doc/v3/merchant/4012791894",
    "https://pay.weixin.qq.com/doc/v3/merchant/4015459512",
    "https://pay.weixin.qq.com/doc/v3/merchant/4013071001",
    "https://pay.weixin.qq.com/doc/v3/merchant/4013071031",
    "https://pay.weixin.qq.com/doc/v3/merchant/4013071036",
    "https://pay.weixin.qq.com/doc/v3/merchant/4013071215",
    "https://pay.weixin.qq.com/doc/v3/merchant/4013071252",
    "https://pay.weixin.qq.com/doc/v3/merchant/4013070756",
    "https://pay.weixin.qq.com/doc/v3/merchant/4012153196",
    "https://pay.weixin.qq.com/doc/v3/merchant/4012154180",
    "https://pay.weixin.qq.com/doc/v3/merchant/4013053249",
    "https://pay.weixin.qq.com/doc/v3/merchant/4013053420",
    "https://pay.weixin.qq.com/doc/v3/merchant/4012551764",
    "https://pay.weixin.qq.com/doc/v3/merchant/4012068829",
    "https://pay.weixin.qq.com/doc/v3/merchant/4012068814",
    "https://pay.weixin.qq.com/doc/v3/merchant/4012078749",
    "https://pay.weixin.qq.com/doc/v3/partner/4012069852",
    "https://pay.weixin.qq.com/doc/v3/partner/4013080340",
    "https://pay.weixin.qq.com/doc/v2/merchant/4011936234",
    "https://pay.weixin.qq.com/doc/v2/merchant/4011939746",
    "https://pay.weixin.qq.com/doc/v2/merchant/4011941549",
    "https://pay.weixin.qq.com/doc/v2/merchant/4011984638",
    "https://pay.weixin.qq.com/doc/v2/merchant/4012197402",
    "https://pay.weixin.qq.com/doc/v2/merchant/4011984682",
    "https://pay.weixin.qq.com/doc/v2/merchant/4011984810",
    "https://pay.weixin.qq.com/doc/v2/merchant/4011984887",
    "https://pay.weixin.qq.com/doc/v2/merchant/4011985481",
]

DOC_LINK_RE = re.compile(
    r'<a href="(?P<href>[^"]+)" class="(?P<class_name>[^"]*sidebar-link[^"]*)"[^>]*>'
    r"(?P<body>.*?)</a>",
    re.IGNORECASE | re.DOTALL,
)
GENERIC_LINK_RE = re.compile(
    r'<a href="(?P<href>[^"]+)"[^>]*>(?P<body>.*?)</a>',
    re.IGNORECASE | re.DOTALL,
)
TITLE_RE = re.compile(r"<title>(?P<title>.*?)</title>", re.IGNORECASE | re.DOTALL)
CONTENT_TITLE_RE = re.compile(
    r'<h1 class="content-title"[^>]*>(?P<title>.*?)</h1>',
    re.IGNORECASE | re.DOTALL,
)
UPDATED_RE = re.compile(r"更新时间[:：]\s*(?P<date>\d{4}\.\d{2}\.\d{2})")
HEADING_RE = re.compile(r"<h([23])[^>]*>(?P<body>.*?)</h\1>", re.IGNORECASE | re.DOTALL)
IWIKI_DATA_RE = re.compile(r'"iwikiData":"(?P<data>.*?)","tocHeader":', re.DOTALL)
PAGE_CONTEXT_RE = re.compile(
    r'<script id="vike_pageContext" type="application/json">(?P<data>.*?)</script>',
    re.DOTALL,
)


def normalize_whitespace(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def strip_tags(fragment: str) -> str:
    without_comments = re.sub(r"<!--.*?-->", "", fragment, flags=re.DOTALL)
    without_tags = re.sub(r"<[^>]+>", "", without_comments)
    return normalize_whitespace(html.unescape(without_tags))


def canonical_doc_url(url: str, base_url: str = "https://pay.weixin.qq.com") -> str:
    parsed = urlparse(urljoin(base_url, url))
    return f"{parsed.scheme}://{parsed.netloc}{parsed.path}"


def fetch_html(url: str) -> str:
    request = Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        },
    )
    with urlopen(request, timeout=30) as response:
        encoding = response.headers.get_content_charset() or "utf-8"
        return response.read().decode(encoding, errors="replace")


def extract_first(pattern: re.Pattern[str], text: str) -> str:
    match = pattern.search(text)
    if not match:
        return ""
    payload = match.groupdict().get("title") or match.groupdict().get("date") or ""
    return strip_tags(payload)


def extract_content_html(page_html: str) -> str:
    match = IWIKI_DATA_RE.search(page_html)
    if not match:
        return ""
    try:
        return json.loads(f"\"{match.group('data')}\"")
    except json.JSONDecodeError:
        return ""


def extract_page_context(page_html: str) -> dict[str, object]:
    match = PAGE_CONTEXT_RE.search(page_html)
    if not match:
        return {}
    try:
        return json.loads(match.group("data"))
    except json.JSONDecodeError:
        return {}


def extract_headings(content_html: str) -> list[str]:
    headings: list[str] = []
    for match in HEADING_RE.finditer(content_html):
        title = strip_tags(match.group("body"))
        if title and title not in headings:
            headings.append(title)
    return headings[:20]


def dedupe_links(links: list[dict[str, str]]) -> list[dict[str, str]]:
    seen: set[tuple[str, str]] = set()
    ordered: list[dict[str, str]] = []
    for item in links:
        title = item["title"].strip()
        url = item["url"].strip()
        if not title or not url:
            continue
        key = (title, url)
        if key in seen:
            continue
        seen.add(key)
        ordered.append({"title": title, "url": url})
    return ordered


def dedupe_path_links(links: list[dict[str, str]]) -> list[dict[str, str]]:
    seen: set[tuple[str, str]] = set()
    ordered: list[dict[str, str]] = []
    for item in links:
        title = item["title"].strip()
        url = item["url"].strip()
        path = item.get("path", "").strip()
        if not title or not url:
            continue
        key = (title, url)
        if key in seen:
            continue
        seen.add(key)
        ordered.append({"title": title, "url": url, "path": path})
    return ordered


def extract_sidebar_links(page_html: str, page_url: str) -> list[dict[str, str]]:
    links: list[dict[str, str]] = []
    for match in DOC_LINK_RE.finditer(page_html):
        class_name = match.group("class_name")
        if "ellipsis" not in class_name:
            continue
        href = urljoin(page_url, html.unescape(match.group("href")))
        if "/doc/" not in href:
            continue
        title = strip_tags(match.group("body"))
        if not title:
            continue
        links.append({"title": title, "url": href})
    return dedupe_links(links)


def node_to_path_link(node: dict[str, object], page_url: str) -> dict[str, str]:
    title = normalize_whitespace(str(node.get("title", "")))
    path_items = []
    for item in node.get("pathArray") or []:
        item_title = normalize_whitespace(str(item.get("title", "")))
        if item_title:
            path_items.append(item_title)
    return {
        "title": title,
        "url": canonical_doc_url(str(node.get("url", "")), page_url),
        "path": " > ".join(path_items),
    }


def find_menu_node(
    nodes: list[dict[str, object]],
    current_url: str,
    page_url: str,
    ancestors: list[dict[str, object]] | None = None,
) -> tuple[dict[str, object], list[dict[str, object]]] | None:
    trail = ancestors or []
    for node in nodes:
        next_trail = trail + [node]
        node_url = str(node.get("url", "")).strip()
        if node_url and canonical_doc_url(node_url, page_url) == current_url:
            return node, next_trail
        children = node.get("childrenList") or []
        found = find_menu_node(children, current_url, page_url, next_trail)
        if found:
            return found
    return None


def extract_related_menu_links(page_html: str, page_url: str) -> list[dict[str, str]]:
    page_context = extract_page_context(page_html)
    menu_data = page_context.get("data", {}).get("menuData") or []
    current_url = canonical_doc_url(page_url, page_url)
    found = find_menu_node(menu_data, current_url, page_url)
    if not found:
        return []

    _, ancestors = found
    related: list[dict[str, str]] = []
    for node in ancestors[-3:]:
        for child in node.get("childrenList") or []:
            link = node_to_path_link(child, page_url)
            if link["url"] and "/doc/" in link["url"]:
                related.append(link)
    return dedupe_path_links(related)[:32]


def is_official_reference(url: str) -> bool:
    return any(
        marker in url
        for marker in (
            "pay.weixin.qq.com/doc/",
            "developers.weixin.qq.com/",
            "github.com/wechatpay-apiv3/",
            "pkg.go.dev/github.com/wechatpay-apiv3/",
            "packagist.org/packages/wechatpay/",
            "central.sonatype.com/artifact/com.github.wechatpay-apiv3/",
        )
    )


def extract_key_links(content_html: str, page_url: str) -> list[dict[str, str]]:
    links: list[dict[str, str]] = []
    for match in GENERIC_LINK_RE.finditer(content_html):
        href = urljoin(page_url, html.unescape(match.group("href")))
        if not is_official_reference(href):
            continue
        title = strip_tags(match.group("body"))
        if not title:
            continue
        links.append({"title": title, "url": href})
    return dedupe_links(links)[:36]


def snapshot_page(url: str) -> dict[str, object]:
    page_html = fetch_html(url)
    content_html = extract_content_html(page_html)
    title = extract_first(CONTENT_TITLE_RE, page_html) or extract_first(TITLE_RE, page_html)
    updated_at = extract_first(UPDATED_RE, page_html)
    headings = extract_headings(content_html)
    sidebar_links = extract_sidebar_links(page_html, url)
    related_menu_links = extract_related_menu_links(page_html, url)
    key_links = extract_key_links(content_html, url)
    return {
        "url": url,
        "title": title,
        "updated_at": updated_at,
        "headings": headings,
        "sidebar_links": sidebar_links,
        "related_menu_links": related_menu_links,
        "key_links": key_links,
    }


def render_markdown(generated_at: str, pages: list[dict[str, object]]) -> str:
    lines = [
        "# 微信支付官方文档索引快照",
        "",
        f"- 生成时间：{generated_at}",
        "- 生成方式：`python scripts/build_official_index.py`",
        "- 说明：该文件只做入口索引与快照记录。涉及精确参数、签名、证书、回调字段时，仍以对应官方页面为准。",
        "",
    ]

    for page in pages:
        title = page["title"] or page["url"]
        lines.append(f"## {title}")
        lines.append("")
        lines.append(f"- URL：{page['url']}")
        lines.append(f"- 官方更新时间：{page['updated_at'] or '未提取到'}")
        headings = page["headings"]
        if headings:
            lines.append("- 页面大纲：")
            for heading in headings:
                lines.append(f"  - {heading}")
        sidebar_links = page["sidebar_links"]
        if sidebar_links:
            lines.append("- 侧边栏子文档：")
            for link in sidebar_links:
                lines.append(f"  - {link['title']}：{link['url']}")
        related_menu_links = page["related_menu_links"]
        if related_menu_links:
            lines.append("- 目录树相关页：")
            for link in related_menu_links:
                label = link["path"] or link["title"]
                lines.append(f"  - {label}：{link['url']}")
        key_links = page["key_links"]
        if key_links:
            lines.append("- 页面内关键官方链接：")
            for link in key_links:
                lines.append(f"  - {link['title']}：{link['url']}")
        lines.append("")

    return "\n".join(lines).strip() + "\n"


def unique_urls(default_urls: list[str], extra_urls: list[str], include_defaults: bool) -> list[str]:
    ordered: list[str] = []
    seen: set[str] = set()
    sources = []
    if include_defaults:
        sources.extend(default_urls)
    sources.extend(extra_urls)
    for url in sources:
        if url in seen:
            continue
        seen.add(url)
        ordered.append(url)
    return ordered


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build a local index from key WeChat Pay official docs."
    )
    parser.add_argument(
        "--url",
        action="append",
        default=[],
        help="Additional official documentation URL to include.",
    )
    parser.add_argument(
        "--no-defaults",
        action="store_true",
        help="Only index URLs passed through --url.",
    )
    parser.add_argument(
        "--output-dir",
        default=None,
        help="Output directory for official-doc-index.md and official-doc-index.json.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    skill_dir = Path(__file__).resolve().parents[1]
    output_dir = Path(args.output_dir).resolve() if args.output_dir else skill_dir / "references"
    output_dir.mkdir(parents=True, exist_ok=True)

    urls = unique_urls(DEFAULT_URLS, args.url, include_defaults=not args.no_defaults)
    if not urls:
        print("No URLs provided.", file=sys.stderr)
        return 1

    pages: list[dict[str, object]] = []
    errors: list[str] = []
    for url in urls:
        try:
            pages.append(snapshot_page(url))
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{url} -> {exc}")

    generated_at = dt.datetime.now().astimezone().isoformat(timespec="seconds")
    payload = {
        "generated_at": generated_at,
        "seed_urls": urls,
        "pages": pages,
        "errors": errors,
    }

    json_path = output_dir / "official-doc-index.json"
    md_path = output_dir / "official-doc-index.md"
    json_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    md_path.write_text(render_markdown(generated_at, pages), encoding="utf-8")

    print(f"[OK] Wrote {md_path}")
    print(f"[OK] Wrote {json_path}")
    if errors:
        print("[WARN] Some URLs could not be fetched:")
        for error in errors:
            print(f"  - {error}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
