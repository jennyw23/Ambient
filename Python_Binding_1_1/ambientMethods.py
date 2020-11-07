# Boston TechTogether Hackathon 2020

# "Ambient" project: Eco-friendly application that crowdsources temperature preferences 
# across individuals in a building to adjust the ambient temperature based on group sentiment.

import wap

server = 'http://api.wolframalpha.com/v2/query.jsp'
appid = '26GLXH-Y5WJW8A96R'


def displayInput(input):
    return 'derivative of square root of {} = 0'.format(input)

def createEquation(arr):
    resultString = ''
    count = 0
    for input in arr:
        resultString += '(x-{})^2'.format(input)
        if count != len(arr)-1:
            resultString += " + "
        count += 1
    return resultString

def displaySolution(input): 
    waeo = wap.WolframAlphaEngine(appid, server)
    answerText = 'Incorrect array input'
    queryStr = waeo.CreateQuery(input)
    wap.WolframAlphaQuery(queryStr, appid)
    result = waeo.PerformQuery(queryStr)
    result = wap.WolframAlphaQueryResult(result)
    for pod in result.Pods():
        waPod = wap.Pod(pod)
        title = "Pod.title: " + waPod.Title()[0]
        if waPod.Title()[0] == 'Solution':
            # print title
            for subpod in waPod.Subpods():
                waSubpod = wap.Subpod(subpod)
                plaintext = waSubpod.Plaintext()[0]
                img = waSubpod.Img()
                src = wap.scanbranches(img[0], 'src')[0]
                alt = wap.scanbranches(img[0], 'alt')[0]
                # print "-------------"
                # print "img.src: " + src
                # print "img.alt: " + alt
    try:
        answerText = alt[3:]
        return answerText
    except:
        return answerText
