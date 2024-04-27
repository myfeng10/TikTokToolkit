from TikTokApi import TikTokApi
import asyncio
import os
import json

# ms_token = "SML70SUCdIz3_Oi-E2vTfIi3OQlfkhy8aIBHM9mW-jp2VfFnfwpnFTXPTcPwT3BojRGl3OZhMz29AbB-vmdqBedhIs6GQQz7Qwky9mD1dkC4X6hvcrHWW2aB3C1BQqox3Lw4YNpSU0ZeeZtA"
# ms_token="yWXgBD0ef3yi3NFIlWKNSsNbXFqWwpm0PAmcuk4S9pK0dqnsWAqX16zQVUx7z4x9FbvxZXTMXDz7YHjHt9Y5i1MpfbmWnFbGVTMfyFi_g5I8aOPpWb6RYdHhPO_R" 
ms_token = ""


async def get_hashtag_videos():
    result = []
    async with TikTokApi() as api:
        await api.create_sessions(ms_tokens=[ms_token], num_sessions=1, sleep_after=3,headless=False)
        tag = api.hashtag(name="climatechange")
        async for video in tag.videos(count=30):
            result.append(video.as_dict)
    return result

if __name__ == "__main__":
    result = asyncio.run(get_hashtag_videos())
    with open('tiktok_videos.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)