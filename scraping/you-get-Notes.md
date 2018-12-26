
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
8. get_content
    ```
    req = request.Request(url, headers=headers)
    response = urlopen_with_retry(req)
    data = response.read()
    return data
    ```
    ```
    def get_content(url, headers={}, decoded=True):
    """Gets the content of a URL via sending a HTTP GET request.
    Args:
        url: A URL.
        headers: Request headers used by the client.
        decoded: Whether decode the response body using UTF-8 or the charset specified in Content-Type.
    Returns:
        The content as a string.
    """

    logging.debug('get_content: %s' % url)

    req = request.Request(url, headers=headers)
    if cookies:
        cookies.add_cookie_header(req)
        req.headers.update(req.unredirected_hdrs)

    response = urlopen_with_retry(req)
    data = response.read()

    # Handle HTTP compression for gzip and deflate (zlib)
    content_encoding = response.getheader('Content-Encoding')
    if content_encoding == 'gzip':
        data = ungzip(data)
    elif content_encoding == 'deflate':
        data = undeflate(data)

    # Decode the response body
    if decoded:
        charset = match1(
            response.getheader('Content-Type'), r'charset=([\w-]+)'
        )
        if charset is not None:
            data = data.decode(charset)
        else:
            data = data.decode('utf-8', 'ignore')

    return data

    ```
9. download_urls
    ```
    def download_urls(
    urls, title, ext, total_size, output_dir='.', refer=None, merge=True,
    faker=False, headers={}, **kwargs
    ):
    
    ...
    output_filename = get_output_filename(urls, title, ext, output_dir, merge)
    output_filepath = os.path.join(output_dir, output_filename)
    
    ...url_save
    ```
10. url_save
     def url_save(
    url, filepath, bar, refer=None, is_part=False, faker=False,
    headers=None, timeout=None, **kwargs
    ):
11. urlopen_with_retry
   
    
    request.urlopen(*args, **kwargs)
12. ffmpeg_download_stream in ffmpeg.py
