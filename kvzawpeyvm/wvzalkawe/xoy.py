import joblib
import os
import re
import pandas as pd
def sort_(s, n):
    for i in range(1, n):

        temp = s[i]
        # Insert s[j] at its correct position
        j = i - 1

        while j >= 0 and len(s[j]) > len(temp):
            s[j + 1] = s[j]
            j -= 1

        s[j + 1] = temp


#set_verbo = load('ziksionario.map')
try:
    set_verbo = joblib.load('kvzawpeyvm/wvzalkawe/ziksionario.map')
except:
    set_verbo = joblib.load('kaxvkaam/kvzawpeyvm/wvzalkawe/ziksionario.map')

verbo_vy = list(set_verbo.keys())

# sort(verbo_vy,len(verbo_vy))
verbo_vy.reverse()
verbo_regex = []

for verbo in verbo_vy:
    vocales = ['a', 'e', 'i', 'o', 'u', 'v']
    if '(' in verbo:
        meturegexgenon = [a for a in re.split('[()]', verbo) if len(a) > 0]
        if len(meturegexgenon) == 2:
            op1 = meturegexgenon[0]
            if op1[-1] not in vocales:
                op1 += 'v{0,1}'
            op2 = meturegexgenon[0] + meturegexgenon[1]
            if op2[-1] not in vocales:
                op2 += 'v{0,1}'
            verbo = op1 + '|' + op2
        elif len(meturegexgenon) == 3:
            op1 = meturegexgenon[0] + meturegexgenon[2]
            if op1[-1] not in vocales:
                op1 += 'v{0,1}'
            op2 = meturegexgenon[0] + meturegexgenon[1] + meturegexgenon[2]
            if op2[-1] not in vocales:
                op2 += 'v{0,1}'
            verbo = op1 + '|' + op2

    verbo_regex.append(verbo)



slotsIneke = [
    [r'konv{0,1}',r'n{0,1}entu', r'n{0,1}tuku', r'[nñ]{0,1}ma', r'ye'],  # Y canhumil
    [r'v{0,1}m', r'v{0,1}l'],
    [r'tu', r'ka'],
    [r'ni{0,1}e', r'kvn[ou]'],
    [r'u{0,1}w'],
    [r'kiy{0,1}aw', r'[yi]aw', r'kvtiy{0,1}e', r'tiy{0,1}e'],
    [r'v{0,1}l'],
    [r'kvlew', r'kvle', r'meke{0,1}', r'lew', r'le'],
    [r'falvñma', r'falel', r'fal', r'v{0,1}ñma', r'v{0,1}ñmu', r'el'],  # ,r'l{0,1}el'],
    [r'yefal', r'yeñma', r'ye'],
    [r'geye', r'gefal', r'ge', r'u{0,1}w', r'mu'],
    [r'femuw', r'femge', r'rumeñma', r'faluwkvle', r'faluw', r'fem', r'rume', r'kantu'],
    [r'vrwepa', r'evrwepu', r'weye', r'memu', r'mege', r'meye', r'v{0,1}r{0,1}pa', r'v{0,1}r{0,1}p[uo]', r'we', r'me'],
    [r'tu', r'ka'],
    [r'ke|k(?!vnu)',r'pe', r'p', r'wye', r'petu', r'ketu'],
    [r'rk',r'ik',r'vrke',r'ike'],
    [r'la', r'k[ei]l', r'je', r'n[uo]'],
    [r'y{0,1}a', r'fu', r'f', r'fi', r'fil']]

desinenciasInd = [r'v{0,1}n$', r'[yi]{0,1}mi$', r'[yi]$',
                  r'i{0,1}yu$', r'[iy]{0,1}mu$', r'[yi][\s]*egu$|[iy]gu$',
                  r'i{0,1}y{0,1}iñ$', r'[iy]{0,1}mvn$', r'[yi][\s]*egvn$|[iy]gvn$', r'[yi]$']
sort_(desinenciasInd, len(desinenciasInd))
desinenciasInd.reverse()

transicionInd = [r'en$', r'eyu$', r'eymi$', r'eymu$', r'eymvn$',
                 #       		r'w[.*]i{0,1}y{0,1}iñ$',
                 r'fiñ$', r'enew$|eneu$|enu$|eno$', r'eymew$', r'eyew$',
                 r'eyumew$|eyumeu$|eyumu$|eyumo$', r'ey{0,1}iñmew$|ey{0,1}iñmeu$|ey{0,1}iñmu$|ey{0,1}iñmo$',
                 r'eymumew$|eymumeu$|eymumu$|eymumo$', r'eymvnmew$|eymvnmeu$|eymvnmu$|eymvnmo$']
