import json
from js import localStorage, document, console, XMLHttpRequest
import os
# import openai


# localStorage.setItem("openAI", "")
# bearer = "Bearer " + localStorage.getItem("openAI")
bearer = "Bearer " + os.getenv("OPENAI_API_KEY")

# print(bearer)
promptDiv = document.getElementById("prompt")
prompt="A neutron star is the collapsed core of a massive supergiant star, which had a total mass of between 10 and 25 solar masses, possibly more if the star was especially metal-rich.[1] Neutron stars are the smallest and densest stellar objects, excluding black holes and hypothetical white holes, quark stars, and strange stars.[2] Neutron stars have a radius on the order of 10 kilometres (6.2 mi) and a mass of about 1.4 solar masses.[3] They result from the supernova explosion of a massive star, combined with gravitational collapse, that compresses the core past white dwarf star density to that of atomic nuclei.\n\nTl;dr"
promptDiv.innerHTML = "<h3>Prompt: </h3>\"" + prompt + "\"<hr/>"

# for best results (at a cost of $.02 per 1k tokens), use text-davinci-003
# for quickest and cheapest results ($.0004 per 1k tokens), use text-ada-001
engine = "text-davinci-003"

xhr = XMLHttpRequest.new()
xhr.open("POST", "https://api.openai.com/v1/completions", False)
xhr.setRequestHeader("Content-Type", "application/json")
xhr.setRequestHeader("Authorization", bearer)

data = json.dumps({
    "model": "text-davinci-003",
    "prompt": prompt,
    "max_tokens": 100,
    "temperature": 0.7,
    "top_p": 1,
    "frequency_penalty": 1.2,
    "presence_penalty": 1
})

# response = openai.Completion.create(    
#   model="text-davinci-003",
#   prompt="A neutron star is the collapsed core of a massive supergiant star, which had a total mass of between 10 and 25 solar masses, possibly more if the star was especially metal-rich.[1] Neutron stars are the smallest and densest stellar objects, excluding black holes and hypothetical white holes, quark stars, and strange stars.[2] Neutron stars have a radius on the order of 10 kilometres (6.2 mi) and a mass of about 1.4 solar masses.[3] They result from the supernova explosion of a massive star, combined with gravitational collapse, that compresses the core past white dwarf star density to that of atomic nuclei.\n\nTl;dr",
#   temperature=0.7,
#   max_tokens=60,
#   top_p=1.0,
#   frequency_penalty=0.0,
#   presence_penalty=1
# )

# print('Summarized Response: ', response["choices"][0]["text"])

xhr.send(data)

json_response = json.loads(xhr.response)
completion_text = json_response["choices"][0]["text"]
# console.log("Colors: " + completion_text)

completionDiv = document.getElementById("completion")
completionDiv.innerHTML = "<h3>OpenAI (" + engine + ") Summarized Response : </h3>\"" + completion_text.strip() + "\""