# multiprocessing  in python
# import multiprocessing
import concurrent.futures
import requests


def downloadFile(url, name):
    print(f"starting downloading{name}")
    response = requests.get(url)
    open(f"files/file{name}.jpg", "wb").write(response.content)
    print(f"finished downloading{name}")


url = "https://picsum.photos/200/300"
# pros=[]
# for i in range(50):
#  #downloadFile(url,i)
#  p=multiprocessing.Process(target=downloadFile,args=[url,i])
#  p.start()
#  pros.append(p)
#
# f#or p in pros:
#  p.join()
with concurrent.futures.ProcessPoolExecutor() as executer:
    l1 = [url for i range(60)]
    l2 = [i for i in range(60)]
    results = executer.map(downloadFile, l1, l2)
    for r in results:
        print(r)
