
you_get notes
1. you-get/you-get executable files
    ```
    you_get.main(repo_path=_filepath) //_filepath is current dos command path
    ```
2.call main in common.py ( fake_headers in common.py)
  ```
  def main(**kwargs):
    script_main(any_download, any_download_playlist, **kwargs)
  ```
3. script_main
    ```
    download_main(
            download, download_playlist,
            URLs, args.playlist,
            output_dir=args.output_dir, merge=not args.no_merge,
            info_only=info_only, json_output=json_output, caption=caption,
            password=args.password,
            **extra
        )
     ```
4.download_main
   ```
   def download_main(download, download_playlist, urls, playlist, **kwargs):
    for url in urls:
        if re.match(r'https?://', url) is None:
            url = 'http://' + url

        if playlist:
            download_playlist(url, **kwargs)
        else:
            download(url, **kwargs)
   ```
5.download(url, **kwargs)
  ```
  you_get.extractors.extractors for each SITE  
  like kuwo.py
  ```
6.kuwo_download in kuwo.py
  ```
  def kuwo_download(url, output_dir = '.', merge = True, info_only = False, **kwargs):
    if "www.kuwo.cn/yinyue" in url:
        rid=match1(url,'yinyue/(\d+)')
        kuwo_download_by_rid(rid,output_dir, merge, info_only)
    else:
        kuwo_playlist_download(url,output_dir,merge,info_only)
  ```
7.kuwo_download_by_rid
 ```
 def kuwo_download_by_rid(rid, output_dir = '.', merge = True, info_only = False):
    html=get_content("http://player.kuwo.cn/webmusic/st/getNewMuiseByRid?rid=MUSIC_%s"%rid)
    title=match1(html,r"<name>(.*)</name>")
    #to get title
    #format =aac|mp3 ->to get aac format=mp3 ->to get mp3
    url=get_content("http://antiserver.kuwo.cn/anti.s?format=mp3&rid=MUSIC_%s&type=convert_url&response=url"%rid)
    songtype, ext, size = url_info(url)
    print_info(site_info, title, songtype, size)
    if not info_only:
        download_urls([url], title, ext, size, output_dir)
 ```
