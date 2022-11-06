import os
import sys
import openai
import random

# Load your API key from an environment variable or secret management service

def main():
    setup()
    imagePrompts = cleanInput()

    links = generateResponse(imagePrompts)
    for x in range(len(links)):
        print(links[x])
    return

def cleanInput():
    parameterList = []
    campingRelatedTerms = ["tents ", "bonfire ", "marshmellows ", "camp ", "woods ", "camping ", "hiking "]
    for x in range(len(sys.argv)):
        if(x==0):
            continue
        else:
            parameterList.append(random.choice(campingRelatedTerms)+sys.argv[x])
    return parameterList


def setup():
    api_key="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"
    openai.api_key = api_key
    return


def generateResponse(s):
    returnLinks = []
    while len(returnLinks)!=len(s):

        for x in range(len(s)):
            response = openai.Image.create(
                prompt=s[x],
                n=1,
                size="1024x1024"
            )
            returnLinks.append(response['data'][0]['url'])
    return returnLinks


if __name__=="__main__":
    main()