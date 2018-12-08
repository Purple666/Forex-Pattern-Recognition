import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import numpy as np
import time
import functools

totalStart = time.time()
date,bid,ask = np.loadtxt('GBPUSD1d.txt', unpack=True, delimiter=',', converters={0:mdates.bytespdate2num('%Y%m%d%H%M%S')})
avgLine = ((bid+ask)/2)

def percentChange(startPoint, currentPoint):
    if startPoint == 0:
        return 100.00
    else:
        try:
            x = ((float(currentPoint - startPoint)/abs(startPoint))*100.00)
            if x == 0.0:
                return 0.000000001
            else:
                return x
        except:
            return 0.000000001

def patternStorage():
    patStartTime = time.time()
    x = len(avgLine) - 51
    y = 22
    while y < x:
        pattern = []
        p1 = percentChange(avgLine[y-21], avgLine[y-20])
        p2 = percentChange(avgLine[y-21], avgLine[y-19])
        p3 = percentChange(avgLine[y-21], avgLine[y-18])
        p4 = percentChange(avgLine[y-21], avgLine[y-17])
        p5 = percentChange(avgLine[y-21], avgLine[y-16])
        p6 = percentChange(avgLine[y-21], avgLine[y-15])
        p7 = percentChange(avgLine[y-21], avgLine[y-14])
        p8 = percentChange(avgLine[y-21], avgLine[y-13])
        p9 = percentChange(avgLine[y-21], avgLine[y-12])
        p10 = percentChange(avgLine[y-21], avgLine[y-11])
        p11 = percentChange(avgLine[y-21], avgLine[y-10])
        p12 = percentChange(avgLine[y-21], avgLine[y-9])
        p13 = percentChange(avgLine[y-21], avgLine[y-8])
        p14 = percentChange(avgLine[y-21], avgLine[y-7])
        p15 = percentChange(avgLine[y-21], avgLine[y-6])
        p16 = percentChange(avgLine[y-21], avgLine[y-5])
        p17 = percentChange(avgLine[y-21], avgLine[y-4])
        p18 = percentChange(avgLine[y-21], avgLine[y-3])
        p19 = percentChange(avgLine[y-21], avgLine[y-2])
        p20 = percentChange(avgLine[y-21], avgLine[y-1])
        p21 = percentChange(avgLine[y-21], avgLine[y])
        outcomeRange = avgLine[y+20:y+30]
        currentPoint = avgLine[y]
        try:
            avgOutcome = (functools.reduce(lambda x, y: x+y, outcomeRange) / len(outcomeRange))
        except Exception as e:
            print (str(e))
            avgOutcome=0
        futureOutcome = percentChange(currentPoint, avgOutcome)
        pattern.append(p1)
        pattern.append(p2)
        pattern.append(p3)
        pattern.append(p4)
        pattern.append(p5)
        pattern.append(p6)
        pattern.append(p7)
        pattern.append(p8)
        pattern.append(p9)
        pattern.append(p10)
        pattern.append(p11)
        pattern.append(p12)
        pattern.append(p13)
        pattern.append(p14)
        pattern.append(p15)
        pattern.append(p16)
        pattern.append(p17)
        pattern.append(p18)
        pattern.append(p19)
        pattern.append(p20)
        pattern.append(p21)
        patternAr.append(pattern)
        performanceAr.append(futureOutcome)
        y += 1
    patEndTime = time.time()
    print ("pattern storage took", round(patEndTime-patStartTime, 3), "seconds")

def currentPattern():
    cp1 = percentChange(avgLine[-22], avgLine[-21])
    cp2 = percentChange(avgLine[-22], avgLine[-20])
    cp3 = percentChange(avgLine[-22], avgLine[-19])
    cp4 = percentChange(avgLine[-22], avgLine[-18])
    cp5 = percentChange(avgLine[-22], avgLine[-17])
    cp6 = percentChange(avgLine[-22], avgLine[-16])
    cp7 = percentChange(avgLine[-22], avgLine[-15])
    cp8 = percentChange(avgLine[-22], avgLine[-14])
    cp9 = percentChange(avgLine[-22], avgLine[-13])
    cp10 = percentChange(avgLine[-22], avgLine[-12])
    cp11 = percentChange(avgLine[-22], avgLine[-11])
    cp12 = percentChange(avgLine[-22], avgLine[-10])
    cp13 = percentChange(avgLine[-22], avgLine[-9])
    cp14 = percentChange(avgLine[-22], avgLine[-8])
    cp15 = percentChange(avgLine[-22], avgLine[-7])
    cp16 = percentChange(avgLine[-22], avgLine[-6])
    cp17 = percentChange(avgLine[-22], avgLine[-5])
    cp18 = percentChange(avgLine[-22], avgLine[-4])
    cp19 = percentChange(avgLine[-22], avgLine[-3])
    cp20 = percentChange(avgLine[-22], avgLine[-2])
    cp21 = percentChange(avgLine[-22], avgLine[-1])
    patForRec.append(cp1)
    patForRec.append(cp2)
    patForRec.append(cp3)
    patForRec.append(cp4)
    patForRec.append(cp5)
    patForRec.append(cp6)
    patForRec.append(cp7)
    patForRec.append(cp8)
    patForRec.append(cp9)
    patForRec.append(cp10)
    patForRec.append(cp11)
    patForRec.append(cp12)
    patForRec.append(cp13)
    patForRec.append(cp14)
    patForRec.append(cp15)
    patForRec.append(cp16)
    patForRec.append(cp17)
    patForRec.append(cp18)
    patForRec.append(cp19)
    patForRec.append(cp20)
    patForRec.append(cp21)

