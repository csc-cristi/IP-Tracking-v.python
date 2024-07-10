import urllib.request
import json
import time







class Data:
    def __init__(self, city, region, country, loc, postal, timezone):
        self.city = city
        self.region = region
        self.country = country
        self.loc = loc
        self.postal = postal
        self.timezone = timezone

def main():
    print(" ▄█     ▄███████▄          ███        ▄████████    ▄████████  ▄████████    ▄█   ▄█▄    ▄████████    ▄████████ \r\n███    ███    ███      ▀█████████▄   ███    ███   ███    ███ ███    ███   ███ ▄███▀   ███    ███   ███    ███ \r\n███▌   ███    ███         ▀███▀▀██   ███    ███   ███    ███ ███    █▀    ███▐██▀     ███    █▀    ███    ███ \r\n███▌   ███    ███          ███   ▀  ▄███▄▄▄▄██▀   ███    ███ ███         ▄█████▀     ▄███▄▄▄      ▄███▄▄▄▄██▀ \r\n███▌ ▀█████████▀           ███     ▀▀███▀▀▀▀▀   ▀███████████ ███        ▀▀█████▄    ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   \r\n███    ███                 ███     ▀███████████   ███    ███ ███    █▄    ███▐██▄     ███    █▄  ▀███████████ \r\n███    ███                 ███       ███    ███   ███    ███ ███    ███   ███ ▀███▄   ███    ███   ███    ███ \r\n█▀    ▄████▀              ▄████▀     ███    ███   ███    █▀  ████████▀    ███   ▀█▀   ██████████   ███    ███ \r\n                                     ███    ███                           ▀                        ███    ███ \r\n                                                                                                              \r\n                                                                                                              " )
    print("(Python Version)")
    print(" ")
    ip = input("Enter IP: ")
    url = f"https://ipinfo.io/{ip}/json"

    try:
        with urllib.request.urlopen(url) as response:
            responseData = response.read().decode('utf-8')
            ipInfo = json.loads(responseData)

            print(" ")
            print("[+] Request Successfully Made")

            ipData = Data(
                city=ipInfo['city'],
                region=ipInfo['region'],
                country=ipInfo['country'],
                loc=ipInfo['loc'],
                postal=ipInfo['postal'],
                timezone=ipInfo['timezone']
            )

            
            print(" ")
            print(f"Country: {ipData.country}")
            print(f"City: {ipData.city}")
            print(f"Coordinates: {ipData.loc}")
            print(f"Region: {ipData.region}")
            print(f"Timezone: {ipData.timezone}")

            time.sleep(10)

    except Exception as ex:
        print(f"Error: {ex}")

if __name__ == "__main__":
    main()


