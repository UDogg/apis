import requests

api_url = "https://example.com/api/upload_video"
video_file = "path_to_video.mp4"

with open(video_file, "rb") as f:
    files = {"file": f}
    response = requests.post(api_url, files=files)

print(response.status_code, response.json())
