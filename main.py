import json
import matplotlib.pyplot as plt
import datetime
from statistics import mean
import requests




print("Available CDNs: \n1.Facebook \n2.Google \n3.Akamai \n4.Amazon CloudFront \n5.Cloudflare")
print ("Press 0 for new CDN server")
input_choice = input("Please input your choice:")



cdn_server = "Facebook"
filename = 'fbpingipv6.json'
filename2 = 'fbpingipv4.json'
total_avg_lat = 0

if (input_choice=='1'):
    cdn_server = "Facebook"
    # filename = 'fbpingipv6.json'
    # filename2 = 'fbpingipv4.json'
    response = requests.get("https://atlas.ripe.net/api/v2/measurements/11423750/results/?start=1519430400")
    response_ipv4 = requests.get("https://atlas.ripe.net/api/v2/measurements/11423751/results/?start=1519430400")

elif (input_choice=='2'):
    cdn_server = "Google"
    # filename = 'googlepingipv6.json'
    # filename2 = 'googlepingipv4.json'
    response = requests.get("https://atlas.ripe.net/api/v2/measurements/11423800/results/?start=1519430400")
    response_ipv4 = requests.get("https://atlas.ripe.net/api/v2/measurements/11423797/results/?start=1519430400")


elif (input_choice=='3'):
    cdn_server = "Akamai"
    # filename = 'akamaipingipv6.json'
    # filename2 = 'akamaipingipv4.json'
    response = requests.get("https://atlas.ripe.net/api/v2/measurements/11422827/results/?start=1519430400")
    response_ipv4 = requests.get("https://atlas.ripe.net/api/v2/measurements/11422828/results/?start=1519430400")


elif (input_choice=='4'):
    cdn_server = "Newjobs"
    # filename = 'newjobspingipv6.json'
    # filename2 = 'newjobspingipv4.json'
    response = requests.get("https://atlas.ripe.net/api/v2/measurements/11423792/results/?start=1519430400")
    response_ipv4 = requests.get("https://atlas.ripe.net/api/v2/measurements/11423769/results/?start=1519430400")



elif (input_choice=='5'):
    cdn_server = "Cloudflare"
    # filename = 'newjobspingipv6.json'
    # filename2 = 'newjobspingipv4.json'
    response = requests.get("https://atlas.ripe.net/api/v2/measurements/11423728/results/?start=1519430400")
    response_ipv4 = requests.get("https://atlas.ripe.net/api/v2/measurements/11423737/results/?start=1519430400")


elif (input_choice=='0'):
    input_server = input("Please enter the CDN server name:")
    cdn_server = input_server

    input_url = input("Please provide the JSON output URL of IPv6 Ping:")
    input_url_ipv4 = input("Please provide the JSON output URL of IPv4 Ping:")


    # filename = 'newjobspingipv6.json'
    # filename2 = 'newjobspingipv4.json'
    response = requests.get(input_url)
    response_ipv4 = requests.get(input_url_ipv4)



config = response.json()
config_ipv4 = response_ipv4.json()



#IPv4
open(filename).read()

#IPv6
open(filename2).read()

i=0
while i<=1:
    print ("Hello World")
    i+=1


#config = json.loads(open(filename).read())
#config_ipv4 = json.loads(open(filename2).read())


print ("Avg\t Max\t Min\t")
i = 1

timestamp = []
avg_latency = []
for x in config:
    #print(x['max'],",\t", x['min'],",\t",x['result'][2]['rtt'])
    print (i)

    timestamp.append(i)
    avg_latency.append(x['avg'])
    i +=1
    #print (x['result'][2]['rtt'])
    # if (i>=80):
    #      break









timestamp_ipv4=[]
avg_latency_ipv4=[]
i=1
for y in config_ipv4:
    #print(x['max'],",\t", x['min'],",\t",x['result'][2]['rtt'])


    timestamp_ipv4.append(i)
    avg_latency_ipv4.append(y['avg'])
    i +=1
    #print (x['result'][2]['rtt'])
    # if (i>=80):
    #      break

print ("Count",i)







plt.xlabel('Timestamp')
plt.ylabel('Latency(ms)')
plt.plot(timestamp,avg_latency,'r',label='IPv6')
plt.plot(timestamp_ipv4,avg_latency_ipv4,'b',label='IPv4')
#plt.legend("64")
plt.legend(loc='upper right', shadow=True, fontsize='small')

total_avg_lat = mean(avg_latency)
total_avg_lat_ipv4 = mean(avg_latency_ipv4)
plt.title("Latency report of "+cdn_server+"\n(Average Latency IPv6 / IPv4 : "+str(int(total_avg_lat))+" / "+str(int(total_avg_lat_ipv4))+" ms)")


plt.show()