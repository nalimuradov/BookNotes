import json
import urllib.request

xd = r"AIzaSyDmVJu0dTtlKe36VTd2hmywO5pzPpSsGn4"


def get_videos_from_channel(channel_id):
    video_ids = []
    channel_videos = urllib.request.urlopen(f"https://www.googleapis.com/youtube/v3/search?part=snippet&"
                                            f"channelId={channel_id}&type=video&order=date&maxResults=50&key={api_key}")
    channel_videos_json = json.loads(channel_videos.read())['items']
    for x in channel_videos_json:
        video_ids.append(x['id']['videoId'])
    return video_ids


class Video:
    def __init__(self, video_id):
        metadata_url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={api_key}"
        statistics_url = f"https://www.googleapis.com/youtube/v3/videos?part=statistics&id={video_id}&key={api_key}"
        metadata_url = urllib.request.urlopen(metadata_url)
        statistics_url = urllib.request.urlopen(statistics_url)

        self.metadata_info = json.loads(metadata_url.read())
        self.statistics_info = json.loads(statistics_url.read())

        channel_id = self.metadata_info['items'][0]['snippet']['channelId']
        channel_url = urllib.request.urlopen(f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id="
                                             f"{channel_id}&key={api_key}")

        self.channel_info = json.loads(channel_url.read())

    def get_video_title(self):
        return self.metadata_info["items"][0]["snippet"]["title"]

    def get_thumbnail(self):
        return self.metadata_info['items'][0]['snippet']['thumbnails']['default']['url']

    def get_view_count(self):
        return self.statistics_info['items'][0]['statistics']['viewCount']

    def get_subscriber_count(self):
        return self.channel_info['items'][0]['statistics']['subscriberCount']


# key: video_id
# value: [title, subs, thumb, views]
videos = ['8Z8nkjmzC14', 'JDQediQb1Wc', 'xStvKju-4-o', 'Dgo7F-lpyYE', '6gk7giKER6s', '1gQR24B3ISE', 'p9bkz3hxrSM',
          '9aYuQmMJvjA', '9j-_dOze4IM', 'ixathu7U-LQ', 'i2yPxY2rOzs', 'BzcBsTou0C0', '62keA5pdykM', 'LwNPWNCA7ZI',
          'qWGgK4IrH-s', 'MynOPIJi4VY', 'hWLurYddo88', 'PRsp5p1l7DI', '2hM44nr7Wms', 'J1F32aVSYaU', 'GPtGYfCV1hY',
          '6bFN2YkN6bo', 'AOeRbuwCd-Y', 'dI9M6JZR1lM', 'qfovbG84EBg', 't3fbETsIBCY', 'G92TF4xYQcU', 'rTyEMsD-NNM',
          'Gq1Azv_B4-4', 'yMk_XtIEzH8', 'dV8b-Rw2BW8', 'IsyyRKbFi7w', '_2vW0JE18pY', 'GRtSc2Mp0WI', 'vbuwSS6jRXc',
          'msNAEaCTleQ', 'Siyg1Wn5VDs', 'CIW0H70wo0M', 'lmWE2bydekk', '62LSK62Gudc', 'hsnch676Lco', 'sJmkhV02lnM',
          '8I2fMqrruwc', 'FjwD0SOGQ1k', 'dTW_PQyUHXA', 'ytu2yV3Gn1I', 'CV7_stUWvBQ', 'WM1z8soch0Q', '8A4dqoGL62E',
          'Lbfe3-v7yE0', 'pzTal29oQeI', '-bbfFf07WNw', 'S7BycrGnaJA', '5Wq0yv73NpY', 'ELy9fOX8vtc', 'TVCEvx8JCTQ',
          'xfQBkdLa6fo', 'wxxhuzjT9aM', '_ES8x6_vxqc', '1rb3bMvDdX4', 'hx1tEXrYZLE', 'FsfyAqtiEho', 'CjLHuhOTnaI',
          'rc4JmEMRHgA', 'EYPs-ya_GDA', 'RuPx61911Oo', '-gNZtI7hbvI', '5kZRY5xlP6Y', 'R24ihv5JUeU', 'dZh0B8AYxac',
          'DwAyUV6hTf8', 'dYe1KG61o6Y', 'WrYbvyddS1s', 'f5SE47Xjx2Q', 'H4bxzKR7MQs', 'X0uv5jFaJFk', 'DY9VE3i-KcM',
          '_M_d7EIaXV4', 'Fg7jIjmLyWs', 'w8Il1y1hTFc', 'cp1Aq4h3sXA', '-dsM8zPGqa0', 'NM-odCvJdrI', 'OUZ7R7AdIiI',
          '1SrckSJvGc8', 'jzFTwBkIC5o', 'UyohSu-Ft_U', 'lTKuQQegNTs', 'AKr4ih5cLl4', 'mviTS_cIWXg', 'WAaL0ZhpuQM',
          'PEoZLGHKvy8', 'EFwa5Owp0-k', 'ZY1BFv8qEeM', 'yloJi635Ya8', 'mxgOjH7szdk', '4A89J4zrBw8', 'fwRiFQjMkNs',
          'zO0b-l-u7Yk', 'o0PyzrTze2U']


def generate_data():
    training_data = {}

    for video in videos:
        vid_data = Video(video)
        training_data[video] = (vid_data.get_video_title().lower(),
                                vid_data.get_subscriber_count(),
                                vid_data.get_thumbnail(),
                                vid_data.get_view_count())

    with open('data.txt', 'w') as outfile:
        json.dump(training_data, outfile, indent=4)
    # save locally
    return training_data


def print_channel_videos():
    print(get_videos_from_channel("UCgNg3vwj3xt7QOrcIDaHdFg"))


def main():
    # print_channel_videos()
    generate_data()


if __name__ == "__main__":
    main()


'''
sentdex: UCfzlCWGWYyIQ0aLC5w48gBQ
polymatter: UCgNg3vwj3xt7QOrcIDaHdFg
'''