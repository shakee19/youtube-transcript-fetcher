from utils import extract_video_id

url1 = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
url2 = "https://youtu.be/dQw4w9WgXcQ"

print(extract_video_id(url1))
print(extract_video_id(url2))