# import asyncio
# import edge_tts


# async def speak(text):
#     communicate = edge_tts.Communicate(text, voice="de-DE-KatjaNeural")
#     await communicate.save("output_2.mp3")

text = """Hallo und herzlich willkommen. Dies ist ein Testtext zur Überprüfung der Sprachsynthese. 
Achte auf die Betonung, die Aussprache und den natürlichen Sprachfluss. Zahlen wie eins, zwei, drei 
sollten klar verständlich sein. Auch schwierige Wörter wie ‚Sprachsynthesekomponente‘ oder 
‚Entwicklungsperspektiven‘ werden jetzt getestet. Zum Schluss folgt ein kurzer Satz mit 
emotionaler Betonung: Ich freue mich sehr, dass du heute hier bist!"""

# asyncio.run(speak(text))


from gtts import gTTS

tts = gTTS(text=text, lang='de')
tts.save("output.mp3")
