from TikTokApi import TikTokApi
import requests

def scrape_tiktok_data(request):
    api = TikTokApi()
    username = "yenehealth" 
    user_videos = api.user(username=username).videos(count=5)

    tiktok_data = []

    for video in user_videos:
        video_url = video.video_url
        caption = video.caption
        hashtags = ', '.join([tag.name for tag in video.hashtags])
        upload_date = video.create_time

        tiktok_data.append({
            'video_url': video_url,
            'caption': caption,
            'hashtags': hashtags,
            'upload_date': upload_date,
        })

   
    google_apps_script_url = 'https://script.google.com/macros/s/AKfycbwzOlHZZw4g0Wjfg0CdcJnnXspz8DndP58Ienxdvq3HAyiOsSI2cTJdvcCA0haEZ4fpvQ/exec'
    response = requests.post(google_apps_script_url, json=tiktok_data)

    return f"Data sent with status: {response.status_code}"
