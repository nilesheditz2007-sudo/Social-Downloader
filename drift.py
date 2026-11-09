from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import re
import random
import os
from bs4 import BeautifulSoup
import html as html_lib
import yt_dlp
from user_agent import generate_user_agent

app = Flask(__name__)
CORS(app)

@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    return response

def get_fb_video(url):
    headers = {
        'User-Agent': generate_user_agent(),
        'Origin': 'https://fbdown.blog',
        'Referer': 'https://fbdown.blog/',
    }
    try:
        r = requests.post('https://fbdown.blog/get.php', headers=headers, data={'url': url}, timeout=15)
        raw = r.text.replace('\\/', '/')
        data = r.json()['data']
        title = data.get("title", "Unknown Title")
        author = data.get("author", "Unknown Author")
        duration_sec = data.get("duration", 0)
        thumbnail = data.get("thumbnail", "")
        mins = int(duration_sec // 60)
        secs = int(duration_sec % 60)
        duration_str = f"{mins:02d}:{secs:02d}"
        hd = sd = "Not available"
        for m in data.get("medias", []):
            if m.get("quality") == "HD":
                hd = m["url"]
            elif m.get("quality") == "SD" and sd == "Not available":
                sd = m["url"]
        return {
            "status": "success",
            "video": {
                "title": title,
                "author": author,
                "duration": duration_str,
                "thumbnail": thumbnail,
                "hd": hd,
                "sd": sd
            },
            "Developer": "t.me/dg_drift",
            "Main Channel": "@DGDRIFT",
            "Owner": "@DG_DRIFT"
        }
    except:
        return {
            "status": "error",
            "message": "Facebook video not found",
            "Developer": "t.me/dg_drift",
            "Main Channel": "@DGDRIFT",
            "Owner": "@DG_DRIFT"
        }


def download_insta_reel(url):
    try:
        api_key = os.getenv("IGRAM_API_KEY")
        if not api_key:
            return {"status": "error", "message": "IGRAM_API_KEY is not configured"}

        if not url or "instagram.com/" not in url.lower():
            return {"status": "error", "message": "Invalid Instagram URL"}

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Accept": "application/json"
        }

        response = requests.get(
            "https://api.igramapi.com/v1/media",
            params={"url": url.strip()},
            headers=headers,
            timeout=30
        )

        media = response.json()

        if response.status_code != 200:
            error = media.get("error", {})
            return {
                "status": "error",
                "message": error.get("message", "Instagram API request failed")
            }

        formats = media.get("formats") or []
        video_url = media.get("video_url")

        if not video_url and formats:
            video_url = formats[0].get("url")

        if not video_url:
            return {"status": "error", "message": "No video found. This post may be an image."}

        best_format = formats[0] if formats else {}
        audio_url = best_format.get("audio_url")

        download_payload = {
            "type": "video",
            "url": best_format.get("url") or video_url,
            "filename": "instagram-reel"
        }

        if audio_url:
            download_payload["audio_url"] = audio_url

        download_response = requests.post(
            "https://api.igramapi.com/v1/downloads",
            headers={**headers, "Content-Type": "application/json"},
            json=download_payload,
            timeout=120
        )

        download_data = download_response.json()

        if download_response.status_code == 200:
            hd_link = download_data.get("download_url") or video_url
        else:
            hd_link = video_url

        author = media.get("author") or {}
        if isinstance(author, dict):
            username = author.get("username", "Unknown")
        else:
            username = str(author)

        caption = media.get("caption") or f"Instagram Reel by {username}"

        duration = media.get("duration", 0)
        try:
            duration = int(duration)
            duration_text = f"{duration // 60:02d}:{duration % 60:02d}"
        except (ValueError, TypeError):
            duration_text = "Unknown"

        thumbnail = media.get("thumbnail") or ""

        sd_link = formats[-1].get("url") if len(formats) > 1 else video_url

        return {
            "status": "success",
            "video": {
                "title": caption,
                "author": username,
                "duration": duration_text,
                "thumbnail": thumbnail,
                "hd": hd_link,
                "sd": sd_link
            },
            "Developer": "t.me/dg_drift",
            "Main Channel": "@DGDRIFT",
            "Owner": "@DG_DRIFT"
        }

    except requests.exceptions.Timeout:
        return {"status": "error", "message": "Instagram API request timed out"}
    except Exception as e:
        return {"status": "error", "message": f"Instagram request failed: {str(e)}"}

def download_snapchat(url):
    headers = {
        "authority": "www.expertstool.com",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://www.expertstool.com",
        "referer": "https://www.expertstool.com/snapchat-video-downloader/",
        "user-agent": generate_user_agent()
    }
    data = {"url": url}
    try:
        response = requests.post("https://www.expertstool.com/converter.php", headers=headers, data=data, timeout=20)
        html = response.text
        def clean_link(link):
            if not link: return None
            link = link.replace("\\u0026", "&").replace("&quot;", "").strip()
            return link.split(",mediaPreviewUrl:")[0].rstrip("&")
        video_links = re.findall(r'<source[^>]+src="(https?://[^"]+)"', html)
        video_links = [clean_link(v) for v in video_links if clean_link(v)]
        img_links = re.findall(r'(poster|src)="(https?://[^"]+)"', html)
        image_links = list(set([clean_link(i[1]) for i in img_links if clean_link(i[1])]))
        return {
            "status": "success",
            "video": video_links[0] if video_links else None,
            "image": image_links[0] if image_links else None,
            "Developer": "t.me/dg_drift",
            "Main Channel": "@DGDRIFT",
            "Owner": "@DG_DRIFT"
        } if video_links or image_links else {
            "status": "error",
            "message": "Invalid Snapchat URL",
            "Developer": "t.me/dg_drift",
            "Main Channel": "@DGDRIFT",
            "Owner": "@DG_DRIFT"
        }
    except:
        return {
            "status": "error",
            "message": "Failed to fetch Snapchat data",
            "Developer": "t.me/dg_drift",
            "Main Channel": "@DGDRIFT",
            "Owner": "@DG_DRIFT"
        }

