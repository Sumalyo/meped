import requests as req
import subprocess as sp
def download_url(url):
  res = req.get(url)
  #print(res)
  #print(res.content)
  return res
with open ("output.out","wb") as out_file:
  tar = download_url('https://raw.githubusercontent.com/Sumalyo/meped/master/a.out').content
  out_file.write(tar)
out_file.close()