def patternRecognition():
    patFound = 0
    plotPatAr = []
    for eachPattern in patternAr:
        sim1 = 100.00 - abs(percentChange(eachPattern[0], patForRec[0]))
        sim2 = 100.00 - abs(percentChange(eachPattern[1], patForRec[1]))
        sim3 = 100.00 - abs(percentChange(eachPattern[2], patForRec[2]))
        sim4 = 100.00 - abs(percentChange(eachPattern[3], patForRec[3]))
        sim5 = 100.00 - abs(percentChange(eachPattern[4], patForRec[4]))
        sim6 = 100.00 - abs(percentChange(eachPattern[5], patForRec[5]))
        sim7 = 100.00 - abs(percentChange(eachPattern[6], patForRec[6]))
        sim8 = 100.00 - abs(percentChange(eachPattern[7], patForRec[7]))
        sim9 = 100.00 - abs(percentChange(eachPattern[8], patForRec[8]))
        sim10 = 100.00 - abs(percentChange(eachPattern[9], patForRec[9]))
        sim11 = 100.00 - abs(percentChange(eachPattern[10], patForRec[10]))
        sim12 = 100.00 - abs(percentChange(eachPattern[11], patForRec[11]))
        sim13 = 100.00 - abs(percentChange(eachPattern[12], patForRec[12]))
        sim14 = 100.00 - abs(percentChange(eachPattern[13], patForRec[13]))
        sim15 = 100.00 - abs(percentChange(eachPattern[14], patForRec[14]))
        sim16 = 100.00 - abs(percentChange(eachPattern[15], patForRec[15]))
        sim17 = 100.00 - abs(percentChange(eachPattern[16], patForRec[16]))
        sim18 = 100.00 - abs(percentChange(eachPattern[17], patForRec[17]))
        sim19 = 100.00 - abs(percentChange(eachPattern[18], patForRec[18]))
        sim20 = 100.00 - abs(percentChange(eachPattern[19], patForRec[19]))
        sim21 = 100.00 - abs(percentChange(eachPattern[20], patForRec[20]))
        howSim = (sim1+sim2+sim3+sim4+sim5+sim6+sim7+sim8+sim9+sim10+sim11+sim12+sim13+sim14+sim15+sim16+sim17+sim18+sim19+sim20+sim21)/21.00
        if howSim > userPref:
            patFound = 1
            xp = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
            plotPatAr.append(eachPattern)
    if patFound == 1:
        fig = plt.figure(figsize=(10,6))
        for eachPatt in plotPatAr:
            futurePoints = patternAr.index(eachPatt)
            if performanceAr[futurePoints] > patForRec[20]:
                pcolor = '#24bc00'
            else:
                pcolor = '#d40000'
            plt.plot(xp, eachPatt)
            plt.scatter(31, performanceAr[futurePoints], c = pcolor, alpha = 0.25)
        plt.plot(xp, patForRec, '#54fff7', linewidth = 3)
        plt.title('Pattern Recognition')
        plt.grid(True)
        plt.show()

def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter

def graphRawFX():
    fig = plt.figure(figsize=(10,7))
    ax1 = plt.subplot2grid((40,40), (0,0), rowspan=40, colspan=40)
    ax1.plot(date,bid)
    ax1.plot(date,ask)
    plt.gca().get_yaxis().get_major_formatter().set_useOffset(False)
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    ax1_2 = ax1.twinx()
    ax1_2.fill_between(date, 0, (ask-bid), facecolor='g', alpha=.3)
    plt.subplots_adjust(bottom=.23)
    plt.grid(True)
    plt.show()

dataLength = int(bid.shape[0])
print ('The data length is', dataLength)
userPref = float(input('Accuracy '))
toWhat = 37000

while toWhat < dataLength:
    avgLine = ((bid+ask)/2)
    avgLine = avgLine[:toWhat]
    performanceAr = []
    patForRec = []
    patternAr = []
    patternStorage()
    currentPattern()
    patternRecognition()
    totalTime = time.time() - totalStart
    print ('Elapsed time:', round(totalTime, 3), 'Seconds')
    toWhat += 1
