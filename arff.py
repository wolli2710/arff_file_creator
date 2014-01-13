import sys
import re

relationName = ""

if (len(sys.argv)<2):
    print("Usage:\npython arff.py MyRelationName ")
else:
    relationName = sys.argv[1]


class Arff:
    def __init__(self, r="MachineLearning"):
        self.relationName = relationName
    
    file1 = open("MMG_data.txt", 'r', encoding='utf-8')

    data = []
    firstLine = True

    for line in file1.readlines():
        if not firstLine:
            try:
                line = line.replace("\n", "")
                words = line.split("\t")
            except ValueError:
                print("cant parse file!!")
            data.append(words)
        else:
            firstLine = False
            line = line.replace("\n", "")
            words = line.split("\t")
            names = words


    def getType(value):
        v = ""
        if(type(value) == type(1)):
            v = "numeric"
        elif(type(value) == type(1.0)):
            v = "numeric"
        elif(re.match("[0-9]{4}\-[0-9]{2}\-[0-9]{2}\s[0-9]{2}\:[0-9]{2}\:[0-9]{2}", value)):
            v = "date " + "yyyy-MM-dd HH:mm:ss"
        elif(type(value) == type("string")):
            v = "string"
        elif(v == ""):
            print("Data type "+value+" not supported yet.")
        return v


    #names=["contextId","userId","deviceId","context_datetime","timeContext_timeZone","timeContext_dayOfWeek","timeContext_hourOfDay","timeContext_utc","locationContext_provider","locationContext_latitude","locationContext_longitude","locationContext_accuracy","locationContext_altitude","weatherContext_temperature","weatherContext_windSpeed","weatherContext_windDirection","weatherContext_precipitation","weatherContext_humidity","weatherContext_visibility","weatherContext_pressure","weatherContext_cloudCover","weatherContext_weatherCode","batteryContext_batteryLevel","batteryContext_batteryPlugged","batteryContext_batteryStatus","memoryContext_memory","storageContext_storageInternal","storageContext_storageExternal","audioContext_volumeAlarm","audioContext_volumeMusic","audioContext_volumeNotif","audioContext_volumeRinger","audioContext_volumeSystem","audioContext_volumeVoice","audioContext_vibrateNotif","audioContext_vibrateRinger","audioContext_audioOutput","phoneContext_state","phoneContext_roaming","phoneContext_signalStrength","phoneContext_gsm","phoneContext_networkType","taskContext_runningTask1","taskContext_runningTask2","taskContext_runningTask3","taskContext_runningTask4","taskContext_runningTask5","taskContext_runningTask6","taskContext_runningTask7","taskContext_runningTask8","taskContext_runningTask9","taskContext_runningTask10","displayContext_screenOn","displayContext_dockState","networkContext_mobileAvailable","networkContext_mobileConnected","networkContext_wifiEnabled","networkContext_wifiAvailable","networkContext_wifiConnected","networkContext_activeNetworkType","networkContext_activeNetworkSubtype","networkContext_activeNetworkRoaming","networkContext_wifiBssid","networkContext_wifiSsid","networkContext_wifiIpAddress","networkContext_wifiLinkSpeed","networkContext_wifiRssi","networkContext_bluetoothAvailable","networkContext_bluetoothEnabled","lightContext_light","lightContext_lightStandardDeviation","proximityContext_proximity","proximityContext_proximityStandardDeviation","temperatureContext_temperature","temperatureContext_temperatureStandardDeviation","pressureContext_pressure","pressureContext_pressureStandardDeviation","noiseContext_noise","noiseContext_noiseStandardDeviation","accelerationContext_acceleration","accelerationContext_accelerationStandardDeviation","orientationContext_orientationUser","orientationContext_orientationDevice","rotationContext_rotation","rotationContext_rotationStandardDeviation","playerContext_repeatMode","playerContext_shuffleMode","playerContext_apmMode","soundEffectContext_equalizerEnabled","soundEffectContext_equalizerPreset","soundEffectContext_bassBoostEnabled","soundEffectContext_bassBoostStrength","soundEffectContext_virtualizerEnabled","soundEffectContext_virtualizerStrength","soundEffectContext_reverbEnabled","soundEffectContext_reverbPreset","activityContext_activity","activityContext_mood","musicContext_Artist","musicContext_Title","musicContext_duration"]
    values = data[0]
    file2 =  open("result.arff", 'w' , encoding='utf-8')

    relationName+="\n"

    relString = '@RELATION ' + relationName
    file2.write(''+relString+'')

    for i in range(len(names)):
        str2 = "@ATTRIBUTE " + names[i] + " " + getType( values[i] ) + "\n"
        file2.write(''+str2+'')
    file2.write('''@DATA\n''')

    for line in data:
        try:
            file2.write(",".join(line)+"\n")
        except UnicodeEncodeError:
                print("cant write Data to file!!")