sort_(transicionInd, len(transicionInd))
transicionInd.reverse()

desinenciasCond = [r'li$', r'v{0,1}lmi$', r'le$',
                   r'liyu$', r'v{0,1}lmu$', r'le[\s]*egu$',
                   r'li[y\-]{0,1}iñ$', r'v{0,1}lmvn$', r'le[\s]*egvn$']
sort_(desinenciasCond, len(desinenciasCond))
desinenciasCond.reverse()

transicionCond = [r'eli$', r'eliyu$', r'elmi$', r'elmu$', r'elmvn$',
                  r'w[*]li[y\-]{0,1}iñ$',
                  r'elimew$|elimeu$|elimu$|elimo$', r'eliyumew$|eliyumeu$|eliyumu$|eliyumo$', r'eliyew$',
                  r'eliyumew$|eliyumeu$|eliyumu$|eliyumo]$',
                  r'eliy{0,1}iñmew$|eliy{0,1}iñmeu$|eliy{0,1}iñmu$|eliy{0,1}iñmo$',
                  r'elmumew$|elmumeu$|elmumu$|elmumo$', r'elmvnmew$|elmvnmeu$|elmvnmu$|elmvnmo$']
sort_(transicionCond, len(transicionCond))
transicionCond.reverse()

desinenciasImpe = [r'ci$', r'ge$', r'pe$',
                   r'yu$', r'mu$', r'pe[\s]*egu$'
                                   r'y{0,1}iñ$', r'mvn$', r'pe[\s]*egvn$']
sort_(desinenciasImpe, len(desinenciasImpe))
desinenciasImpe.reverse()

transicionImpe = [r'en$', r'w[*]ai{0,1}y{0,1}iñ$',
                  r'fici$', r'ecimecimew$|ecimeu$|ecimu$|ecimo$', r'eymew$|eymeu$|eymu$|eymo]$',
                  r'eyew$|eyeu$|eyu$|eyo$',
                  r'eyumew$|eyumeu$|eyumu$|eyumo]$', r'ey{0,1}iñmew$|ey{0,1}iñmeu$|ey{0,1}iñmu$|ey{0,1}iñmo$',
                  r'eymumew$|eymumeu$|eymumu$|eymumo]$', r'eymvnmew$|eymvnmeu$|eymvnmu$|eymvnmo$']
sort_(transicionImpe, len(transicionImpe))
transicionImpe.reverse()

otrasDesinencias = [r'y{0,1}[ve]m$', r'm[uo]m$', r'am$', r'lu$', r'el$',
                    r'ae{0,1}l$', r'fiel$', r'fel$', r'[uw]ma$', r'fe$', r'we$',
                    r'wem[uo]m$', r'pey[ve]m$', r'e{0,1}ntu$', r'wen$', r'ci$',
                    r'ke$', r'y{0,1}em$', r'n[ou]$', r'etew|etu|eto$']
sort_(otrasDesinencias, len(otrasDesinencias))
otrasDesinencias.reverse()




import re
class Xoy:


    def __init__(self, idx='f0', regex='', wecun=False,cemkeci=1,inaafeyu_verbo=True, wigkazugun = '',kineupa = True, rakin = 0):
        self.id = idx
        if '^' not in regex:
            regex = '^' + regex
        self.regex = regex
        self.wecun = wecun
        self.cemkeci = cemkeci
        self.inafeyu_verbo = inaafeyu_verbo
        self.wigkazugun = wigkazugun
        self.kineupa = kineupa
        self.rakin = rakin
        
                

    def __str__(self):
        return self.regex

    def __repr__(self):
        return self.regex

    def __eq__(self,kagelu):
        return self.id == kagelu.id and self.regex == kagelu.regex


    def mvli(self,hemvl):
        if re.match(self.regex, hemvl):
            return True
        return False

    def wvzage(self,hemvl):
        mvlewelu = re.sub(self.regex, '', hemvl)
        xoy = re.sub(mvlewelu+'$','',hemvl)
        return xoy, mvlewelu

    
