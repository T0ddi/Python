from pytube import YouTube

def download_video(url):
    yt = YouTube(url)

    # prints out video title and other details
    print(f"Title: {yt.title}")
    #print(f"Number of views: {yt.views}")
    #print(f"Likes: {yt.likes}")
    #print(f"Dislikes: {yt.dislikes}")

    # ask if to download
    download = input("Do you want to download the video? (y/n): ")

    if download == 'y':
        # filter streams for 1080p progressive MP4
        stream_1080p = yt.streams.filter(progressive=True, file_extension='mp4', resolution="1080p").first()

        if stream_1080p:
            print("Found a suitable stream, downloading...")
            stream_1080p.download()

            print("\nVideo downloaded successfully")
        else:
            print("\nSorry, no 1080p progressive MP4 stream found. Try again with a different video.")
    else:
        print("\nYou chose not to download")

def main():
    url = input("Enter the URL of video you want to download: ")

    try:
        download_video(url)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()