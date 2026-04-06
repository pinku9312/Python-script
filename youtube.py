from pytube import YouTube

def download_video():
    url = input("Enter the YouTube video URL: ")
    
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        
        print(f"Downloading: {yt.title}")
        stream.download()
        print("Download complete!")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    download_video()

