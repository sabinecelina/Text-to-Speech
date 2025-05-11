# Text-to-Speech

## Text to Speech with Python

I wanted to create a natural text-to-speech system using Python. My goal was to generate lifelike speech output that sounds as close to a human voice as possible. To achieve this, I explored various libraries such as gTTS, pyttsx3, and Microsoft's azure-cognitiveservices-speech. Among these, the Azure Speech SDK provided the most natural-sounding results, especially when using neural voices like "en-US-AriaNeural" or "de-DE-KatjaNeural" for a german voice.

In the following example, I demonstrate how to generate speech using the Azure Speech SDK in Python.
```python
import asyncio
import edge_tts


async def speak(text):
    communicate = edge_tts.Communicate(text, voice="de-DE-KatjaNeural")
    await communicate.save("output_edge_ttes.mp3")

text = """Hallo und herzlich willkommen. Dies ist ein Testtext zur Überprüfung der Sprachsynthese. 
Achte auf die Betonung, die Aussprache und den natürlichen Sprachfluss. Zahlen wie eins, zwei, drei 
sollten klar verständlich sein. Auch schwierige Wörter wie ‚Sprachsynthesekomponente‘ oder 
‚Entwicklungsperspektiven‘ werden jetzt getestet. Zum Schluss folgt ein kurzer Satz mit 
emotionaler Betonung: Ich freue mich sehr, dass du heute hier bist!"""

asyncio.run(speak(text))
```