verbo_regex=[Xoy(row[1][0],row[1][1],row[1][2],row[1][3],row[1][4],row[1][5],row[1][6],row[1][7]) for row in pd.read_csv('kvzawpeyvm/wvzalkawe/folil.csv',header=None).iterrows()]
slotsIneke=[

            [Xoy('sI0', 'konv{0,1}', False,1,False, 'entrar/empezar' ,True,1),
             Xoy('sI1', 'n{0,1}entu', False,1,False, 'sacar',True,1),
             Xoy('sI2', 'n{0,1}tuku', False,1,False, 'poner/con',True,1),
             Xoy('sI3', '[nñ]{0,1}ma', False,1,False, 'afectar algo de alguien/algo / "quita"/ que te "caerle algo"',True,1),
             Xoy('sI30', 'ye', False,1,False, 'llevar, constante',True,1),
            ],

            #[#Xoy('sI5', 'v{0,1}m', False,1,False, 'hacerlo a alguien/algo',True,2),
             [Xoy('sI6', 'v{0,1}l', False,1,False,'hacer hacer algo, hacerle algo ',True,2),
            ],

            [Xoy('sI7', 'tu', False,1,False, 'verbalizador, o  (come en caso de comidas, tocar en caso de instrumentos, etc)',True,3),
             Xoy('sI8', 'ka', False,1,False, 'acción que se repite o intensa, sirve para  generar verbos Ej: nütxam a  nütxamkan',True,3),
            ],

            [Xoy('sI9', 'ni{0,1}e', False,1,False, 'tener, también sirve como el "presente o el estar" para verbos que afectan otras personas/cosas',True,4),
            Xoy('sI9', 'n[iy][iy]{0,1}', False,1,False, 'tener, tamién sirve como el "presente o el estar" para verbos que afectan otras personas/cosas',True,4),
             Xoy('sI10', 'kvn[ou]', False,1,False, 'dejar',True,4),
            ],

            [Xoy('sI11', 'u{0,1}w', False,1,False, 'hacer algo a si mismo',True,5),
            ],

            [Xoy('sI12', 'kiy{0,1}aw', False,1,False, 'andar',True,6),
             Xoy('sI12', '[yi]aw', False,1,False, 'andar',True,6),
             Xoy('sI15', 'kvtiy{0,1}e', False,1,False, 'con intensidad o vehemencia',True,6),
             Xoy('sI15', 'tiy{0,1}e', False,1,False, 'con intensidad o vehemencia',True,6),
            ],

            [Xoy('sI6', 'v{0,1}l', False,1,False, 'hacer hacer algo, hacerle algo ',True,7),
            ],

            [Xoy('sI17', 'kvlew', False,1,False, 'quedar',True,8),
             Xoy('sI21', 'kvle', False,1,False, 'estar',True,8),
             Xoy('sI19', 'meke{0,1}', False,1,False, 'estar haciendo algo / ocupado en ',True,8),
             Xoy('sI17', 'lew', False,1,False, 'quedar',True,8),
             Xoy('sI21', 'le', False,1,False, 'estar',True,8),
             Xoy('sI21', 'l(?=[iy][iy]{0,1})', False,1,False, 'estar',True,8),
            ],

            [Xoy('sI22', 'falvñma', False,1,False, 'encargo o deber en hablando de un objeto de alguien',True,9),
             Xoy('sI23', 'falel', False,1,False, 'se considera en un deber peroen beneficio de alguien*',True,9),
             Xoy('sI24', 'fal', False,1,False, 'deber de hacer algo| encargar | simular ',True,9),
             Xoy('sI25', 'v{0,1}ñma', False,1,False, 'afectar algo de alguien/algo / "quita"/ que te "caerle algo"',True,9),
             Xoy('sI26', 'v{0,1}ñmu', False,1,False, 'hacer aglo en beneficio propio',True,9),
             Xoy('sI27', 'el', False,1,False, 'agrega una persona al verbo "en su beneficio"',True,9),
            ],

            [
             Xoy('sI75', 'yekvme', False,1,False, 'ir haciendo la acción',True,10),
             Xoy('sI76', 'yekvpa', False,1,False, 'venir haciendo',True,10),
             #Xoy('sI28', 'yefal', False,1,False, '<*metuno*>',True,10),
             #Xoy('sI29', 'yeñma', False,1,False, '<*metuno*>',True,10),
             Xoy('sI30', 'ye', False,1,False, 'llevar, constante',True,10),
            ],

            [#Xoy('sI31', 'geye', False,1,False, '<*metuno*>',True,11),
             #Xoy('sI32', 'gefal', False,1,False, '<*metuno*>',True,11),
             Xoy('sI33', 'ge', False,1,False, 'la acción es sobre la persona del verbo "me dijeron" "te escucharon" ',True,11),
             Xoy('sI33', 'g(?=[iy][iy]{0,1})', False,1,False, 'la acción es sobre la persona del verbo "me dijeron" "te escucharon" ',True,11),
             Xoy('sI11', 'u{0,1}w', False,1,False, 'hacerse algo a si mismo, transformarse en algo',True,11),
             Xoy('sI35', 'm[uo]', False,1,False, 'acciones de tu o uds a nosotros o yo [la terminación indica sobre quien es la acción]',True,11),
            ],

            [Xoy('sI36', 'femuw', False,1,False, '<*metuno*>',True,12),
             Xoy('sI37', 'femge', False,1,False, '<*metuno*>',True,12),
             Xoy('sI38', 'rumeñma', False,1,False, '<*metuno*>',True,12),
             Xoy('sI39', 'faluwkvle', False,1,False, '<*metuno*>',True,12),
             Xoy('sI40', 'faluw', False,1,False, 'fingirse',True,12),
             Xoy('sI41', 'fem', False,1,False, 'hacer la acción rapido',True,12),
             Xoy('sI42', 'rume', False,1,False, 'acción repentina',True,12),
             Xoy('sI43', 'kantu', False,1,False, 'de mentira / de practica',True,12),
            ],

            [#Xoy('sI44', 'vrwepa', False,1,False, '<*metuno*>',True,13),
             #Xoy('sI45', 'vrwepu', False,1,False, '<*metuno*>',True,13),
             #Xoy('sI46', 'weye', False,1,False, '<*metuno*>',True,13),
             #Xoy('sI47', 'memu', False,1,False, '<*metuno*>',True,13),
             #Xoy('sI48', 'mege', False,1,False, '<*metuno*>',True,13),
             #Xoy('sI49', 'meye', False,1,False, '<*metuno*>',True,13),
             Xoy('sI77', 'v{0,1}[ir]pa', False,1,False, 'accion mientras se viene',True,13),
             Xoy('sI50', 'pa', False,1,False, 'venir o llegar a hacer algo ',True,13),
             Xoy('sI78', 'v{0,1}rp[uo]', False,1,False, 'acción mientras se llega a cierto punto',True,13),
             Xoy('sI51', 'p[uo]', False,1,False, 'llegar a hacer algo ',True,13),
             Xoy('sI52', 'we', False,1,False, 'indica lo que queda. Si se niega en la misma palabra indica "ya no"',True,13),
             Xoy('sI53', 'me', False,1,False, 'ir a hacer la acción',True,13),
            ],

            [Xoy('sI7', 'tu', False,1,False, 'verbalizador, o  (come en caso de comidas, tocar en caso de instrumentos, etc), puede indicar cambios',True,14),
             Xoy('sI8', 'ka', False,1,False, 'acción que se repite o intensa, sirve para  generar verbos  Ej: nütxam a  nütxamkan',True,14),
            ],

            [Xoy('sI56', 'ke', False,1,False, 'habitualmente',True,15),
             Xoy('sI56', 'k(?=[iy])', False,1,False, 'habitualmente',True,15),
             Xoy('sI57', 'pe', False,1,False, '"pasado" habia, hace poco, está',True,15),
             Xoy('sI58', 'p(?=[iy])', False,1,False, '"pasado" habia, hace poco, está',True,15),
             Xoy('sI59', 'wye', False,1,False, 'indica que algo ya se hizo',True,15),
             Xoy('sI60', 'petu', False,1,False, '"pasado no tan pasado," habia, hace poco, está (indicando un cambio)',True,15),
             Xoy('sI61', 'ketu', False,1,False, 'habitual "nuevo hábito"',True,15),
            ],

            [Xoy('sI62', 'rk(?=[iy])', False,1,False, 'para hablar con sorpresa del asunto, o como diciendo "dicen que"(porque no es testigo directo o lo sabe 100%)',True,16),
             Xoy('sI63', 'ik(?=[iy])', False,1,False,  'para hablar con sorpresa del asunto, o como diciendo "dicen que"(porque no es testigo directo o lo sabe 100%)',True,16),
             Xoy('sI64', 'v{0,1}rke', False,1,False,  'para hablar con sorpresa del asunto, o como diciendo "dicen que"(porque no es testigo directo o lo sabe 100%)',True,16),
             Xoy('sI65', 'ike', False,1,False,  'para hablar con sorpresa del asunto, o como diciendo "dicen que"(porque no es testigo directo o lo sabe 100%)',True,16),
            ],

            [Xoy('sI66', 'la', False,3,False, 'negación modo "normal"(indicativo)',True,17),
             Xoy('sI67', 'k[ei]l', False,4,False, 'negación modo "órdenes"(imperativo) o también mezclado con condicional (si es que)',True,17),
             Xoy('sI68', 'je', False,1,False, 'indica mucha seguridad en lo que se dice',True,17),
             Xoy('sI69', 'n[uo]', False,2,False, 'negación para lo condicional y otros modos (el, ael, etew,etc), ',True,17),
            ],

            [Xoy('sI70', 'y{0,1}a', False,1,False, 'futuro',True,18),
             Xoy('sI71', 'fu', False,1,False, 'pasado, o algo que ya no sigue siendo válido ahora',True,18),
             Xoy('sI72', 'f(?=[e])', False,1,False, 'pasado, o algo que ya no sigue siendo válido ahora (Viene de FU)',True,18),
             Xoy('sI73', 'fi', False,1,False, 'indica un objeto al que se le hace la acción (Lo, La, Le)[si es terminación indica que lo hace una 3ra persona( el/ella "lo"))]',True,18),
	         Xoy('sI79', 'kifil', False,4,False,'negación en modo "órdenes" (imperativo) con el FI incluido',True,18),
            ],
]
desinenciasInd=[
Xoy('dI0', '[yi][\s]+egvn$', True,3,False, 'ellxs (mas de 2 personas) ',True,100),
Xoy('dI0', '[iy]gvn$', True,3,False, 'ellxs (mas de 2 personas) ',True,100),
Xoy('dI1', '[yi][\s]+egu$|[iy]gu$', True,3,False, 'ellxs ( 2  personas)',True,100),
Xoy('dI1', '[iy]gu$', True,3,False, 'ellxs ( 2  personas)',True,100),
Xoy('dI2', 'i{0,1}y{0,1}iñ$', True,3,False, 'Nosotros (mas de 2 personas)',True,100),
Xoy('dI3', '[iy]mvn$', True,3,False, 'Ustedes (mas de 2 personas)',True,100),
Xoy('dI4', '[iy]mu$', True,3,False, 'Ustedes (2 personas)',True,100),
Xoy('dI5', '[yi]mi$', True,3,False, 'Tú',True,100),
Xoy('dI6', 'i{0,1}yu$', True,3,False, 'Nosotros (2 personas)',True,100),
Xoy('dI7', 'v{0,1}n$', True,3,False, 'Yo',True,100),
Xoy('dI8', '[yi]$', True,3,False, 'El/Ella  ',True,100),
]
transicionInd=[
Xoy('tI0', 'ey{0,1}iñmew$|ey{0,1}iñmeu$|ey{0,1}iñmu$|ey{0,1}iñmo$', True,3,False, 'de el/ella/ellxs a nosotros mas de 2 "nos"',True,100),
Xoy('tI1', 'eymvnmew$|eymvnmeu$|eymvnmu$|eymvnmo$', True,3,False, 'de el/ella/ellxs a ustedes mas de 2 "les"',True,100),
Xoy('tI2', 'eymumew$|eymumeu$|eymumu$|eymumo$', True,3,False, 'de el/ella/ellxs a ustedes 2 "les" ',True,100),
Xoy('tI3', 'eyumew$|eyumeu$|eyumu$|eyumo$', True,3,False, 'de el/ella/ellxs a nosotros 2 "nos" ',True,100),
Xoy('tI4', 'enew$|eneu$|enu$|eno$', True,3,False, 'de el/ella/ellxs a mi "me" ',True,100),
Xoy('tI5', 'eymew$|eymu$|eymo$', True,3,False, 'de el/ella/ellxs a ti "te"',True,100),
Xoy('tI6', 'eymvn$', True,3,False, 'a ustedes "les"',True,100),
Xoy('tI7', 'eyew$|eyu$|eyo$', True,3,False, 'de el/ella/ellxs a el/ella/ellxs "les"',True,100),
Xoy('tI8', 'eymu$', True,3,False, 'a ustedes 2 "les"',True,100),
Xoy('tI9', 'eymi$', True,3,False, 'a ti "te"',True,100),
Xoy('tI10', 'fiñ$', True,3,False, 'de yo a el/ella/ellxs "les"',True,100),
Xoy('tI15', 'fimu$', True,3,False, 'de Ustedes 2  a el/ella/ellxs "les"',True,100),
Xoy('tI13', 'fimi$', True,3,False, 'de Tú a el/ella/ellxs "les"',True,100),
Xoy('tI14', 'fimvn$', True,3,False, 'de Ustedes a el/ella/ellxs "les"',True,100),
Xoy('tI11', 'eyu$', True,3,False, 'yo a ti "te" ',True,100),
Xoy('tI12', 'en$', True,3,False, 'tu a mi "me"[también se podría entender como una orden]',True,100),
]
desinenciasCond=[
Xoy('dC0', 'li[y\-]{0,1}iñ$', True,2,False, 'Si/cuando(futuro) nosotros mas de 2 ...',True,100),
Xoy('dC1', 'le[\s]*egvn$', True,2,False, 'Si/cuando(futuro) ellxs mas de 2 ...',True,100),
Xoy('dC2', 'v{0,1}lmvn$', True,2,False, 'Si/cuando(futuro) ustedes mas de 2',True,100),
Xoy('dC3', 'le[\s]*egu$', True,2,False, 'Si/cuando(futuro) ellxs 2',True,100),
Xoy('dC4', 'v{0,1}lmu$', True,2,False, 'Si/cuando(futuro) ustedes 2',True,100),
Xoy('dC5', 'v{0,1}lmi$', True,2,False, 'Si/cuando(futuro) tu ',True,100),
Xoy('dC6', 'liyu$', True,2,False, 'Si/cuando(futuro) nosotros 2',True,100),
Xoy('dC7', 'le$', True,2,False, 'Si/cuando(futuro) el/ella',True,100),
Xoy('dC8', 'li$', True,2,False, 'si yo',True,100),
]
transicionCond=[
Xoy('tI0', 'eliy{0,1}iñmew$|eliy{0,1}iñmeu$|eliy{0,1}iñmu$|eliy{0,1}iñmo$', True,2,False,  'de el/ella/ellxs a nosotros mas de 2 "si nos"',True,100),
Xoy('tI1', 'eliyumew$|eliyumeu$|eliyumu$|eliyumo]$', True,2,False, 'de el/ella/ellxs a nosotros 2 "si nos"',True,100),
Xoy('tI2', 'elmvnmew$|elmvnmeu$|elmvnmu$|elmvnmo$', True,2,False, 'de el/ella/ellxs a uds mas de 2 "si les"',True,100),
Xoy('tI3', 'eliyumew$|eliyumeu$|eliyumu$|eliyumo$', True,2,False, 'de el/ella/ellxs a nosotros 2 "si nos"',True,100),
Xoy('tI4', 'elmumew$|elmumeu$|elmumu$|elmumo$', True,2,False, 'de el/ella/ellxs a ustedes 2 "si les"',True,100),
Xoy('tI5', 'elimew$|elimeu$|elimu$|elimo$', True,2,False, 'de el/ella/ellxs a mi 2 "si me"',True,100),
Xoy('tI13','elmew$|elmeu$|elmu$|elmo$', True,2,False, 'de el/ella/ellxs a mi 2 "si te"',True,100),
Xoy('tI7', 'eliyew$|eliyu$', True,2,False, 'de el/ella/ellxs a  el/ella/ellxs "si les"',True,100),
Xoy('tI8', 'elmvn$', True,2,False, 'a ustedes mas de 2 "si les" ',True,100),
Xoy('tI9', 'eliyu$', True,2,False, 'si yo a ti "si yo te"',True,100),
Xoy('tI10', 'elmu$', True,2,False, 'a ustedes 2',True,100),
Xoy('tI11', 'elmi$', True,2,False, 'a ti "si te" ',True,100),
Xoy('tI12', 'eli$', True,2,False, 'tu a mi "si me"',True,100),
]
desinenciasImpe=[
Xoy('di0', 'pe[\s]*egu$', True,4,False, ' que ellxs 2 hagan',True,100),
Xoy('di1', 'pe[\s]*egvn$', True,4,False, 'que ellxs hagan',True,100),
Xoy('di2', 'mvn$', True,4,False, 'que ustedes hagan',True,100),
Xoy('di3', 'mu$', True,4,False, ' que ustedes 2 hagan',True,100),
Xoy('di4', 'yu$', True,4,False, 'que nosostros 2 hagamos',True,100),
Xoy('di8', 'yiñ$', True,4,False, 'que nosostros hagamos',True,100),
Xoy('di5', 'pe$', True,4,False, 'que el/ella haga ',True,100),
Xoy('di6', 'ge$', True,4,False, 'tu hazlo ',True,100),
Xoy('di7', 'ci$', True,4,False, 'que yo haga',True,100),
]
transicionImpe=[
#Xoy('ti0', 'ey{0,1}iñmew$|ey{0,1}iñmeu$|ey{0,1}iñmu$|ey{0,1}iñmo$', True,2,False, 'de el/ella/ellxs a nosotros "orden"',True,100),
Xoy('ti1', 'emvnmew$|emvnmeu$|emvnmu$|emvnmo$', True,4,False, 'de el/ella/ellxs a ustedes "orden"',True,100),
Xoy('ti2', 'emumew$|emumeu$|emumu$|emumo]$', True,4,False, 'de  el/ella/ellxs a ustedes 2 "orden"',True,100),
Xoy('ti3', 'ecimecimew$|ecimeu$|ecimu$|ecimo$', True,4,False, 'de el/ella/ellxs a yo "orden"',True,100),
Xoy('ti8', 'fici$', True,4,False, 'de yo a el/ella/ellxs "orden"',True,100),
Xoy('ti4', 'fe$', True,4,False, '"hazlo a el/ella/es@"  "orden"',True,100),
]
otrasDesinencias=[
Xoy('dO0', 'etew|etu|eto$', True,2,False, 'se refiere a lo que hicieron o quien lo hizo (3ras personas a cualquiera; se usa con posesivos para ser más claro, con futuro se puede hablar de propósito) ',True,100),
Xoy('dO1', 'y{0,1}[ve]m$', True,2,False, 'sirve para hablar de "cada vez que"',True,100),
Xoy('dO2', 'e{0,1}ntu$', True,2,False, 'sirve para hacer conjuntos de cosas',True,100),
Xoy('dO3', 'y{0,1}em$', True,2,False, 'puede servir para expresar algo que ya no corre',True,100),
Xoy('dO4', 'pey[ve]m$', True,2,False, 'Herramienta o lugar para hacer una acción',True,100),
Xoy('dO5', 'wem[uo]m$', True,2,False, 'con números expresa cantida de días hacia atrás',True,100),
Xoy('dO6', 'y{0,1}al$', True,2,False, 'sirve para expresar propósito o una acción sin conjugar',True,100),
Xoy('dO7', '[uw]ma$', True,2,False, 'indica una persona o cosa que ya hizo la acción del verbo',True,100),
Xoy('dO8', 'm[uo]m$', True,2,False, 'forma sustantivo que indica que un hecho ya ha sucedido',True,100),
#Xoy('dO9', 'n[ou]$', True,2,False, 'niega lo anterior, generalmente puede ser con sustantivos',True,100),
Xoy('dO10', 'fiel$', True,2,False, 'sirve para las transiciones indica una acción hecha sobre otrx(s)',True,100),
Xoy('dO11', 'wen$', True,2,False, 'sirve para expresar relaciones entre personas ',True,100),
Xoy('dO12', 'fel$', True,2,False, 'puede servir para expresar un deseo. también acción en el pasado',True,100),
Xoy('dO13', 'ke$', True,2,False, 'con adjetivos "pluraliza"',True,100),
Xoy('dO14', 'ci$', True,2,False, 'sirve para hacer adjetivos',True,100),
Xoy('dO15', 'we$', True,2,False, 'Herramienta o lugar para hacer una acción o donde resalta un elemento',True,100),
Xoy('dO16', 'fe$', True,2,False, 'alguien que suele hacer esta acción como oficio por ejemplo',True,100),
Xoy('dO17', 'el$', True,2,False, 'expresa acciones o resultados de esta en el pasado',True,100),
Xoy('dO18', 'lu$', True,2,False, 'se puede referir a una persona o a una característica de esta, también sirve para decir "cuando"',True,100),
Xoy('dO19', 'am$', True,2,False, 'sirve para expresar propósito',True,100),
Xoy('dO20', 'v{0,1}n$', True,2,False, 'verbo sin conjugar',True,100),

]
sustantivosAdjetivos =[
]


