import argparse, json, re
from pathlib import Path

FILE = Path("data/site.json")

def clean(value): return (value or "").strip()
def find(videos, video_id):
    return next((v for v in videos if v["id"] == video_id), None)

parser = argparse.ArgumentParser()
for name in ("action", "id", "title", "url", "thumbnail", "description", "genre", "status", "order"):
    parser.add_argument(f"--{name}", default="")
args = parser.parse_args()
data = json.loads(FILE.read_text(encoding="utf-8"))
videos = data.setdefault("videos", [])
action, video_id = clean(args.action), clean(args.id)

if action == "add":
    video_id = video_id or re.sub(r"[^a-z0-9]+", "-", clean(args.title).lower()).strip("-") or f"video-{len(videos)+1}"
    if find(videos, video_id): raise SystemExit("That Video ID already exists. Use a different ID.")
    videos.append({"id":video_id,"title":clean(args.title),"url":clean(args.url),"thumbnail":clean(args.thumbnail),"description":clean(args.description),"genre":clean(args.genre),"status":clean(args.status) or "published","order":int(args.order or len(videos)+1)})
else:
    video = find(videos, video_id)
    if not video: raise SystemExit("Video ID not found.")
    if action == "delete": videos.remove(video)
    elif action == "hide": video["status"] = "hidden"
    elif action == "show": video["status"] = "published"
    elif action == "feature": data.setdefault("site", {})["featuredVideoId"] = video_id
    elif action == "update":
        for key in ("title", "url", "thumbnail", "description", "genre", "status"):
            value = clean(getattr(args, key))
            if value: video[key] = value
        if clean(args.order): video["order"] = int(args.order)
    else: raise SystemExit("Choose an action.")
FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
