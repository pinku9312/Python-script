import yt_dlp

url = "https://youtube.com/playlist?list=PLnFCwVWiQz4nFE9X6ADRTtBvZDIrIAL1u&si=J8FIs_xoKz7Nyu39"

ydl_opts = {
    # Save files with playlist index and title
    'outtmpl': 'Downloaded_Playlist/%(playlist_index)s - %(title)s.%(ext)s',

    # Prefer mp4 + m4a (more reliable than webm fragments), fallback to best single mp4
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',

    # Merge into mp4 container
    'merge_output_format': 'mp4',

    # Don’t stop the whole playlist if one video fails
    'ignoreerrors': True,

    # Retry fragment downloads if needed
    'fragment_retries': 10,
    'skip_unavailable_fragments': True,
    'concurrent_fragment_downloads': 1,
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

