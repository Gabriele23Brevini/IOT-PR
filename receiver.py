
from machine import Pin
from ir_rx import NEC_16

# Libreria che contiene le implementazioni per la ricezione del segnale Ir:

ir_key = {
    0x45: 'POWER',
    0x46: 'MODE',
    0x47: 'MUTE',
    0x44: 'PLAY',
    0x40: 'PREV',
    0x43: 'NEXT',
    0x07: 'EQ',
    0x15: 'MINUS',
    0x09: 'PLUS',
    0x16: '0',
    0x19: 'REPEAT',
    0x0D: 'USD',
    0x0C: '1',
    0x18: '2',
    0x5E: '3',
    0x08: '4',
    0x1C: '5',
    0x5A: '6',
    0x42: '7',
    0x52: '8',
    0x4A: '9'    
    }



# La funzione di seguito chiamata "callback" prende tre argomenti:
        # 1) data: Rappresenta il dato associato al segnale infrarosso ricevuto. Nel contesto del protocollo NEC_16, questo dato è un valore specifico che identifica il pulsante premuto sul telecomando
        # 2) addr: Rappresenta l'indirizzo associato al segnale infrarosso ricevuto. Nel protocollo NEC, questo valore è spesso utilizzato per distinguere diversi dispositivi.
        # 3) ctrl: Rappresenta il byte di controllo associato al segnale infrarosso ricevuto. Questo byte può contenere informazioni aggiuntive sul segnale, ad esempio se è un segnale di ripetizione.

def callback(data, addr, ctrl):
    if data > 0:  # NEC protocol sends repeat codes.
        # Nota bene: con data>0 riesco a non gestire i codici di ripetizione, che altrimente verrebbero girati per esempio tenendo premuto un tasto (cosa che non voglio).
        
        # print('Data {:02x} Addr {:04x}'.format(data, addr))
        
        print(ir_key[data])
        # Alla fine, ottengo quello che voglio: stampare la stringa che è associata al codice Ir che viene ricevuto.

ir = NEC_16(Pin(23, Pin.IN), callback)
# Ir fa questo: crea un oggetto (NEC_16) a cui vengono passati due argomenti. il primo è un oggetto (Pin(23, Pin.IN); il secondo è una funzione (callback)
# Questo indica che il ricevitore IR è collegato al pin 23 e deve chiamare la funzione callback quando riceve un segnale IR valido.
