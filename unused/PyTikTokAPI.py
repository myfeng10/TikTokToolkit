import unused.PyTikTokAPI as PyTikTokAPI

cookie = {
  "s_v_web_id": "verify_lubcd19o_jM4OwGjK_5kRD_4Eg2_8OX6_JeRA8LH50D2P",
  "tt_webid": "1%7CSKY2Jzc__25VYb7fsSXnBCz_90xwsEGKbLpqgQO-VsM%7C1711639444%7C8a2d05fd4a38b94d098c788a8389c9fc0736319633ad93ab6e9a4d504889a64a"
}


api = PyTikTokAPI(cookie=cookie)
user_videos = api.getLikesByUserName("fcbarcelona")
print(user_videos)