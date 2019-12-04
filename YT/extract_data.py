import json
import urllib.request

api_key = r"AIzaSyDmVJu0dTtlKe36VTd2hmywO5pzPpSsGn4"


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
videos = ['pzTal29oQeI', '-bbfFf07WNw', 'S7BycrGnaJA', '5Wq0yv73NpY', 'ELy9fOX8vtc', 'TVCEvx8JCTQ', 'xfQBkdLa6fo',
          'wxxhuzjT9aM', '_ES8x6_vxqc', '1rb3bMvDdX4', 'hx1tEXrYZLE', 'FsfyAqtiEho', 'CjLHuhOTnaI', 'rc4JmEMRHgA',
          'EYPs-ya_GDA', 'RuPx61911Oo', '-gNZtI7hbvI', '5kZRY5xlP6Y', 'R24ihv5JUeU', 'dZh0B8AYxac', 'DwAyUV6hTf8',
          'dYe1KG61o6Y', 'WrYbvyddS1s', 'f5SE47Xjx2Q', 'H4bxzKR7MQs', 'X0uv5jFaJFk', 'DY9VE3i-KcM', '_M_d7EIaXV4',
          'Fg7jIjmLyWs', 'w8Il1y1hTFc', 'cp1Aq4h3sXA', '-dsM8zPGqa0', 'NM-odCvJdrI', 'OUZ7R7AdIiI', '1SrckSJvGc8',
          'jzFTwBkIC5o', 'UyohSu-Ft_U', 'lTKuQQegNTs', 'AKr4ih5cLl4', 'mviTS_cIWXg', 'WAaL0ZhpuQM', 'PEoZLGHKvy8',
          'EFwa5Owp0-k', 'ZY1BFv8qEeM', 'yloJi635Ya8', 'mxgOjH7szdk', '4A89J4zrBw8', 'fwRiFQjMkNs', 'zO0b-l-u7Yk',
          'o0PyzrTze2U', 'ySzzjut3c9A', 'xO6AnTc0OE8', 'JHDkALRz5Rk', 'cWUb9PSp3fc', 'e9SsnK6t-z8', '-6NeAOMBBd0',
          'UAjbTiqMcfY', '-AqF-2Htv-I', 'fxpGWcACW6k', 'W6gyEbprEiQ', 'o4ah2I8YjkQ', 'n7hzomuDEIk', 'N5F4m3vPv9g',
          'rHrdFc9kC7M', 'b3U8eH8LTp0', '7YrTjyBDzlU', 'bArtnedm3eQ', 'TWpCj8jIxkY', 'iLVhkdefZLU', 'S5Zre_puj6g',
          'KSwqdl0Q9F8', 'xIBf48PP9hI', 'J6QV5wb4DeA', '4a0-WnFA1wA', '8FLXf-mW5QI', 'CidaOP7PA-o', 'ApdC4hBYxMY',
          'x6sM5sShTSs', 'W1u57UB8Zno', 'peOvrU4WVbs', 'vFfW4Vp2J8U', '2Hy4ggArPrE', 'U0aNeYZL8jY', 'HKQoRg0dZg4',
          'l14L6vI-go4', 's0dMTAQM4cw', 'H0k31FURJPg', 'oCZr4j24dsg', 'rcCu3Yia6WU', 'vTgMIivWu8o', '-fusUxEPwsw',
          'fufUZWz6fMo', 'QcXWCSyXMBM', 'Kap1dQnkKPw', 'TySxK0GyBsM', 'IecNzgdILic', '5q4D7apcQ80', 'K2-mQ4UJpJ8',
          'G0Iq45Nbevk', 'EwllBdC0Iww', 'tfDUQ5O2w8Y', 'x3dMnyYw40c', 'ZvyzHyiJYSM', '0QpKLaCmKQM', 'bncjswefp6Y',
          'vxj1ej2S-IU', '8YojGkkAhs8', 'HGqxbdLD4M0', 'i8HyfEZ0T2Q', 'pHvp_hFFY-U', 'FMZFitVUw5E', '7dXvgPrmC68',
          '96B8_Vfkxmw', 'ojFfFgcBQ3A', 'xjs7Nu3PXsM', 'behsy2owilI', 'RGNWZTFgaqg', 'YKXvBxPawZs', '_D78fDfuHPI',
          '1PayXEyRhCI', '0A1dTRCe7jg', 'KFDngVmNFFM', '8m89ZxB4-UY', 'w5o-zqII6eQ', '8QiDl-v0GHY', 'Tb0AokjhjTw',
          '9H9vF-Wlf6U', 'fKISlSd0vLk', 'ywMQFy-3bac', 'fLxKLO0h7vk', 'VkUyZRk-IWE', 'fX2ZtMAlizs', 'x82_yXchq_U',
          'aC321k61dcc', 'yWvzJSlEX-M', 'Uqxx9EFK6u0', '_WD_3cGQ0wc', 'Vhu5GsaSGYs', 'raX4BLcPepU', 'rp0frvfG-vw',
          '2BcoXCD9rWQ', 'goZm_zKByis', 'oX5nz7aBH8E', 'W8WkukMityM', 'seoFN5bCdL8', 'xsP0JvuuqAM', 'NSKGWR81Odw',
          'RTUwjLj0xsI', 'p3TOMUbDwHs', 'bE6l3LpqTUk', '8hY0Xa3G9IQ', 'YQLsxL6NutA', 'LAttC8BMtrg', 'b7IUSc43Btk',
          'tZqx2LMyud8', 'nSbAn2ZLPI8', 'KH86zMz5vxg', 'o1sCIZrs04g', '28RLTQU-_TM', 'czwFq_e-dMs', '3FD-WCcC2Pk',
          'xrYkzMjy_Nc', 'Zrt5inc2sVU', 'fVgMexZO5Z8', 'cdQl0vc9D3M', '14WFTNPXw3k', '1MczJMNIf5g', 'Vb57sYbWBN4',
          '8IMFcYy2ALo', 'y4CB8aMWZKU', 'KsT4PdcZYTg', 't_hbOW6H-Gk', 'KKPYoudGEHo', 'kPb0eKUdLfg', 'JzT8cUymD3I',
          'W035k5uk8Ew', 'oQiUBy1VNSk', 'ynFVLzdKViU', 'eZHudOOsB1k', 'exe6NgrRZlI', 'JyJ9K0WNRbM', 'ttP4cbPpmhs',
          'H12DPijkMUc', 'q_bvwm4Euq4', 'hCVNmn-9Lr8', 'UZW5wA9f9rc', '8neOn4dBY58', 'HdB2cThv4o0', '958LHYp9704',
          'vcK3RZCJ_oQ', 'LEqmpqiOxkQ', 'VX2SJZmJjV4', 'fzlzUSoMvkc', 'E0NpcA7BHnQ', '9wWg3SmY2pA', 'AGKVV4NABNA',
          'gqdx11GfxHQ', 'a0pyMOd-3Rw', 'oAjDKSlAvAY', 'EWsrWLM2IRk', 'sf3adAPotrM', 'fFJeTy1_8Ng', '8UNCvk9YXOo',
          'TLZ6W-Nqv1I', 'kdAs3UVgIGg', 'O_MQr4lHm0c', 'uFt-q8HgYpI', 'TSDOXxlT0U0', 'idfv7Lw4Y_s', 'th3KE_H27bs',
          'HzAtOyw6ACw', 'uU2L5nTSHtc', '9A7_xCrgX1U', 'byAogVoMViE', 'dsJWs6Z6eNs', 'Zd_Lbg9jroU', 'flb_S5JJC4k',
          'OQuwz64qsBM', 'R9XKRR7aKHI', 'Stt4iGMiHiI', 'ppfONdsOkWI', 'A2DzsgJSwcc', 'iB4MS1hsWXU', 'DTcJmIbn5nw',
          'RZgkjEdMbSw', 'RjquHTj4HlY', 'SGTMSV8QUrs', '87qLWFZManA', 'ON4iy8hq2hM', 'OQSMr-3GGvQ', 'a63t8r70QN0',
          '5MuIMqhT8DM', 'qAC-5hTK-4c', 'DBBA2LAsepU', 'uyMtsyzXWd4', 'vXlJEcrinwg', 'H2QxFM9y0tY', 'mCHC99MqVfE',
          'PYJ22-YYNW8', 'x6fIseKzzH0', 'UJz69v_7258', 'H8rDS6Wto5g', 'iBa9EoEbb38', 'yjYrxcGSWX4', '-BvcToPZCLI',
          'AHV_BxlNzmM', 'dDClQv1SeeE', '4xKgo0_HGRM', '7LN4L5EMmmc', 'NuBtcUGqgMc', 'Bx5hxm9iNfE', 'IYOa54hxulQ',
          'A2VAN7PtQW0', 'KwFhEB34Hj8', 'hoz5GmDhzUs', 'IsMonxeCQqE', 'HzUIUTatyZI', '_VPMVJ8fVC0', 'PMAPGcO-s1c',
          'Dxt2QE3wl90', 'iV3p2P7jA2A', '8wAgaNPRnbU', 'BW1x6F63F80', '8aP8sbQuQDg', 'LCkneiz2JPo', 'IYvJIgjLzxs',
          '1nVKV3LyCQA', 'mWfn2PLkwJg', 'YsFFYS5WPeo', 'Ea-qS1zCT5A', 'LrRzZXuE9qA', 'jrLJ4ra7s3E', 'b_8YvN1ptng',
          '1kC51RAGef4', 'pSyCiMyQVgU', '0j9XYLsV5DM', 'P3rF5t7tegs', 'MSgbPZOIBHk', 'nq9x9GtUuu4', 'RXAEN8MP8N4',
          'zO5qtrG_ln4', 'jhe4GjxrM_Q', 'AbxbOd_mtn8', 'qBGepey5_o4', 'E3e20718ioY', 'brAJ7pEudFU', 'GhxEr2-sA2I',
          'RApzagDfqdc', 'zr8wAm7i-vo', 'ppi0khS0s_8', 'RQV4jUi4Nas', '_LyR8Nhzoxw', 'VF6WPDZF9kk', '6HDc8B1RxzU',
          'Jpd_CUX2o98', '0olmZzsF4Xo', 'BriBDiBxaMY', '49edFdjw920', 'wiCRhrWpDbI', '-JkcZRBUNtw', 'D8XheaeGVlk',
          'l114-xE5JHI', 'RlsYc_w-doM', 'pmY1tiJD-us', 'aK6j-wHpGT4', 'e7A-lHlmShA', 'WbvCwPav9bA', '65kPnykzvJI',
          'nQA6AYhiv0I', 'HNYa1eaw6GU', 'nkn1r7kHNNA', 'bMivrLg5-Tk', 'o7bD7dwzWP0', 'lALDNo9xeOQ', 'DRstKX5fLcM',
          'p11E9jQB87U', 'T_5Xh9padyg', '13Rn60CEH_Y', 'pyxReIV1TQg', 'E9jb16KOjXs', 'OiMYxnCd-xU', 'U3vZCVUUDwE',
          'HKBU3lD-cBc', 'zxpuXLxNYHc', 'IBIGD4CvF1I', 'AOC0wkNlj7k', 'm0WM9CZBhus', '0MZa4PqXb_M', 'h3xQepMiiq8',
          'bFYTYWaFAYk', 'KH4EVLxeQvU', 'KZS95mHG3FA', 'l_oI1jolAXE', '49V9lElPaeo', '86708vvECJw', '5f8GMF7tKs8',
          'Yk7N76SAvzw', 'Kp3cjetx9Yw', 'kDcFHVm6e2w', 'kMcuu8mLQ0s', 'i-sLPMICQhw', 'RmpYII-Rv1s', 'M_ESrmpp2gE',
          'l3B02xqJwA4', 'vMRae0NJ9w4', '4IH_a4fPbNg', 'oUxdiitijLs', 'LILY_KnZ-Ks', '5N0SxSJGT6Y', 'oNKInxlfQfc',
          'TtyN52kxOSM', 'zO1awoY7Ccg', 'o93SGk5vWUE', 'V1ouBo_mZ0w', '_aYK5QiAiEM', 'KnKcwZH1lIQ', 'OneGXTBBLOg',
          'erNQjXRAU7s', '-DIGQKYmpUc', 'wIYCPosCVzQ', 'zOguO7c7vLE', '1_pZmc-HJ7E', 'Oyawcm7TKtM', 'xwRWna4rBq4',
          'SmWGDZgHOGs', 'BbcllWvG1hc', 'H_PU1_vCHV4', 'hb0dPXJiCIk', 'aSTxbNaHp7U', 'ebGqhdWVNP0', 'U6VNmX9kiVA',
          '1VE6v1Xhqic', 'bhcuo0hY9_8', 'oYuQLxartcM', 'IvPB4bOs-Jw', 'H9o357bF4Rk', '6rAmwFJabFU', '1PGXeSbFu_I',
          'gXM0B_3aEBI', 'YGCeCEesL9k', '6vNZxpxDARM', 'pu_cdBkmcc0', 'VcIz9svh5kI', 'sAs6zB5DlPk', '0TvBu2UAfqU',
          'y79lyCweHzE', 't78Pt91Imq0', 'DEmqbxsvnvQ', '-FiqwKm7Z2A', 'xt6_gvts32w', 's3nvkmdZj-g', 'Gl3GpVJC1sk',
          '3-k0vPH923I', 'XoVvOPWNW30', 'KlU6M986b90', 'fE3SQTl2NQg', 'To5iGXwHWcU', 'JBxU-E-W8_k', 'a7-5vWqSLm0',
          'bOYUG_x9wGs']


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
    print(get_videos_from_channel("UCOgGAfSUy5LvEyVS_LF5kdw"))
    print(get_videos_from_channel("UCou6pqxzTSYf8t-ISPmeQQw"))


def main():
    # print_channel_videos()
    generate_data()


if __name__ == "__main__":
    main()


'''
polymatter: UCgNg3vwj3xt7QOrcIDaHdFg
DW documentary: UCW39zufHfsuGgpLviKh297Q

JRE clips: UCnxGkOGNMqQEUMvroOWps6Q
Payette Forward: UCiIhoHKPMHm0tpga58IBQNQ
TED: UCAuUUnT6oDeKwE6v1NGQxug
Bon Appetit: UCbpMy0Fg74eXXkvxJrtEn3w

jolly: UCOgGAfSUy5LvEyVS_LF5kdw
thesoundproject: UCou6pqxzTSYf8t-ISPmeQQw
'''