import json
from TikTokApi import TikTokApi

def scrape_tiktok_data():
    api = TikTokApi.get_instance()
    user = 'yenehealth' 
    user_videos = api.by_username(user, count=10) 

    data = []
    for video in user_videos:
        video_data = {
            "video_url": f"https://www.tiktok.com/@{user}/video/{video['id']}",
            "caption": video['desc'],
            "hashtags": ' '.join([f"#{tag['name']}" for tag in video.get('textExtra', [])]),
            "upload_date": video['createTime']
        }
        data.append(video_data)

    with open('tiktok_data.json', 'w') as f:
        json.dump(data, f)

if __name__ == '__main__':
    scrape_tiktok_data()

   
    google_apps_script_url = 'https://script.google.com/macros/s/AKfycbwzOlHZZw4g0Wjfg0CdcJnnXspz8DndP58Ienxdvq3HAyiOsSI2cTJdvcCA0haEZ4fpvQ/exec'
    response = requests.post(google_apps_script_url, json=tiktok_data)

    return f"Data sent with status: {response.status_code}"
