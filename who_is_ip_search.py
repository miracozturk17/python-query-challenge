import requests
import pyodbc
from ipwhois import IPWhois

def ip_bilgisi_al(ip_adresi):
    try:
        ip_whois = IPWhois(ip_adresi)
        rdap_result = ip_whois.lookup_rdap()
        ulke = rdap_result["asn_country_code"]
        as_numarasi = rdap_result["asn"]
        as_adi = rdap_result["asn_description"]

        geo_response = requests.get(f"http://ip-api.com/json/{ip_adresi}")
        geo_data = geo_response.json()
        
        print(geo_data)
        
        sehir = geo_data["city"]
        bolge = geo_data["regionName"]

        return {
            "ip": ip_adresi,
            "ulke": ulke,
            "sehir": sehir,
            "bolge": bolge,
            "as_numarasi": as_numarasi,
            "as_adi": as_adi
        }
    except Exception as e:
        print(f"Hata: {e}")
        return None

server = "SERVER"
database = "DATABASE"
username = "USER"
password = "PASSWORD"

connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
conn = pyodbc.connect(connection_string)
cursor = conn.cursor()

cursor.execute("SELECT ip_adresi FROM tIPKontrol ORDER BY tarih")
ip_list = [row[0] for row in cursor.fetchall()]

for ip_adresi in ip_list:
    ip_bilgisi = ip_bilgisi_al(ip_adresi)

    if ip_bilgisi:
        cursor.execute("""
            INSERT INTO ip_bilgileri (ip, ulke, sehir, bolge, as_numarasi, as_adi)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            ip_bilgisi["ip"],
            ip_bilgisi["ulke"],
            ip_bilgisi["sehir"],
            ip_bilgisi["bolge"],
            ip_bilgisi["as_numarasi"],
            ip_bilgisi["as_adi"]
        ))
        conn.commit()

cursor.close()
conn.close()