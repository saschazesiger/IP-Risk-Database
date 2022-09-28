from requests import get

with open("./proxies/provider.csv", "a") as f:
    f.write(f"{rooturl};{len(proxies)}\n")