import json
import asyncio
from TikTokApi import TikTokApi

async def scrape_tiktok_data():
    # Using TikTokApi within a context manager
    async with TikTokApi() as api:
        # Define the username to scrape
        username = 'yenehealth'  # Replace with the actual TikTok username

        # Fetch user videos using the API
        user = api.user(username=username)
        user_videos = user.videos(count=10)

        data = []
        async for video in user_videos:
            video_data = {
                "video_url": f"https://www.tiktok.com/@{username}/video/{video['id']}",
                "caption": video['desc'],
                "hashtags": ' '.join([f"#{tag['name']}" for tag in video.get('textExtra', [])]),
                "upload_date": video['createTime']
            }
            data.append(video_data)
            print(video_data)

        # Write the collected data to a JSON file
        with open('tiktok_data.json', 'w') as f:
            json.dump(data, f)
        print("Data written to tiktok_data.json")

# Running the async function
if __name__ == '__main__':
    asyncio.run(scrape_tiktok_data())
