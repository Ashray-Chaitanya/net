

import requests
import time

lecture_ids =[495,496,497,498,499,500,501,502,503,504,505,506,507,508,509,510,511,512,513,514,515,516,517,518,519,520,521,522,523,524,525,526,527,528,529,530,531,532,533,534,535,536,537]


url_template = "https://online.vtu.ac.in/api/v1/student/my-courses/1-ethical-hacking/lectures/{}/progress"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Cookie": ".."
}

session = requests.Session()

for lecture_id in lecture_ids:

    url = url_template.format(lecture_id)
    total_duration = 1000
    percent = 0
    max_retries = 10
    retry = 0

    while percent < 100 and retry < max_retries:
        retry += 1
        
        # Force completion - set current_time higher than total_duration
        # Force INCOMPLETE state
        body = {
            "current_time_seconds": 9999,
            "total_duration_seconds": total_duration,
            "seconds_just_watched": 9999,
            "is_completed": False
        }
        
        try:
            response = session.post(url, json=body, headers=headers)
            data = response.json()
            progress = data.get("data", {})
            if isinstance(progress, list) and len(progress) > 0:
                progress = progress[0]
            percent = progress.get("percent", 0)
            print(f"Lecture {lecture_id} -- {percent}% (attempt {retry})")
            
            if percent >= 100:
                break
        except Exception as e:
            print(f"Lecture {lecture_id} -- Error: {e}")
            break
        
        time.sleep(0.5)

    print(f"Lecture {lecture_id} completed\n")
