
import urllib.request
import urllib.parse
import json

BASE_URL = "https://api.dharun.dev/v1/bullion/history"

metals = ["gold", "platinum"]

for metal in metals:

    print("\n" + "=" * 60)
    print(f"TESTING: {metal.upper()} 999")
    print("=" * 60)

    params = {
        "metal": metal,
        "purity": 999,
        "days": 184
    }

    query_string = urllib.parse.urlencode(params)
    url = f"{BASE_URL}?{query_string}"

    try:
        request = urllib.request.Request(
            url,
            headers={"User-Agent": "GoldSenseAI-DataAnalysis/1.0"}
        )

        with urllib.request.urlopen(request, timeout=30) as response:
            print("Status Code:", response.status)

            raw_data = response.read().decode("utf-8")
            data = json.loads(raw_data)

            print("\nResponse Structure:")
            print(json.dumps(data, indent=2)[:5000])

    except Exception as error:
        print("Error:", error)