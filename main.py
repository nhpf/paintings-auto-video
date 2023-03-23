import os
import urllib.request
from bs4 import BeautifulSoup
from glob import glob
from tqdm import tqdm


def download_images(web_addr: str, target_dir: str) -> None:
    html_page = urllib.request.urlopen(web_addr)
    soup = BeautifulSoup(html_page, "html.parser")

    all_links = soup.findAll("a")
    img_num = 1

    with tqdm(desc="Downloading images", total=len(all_links)) as pbar:
        for link in all_links:
            img_path = link.get("href")
            if str(img_path).startswith("/asset/"):
                os.system(
                    f"./dezoomify-rs -w 1000 https://artsandculture.google.com{img_path}"
                    f" {target_dir}/{str(img_num).zfill(3)}.jpg"
                )
                img_num += 1
            pbar.update(1)


def create_small_videos(target_dir: str) -> None:
    img_fnames = glob(os.path.join(target_dir, "*.jpg"))
    for (video_idx, img_fname) in enumerate(tqdm(img_fnames, desc="Generating videos")):
        # TODO: set zoom based on resolution and duration
        os.system(
            f"ffmpeg -hide_banner -loglevel error -framerate 25 -loop 1 -i {img_fname}"
            f' -filter_complex "[0:v]scale=8000x4000,'
            f"zoompan=z='min(zoom+0.0015,1.5)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=125,"
            f'trim=duration=10[v1];[v1]scale=-2:480[v]"'
            f' -map "[v]" -y {target_dir}/{str(video_idx).zfill(3)}.mp4'
        )


if __name__ == "__main__":
    will_download = True
    temp_dir_idx = 1
    while os.path.isdir(f"./temp{temp_dir_idx}"):
        ans = input(
            f"There is an image directory at ./temp{temp_dir_idx}. Do you want to use it? (Y/n) "
        )
        if (len(ans.strip()) == 0) or (ans.strip() not in "Nn"):
            will_download = False
            break
        temp_dir_idx += 1

    temp_dir = f"./temp{temp_dir_idx}"

    if will_download:
        os.mkdir(temp_dir)
        # web_addr = input("\nGoogle Arts and culture URL: ")
        url = "https://artsandculture.google.com/entity/georges-seurat/m0gshm"
        download_images(web_addr=url, target_dir=temp_dir)

    create_small_videos(target_dir=temp_dir)