def get_pinterest_download_links(url):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'origin': 'https://www.expertstool.com',
        'referer': 'https://www.expertstool.com/pinterest-video-download/',
        'user-agent': generate_user_agent(),
    }
    data = {'url': url}
    try:
        response = requests.post('https://www.expertstool.com/pinterest-video-download/', headers=headers, data=data, timeout=20)
        html = response.text
        if "API Not Work" in html or "Invalid" in html:
            return {
                "status": "error",
                "message": "Invalid Pinterest URL",
                "Developer": "t.me/dg_drift",
                "Main Channel": "@DGDRIFT",
                "Owner": "@DG_DRIFT"
            }
        soup = BeautifulSoup(html, 'html.parser')
        for btn in soup.find_all('a', class_=re.compile(r'btn.*primary')):
            href = btn.get('href', '')
            if href.startswith('https://v') and '.mp4' in href:
                return {
                    "status": "success",
                    "video": href,
                    "Developer": "t.me/dg_drift",
                    "Main Channel": "@DGDRIFT",
                    "Owner": "@DG_DRIFT"
                }
        for img in soup.find_all('a', href=re.compile(r'pinimg\.com.*originals')):
            return {
                "status": "success",
                "photo": img['href'],
                "Developer": "t.me/dg_drift",
                "Main Channel": "@DGDRIFT",
                "Owner": "@DG_DRIFT"
            }
        return {
            "status": "error",
            "message": "No media found",
            "Developer": "t.me/dg_drift",
            "Main Channel": "@DGDRIFT",
            "Owner": "@DG_DRIFT"
        }
    except:
        return {
            "status": "error",
            "message": "Pinterest request failed",
            "Developer": "t.me/drift127",
            "Main Channel": "@DGDRIFT",
            "Owner": "@DG_DRIFT"
        }


# ============================================================
# YOUTUBE
# ============================================================

def download_youtube(url):
    try:
        if not url:
            return {
                "status": "error",
                "message": "YouTube URL is required",
                "Developer": "t.me/dg_drift",
                "Main Channel": "@DGDRIFT",
                "Owner": "@DG_DRIFT"
            }

        ydl_opts = {
            "quiet": True,
            "no_warnings": True,
            "skip_download": True,
            "noplaylist": True,
            "format": "best[ext=mp4]/best"
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)

        formats = []
        seen_urls = set()

        for f in info.get("formats", []):
            direct_url = f.get("url")
            if not direct_url or direct_url in seen_urls:
                continue
            if f.get("vcodec") == "none":
                continue

            seen_urls.add(direct_url)
            formats.append({
                "quality": f.get("format_note") or f.get("resolution") or "Original",
                "ext": f.get("ext") or "mp4",
                "url": direct_url
            })

        return {
            "status": "success",
            "title": info.get("title", "Unknown Title"),
            "author": info.get("uploader", "Unknown"),
            "duration": info.get("duration"),
            "thumbnail": info.get("thumbnail"),
            "video": formats,
            "Developer": "t.me/dg_drift",
            "Main Channel": "@DGDRIFT",
            "Owner": "@DG_DRIFT"
        }

    except Exception as e:
        return {
            "status": "error",
            "message": f"YouTube request failed: {str(e)}",
            "Developer": "t.me/dg_drift",
            "Main Channel": "@DGDRIFT",
            "Owner": "@DG_DRIFT"
        }

@app.route('/', methods=['GET'])
def index():
    return jsonify({
        "Developer": "t.me/dg_drift",
        "Endpoints": {
            "Facebook": "/facebook?video=URL",
            "Instagram": "/Instagram?video=URL",
            "Pinterest": "/Pinterest?video=URL",
            "Snapchat": "/snap?video=URL",
            "YouTube": "/youtube?video=URL"
        },
        "Main Channel": "@DGDRIFT",
        "Owner": "@DG_DRIFT"
    })

@app.route('/facebook', methods=['GET', 'POST'])
def fb(): return jsonify(get_fb_video(request.values.get("video", "").strip()))

@app.route('/Instagram', methods=['GET', 'POST'])
def insta(): return jsonify(download_insta_reel(request.values.get("video", "").strip()))

@app.route('/snap', methods=['GET', 'POST'])
def snap(): return jsonify(download_snapchat(request.values.get("video", "").strip()))

@app.route('/Pinterest', methods=['GET', 'POST'])
def pin(): return jsonify(get_pinterest_download_links(request.values.get("video", "").strip()))


@app.route('/youtube', methods=['GET', 'POST'])
def youtube():
    return jsonify(download_youtube(request.values.get("video", "").strip()))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5310)