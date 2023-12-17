import os
import requests


logdir = os.path.join(os.getcwd(), "logs")
tokenfile = os.path.join(os.getcwd(), "token.dat")
token = None

if not os.path.exists(logdir):
    os.mkdir(logdir)

if not os.path.exists(tokenfile):
    inp = input("Wprowadź token API dla ipinfo.io: ")
    with open(tokenfile, "w") as f:
        content = """################################################
#Tutaj zamieść token dla zapytań API ipinfo.io #
################################################

token={}""".format(inp)
        f.write(content)

with open(tokenfile, "r") as f:
    imported = f.read()
    for line in imported.split("\n"):
        if "token=" in line:
            token = line.split("=")[1]


sep = "\n" + "-" * 30 + "\n"
logfiles = []
result = []
data = {}
ip = []
failure = [False]
for file in os.listdir(logdir):
    logfiles.append(os.path.join(logdir, file))

if len(logfiles) != 0:

    query = input("Wprowadź login użytkownika: ")

    for file in logfiles:
        with open(file, "r") as log:
            raw = log.read().split("\n")
            for line in raw:
                if query in line[:(15 + 3 + len(query))]:
                    ind = line.index("]")
                    result.append(line[:ind + 1])

    for res in result:
        ip = res.split(".", 3)
        ip[3] = (ip[3].split(" "))[0]
        ip = ".".join(number for number in ip)

        ts_start = res.index("[")
        timestamp = res[ts_start:]

        if ip not in list(data):
            data[ip] = timestamp
        elif ip in list(data) and timestamp > data[ip][0]:
            data[ip] = timestamp.replace("[", "").replace("]", "").split(" ")[0].replace(":", " ", 1)

    print("\nDANE POŁĄCZEŃ UŻYTKOWNIKA: [{}]".format(query))
    print("Łączna liczba rekordów IP: {}".format(len(list(data))))

    test_req = requests.get(f"https://ipinfo.io/8.8.8.8?token={token}").text[1:-1].strip().split("\n")
    for item in test_req:
        if "error" in item:
            failure[0] = True
        if failure[0] and "title" in item:
            failure.append(item.replace('"', '').strip().split(" ", 1)[1].strip(","))

    if not failure[0]:

        for ip_addr, tstamp in data.items():

            raw = requests.get(f"https://ipinfo.io/{ip_addr}?token={token}").text[1:-1].strip().split("\n")
            track = {}

            for item in raw:
                key = item.split(":")[0].replace('"', "").strip()
                value = item.split(":")[1].replace('"', "").strip().rstrip(",")
                track[key] = value

            if "error" in list(track):
                print("Błąd: {}".format(track["error"]))
            else:
                print("{0}IP:  {1}{0}".format(sep, ip_addr)),
                print(f"Ostatnie zapytanie: {tstamp}"),
                print(f"ISP: {track['org'] if 'org' in list(track) else 'brak danych'}")
                print(f"Lokalizacja (w przybliżeniu): {track['region']if 'region' in list(track) else ''}, {track['city']if 'city' in list(track) else 'brak danych'}")
                print(f"Współrzędne geograficzne: {track['loc']if 'loc' in list(track) else 'brak danych'}")
    else:
        print("Błąd połączenia z API: {}".format(failure[1]))
else:
    print("Błąd: brak logów do odczytu. Umieść logi w folderze ./logs")
