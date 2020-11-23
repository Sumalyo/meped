with open ("output.out","wb") as out_file:
  tar = download_url('https://raw.githubusercontent.com/Sumalyo/meped/master/a.out').content
  out_file.write(tar)
out_file.close()
