import yt_dlp

url = "https://www.youtube.com/watch?v=q8MX_ldXrt8"

ydl_opts = {
    'outtmpl': 'Downloaded_Playlist/%(playlist_index)s - %(title)s.%(ext)s',

    # BEST QUALITY (no weak fallback)
    'format': 'bestvideo+bestaudio/best',

    'merge_output_format': 'mp4',

    'cookiefile': 'cookies.txt',

    # IMPORTANT: fix YouTube restrictions
    'extractor_args': {
        'youtube': {
            'player_client': ['android']
        }
    },

    'user_agent': 'Mozilla/5.0',

    'ignoreerrors': True,
    'fragment_retries': 10,
    'skip_unavailable_fragments': True,
}
    
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])