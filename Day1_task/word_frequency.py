def word_frequency(sentence):
    words=sentence.lower().split()
    frequency={}

    for word in words:
        if word in frequency:
            frequency[word]+=1
        else:
            frequency[word]=1
    return frequency
    
sentence="Anshula is a student of B.Tech and B.Tech is a 4 year Graduation degree"
result=word_frequency(sentence)

sorted_result=dict(
    sorted(result.items(), key=lambda item: item[1], reverse=True)
)

print(sorted_result)