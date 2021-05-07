from chatterbot import ChatBot
import discord
import re
from unicodedata import normalize
llave="ODIxMDg4OTA0MjQ0NjI1NDI2.YE-ooQ.sYFVkZZoFTCxtb1XMKkPNN7RZHY"
chatbot=ChatBot('JP', read_only=True,
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    input_adapter="chatterbot.input.VariableInputTypeAdapter",
    output_adapter="chatterbot.output.OutputAdapter",
    output_format="text",
    database_uri='sqlite:///JP_db.db',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response':'Lo siento, eso está fuera de mi enfoque. Pero puedes preguntarme algo sobre el coronavirus.',
            'maximum_similarity_treshold':0.999999,
            #'statement_comparison_function':'chatterbot.comparisons.SynsetDistance'
        },
    ]#,
    #preprocessors=[
    #    'chatterbot.preprocessors.convert_to_ascii'
    #]
)
#try:
def BotJP():
    global llave
    cliente=discord.Client()
    @cliente.event
    async def on_message(mensaje):
    #texto = str(input("query: "))
        if(mensaje.author == cliente.user):
            return
        texto=mensaje.content
        texto=re.sub(r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", normalize( "NFD", texto), 0, re.I)
        texto= normalize( 'NFC', texto)
        texto=texto.lower()
        respuesta_bot = chatbot.get_response(texto)
    #print("BOT:"+str(respuesta_bot))
        await mensaje.channel.send(respuesta_bot)
    cliente.run(llave)
#except KeyboardInterrupt:
#   pass
BotJP()

