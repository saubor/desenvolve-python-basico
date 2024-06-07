import datetime


agora = datetime.datetime.now()


data_formatada = agora.strftime("Data: %d/%m/%Y")
hora_formatada = agora.strftime("Hora: %H:%M")

print(data_formatada)
print(hora_formatada)
