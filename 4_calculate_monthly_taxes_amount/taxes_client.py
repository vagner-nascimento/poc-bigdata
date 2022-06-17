import urllib.request, json

def get_month_total_taxes(year, month, total_amount):
    url = "http://localhost/tax?year=" + str(year) + "&month=" + str(month) + "&amount=" + str(total_amount)
    res_bys = urllib.request.urlopen(url).read()
    res_str = res_bys.decode("utf8").replace("'", '"')
    data = json.loads(res_str)

    return data
