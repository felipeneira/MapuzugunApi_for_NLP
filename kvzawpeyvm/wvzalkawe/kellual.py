from kvzawpeyvm.rulpawirintukuwe.KimamWirintukun import chuchiWirintukun, zulliafiel_rulpawirintukuwe 
from kvzawpeyvm.wvzalkawe.koyam import Koyam
from kvzawpeyvm.rulpawirintukuwe.Reglas import reglas12, reglas13, reglas21, reglas23, reglas31, reglas32
from kvzawpeyvm.wvzalkawe.xoy import Xoy
import re

def rupaka(txt):
    return(txt)

wirintukunVy = {
                'a0'  : ('Azümchefe',            lambda w:reglas23.rulpawe(w)),
                'r0'  : ('Ragileo',              lambda w:rupaka(w)),
                'u0'  : ('Unificado',            lambda w:reglas21.rulpawe(w)),
                'av1' : ('Azümchefe + Tx -> Tr', lambda w:re.sub('tx','tr',reglas23.rulpawe(w))),
                'av2' : ('Azümchefe + G  -> Ng', lambda w:re.sub('g','ng',reglas23.rulpawe(w))),
                'rv1' : ('Ragileo + C -> Ch',    lambda w:re.sub('c','ch',w)),
                'rv2' : ('Ragileo + V -> Ü',     lambda w:re.sub('v','ü',w)),
                'rv3' : ('Ragileo + Z -> D',     lambda w:re.sub('z','d',w)),
                'uv1' : ('Unificado + D -> Z',   lambda w:re.sub('d','z',reglas21.rulpawe(w))),
                'uv2' : ('Unificado + Tr -> Tx', lambda w:re.sub('tr','tx',reglas21.rulpawe(w)))
}
# -> PARA TXOKIN

def kintuxokin(koyam,n=0,a=''):

## [0] FUTURO + FU => HIPOTETICO
    if koyam.xoy.id == "sI70":
        # Este nivel es Futuro        
        for row in koyam.kom_row:
            kr = kintuxokin(row,n+1,a='a')
            if kr[1] and kr[2]==1:
                wk=Koyam(row.hemvl, rakin_row=row.rakin_row, xoys='afu', r_xoy=row.r_xoy, wecun_amci=False, folil_amci=False, chumte=row.chumte,
                 tvfacihemvl=('', ''), chaw=koyam, xoy=Xoy('sI71*', 'afu', False,1,False, 'hipotético',True,18))
                wk.kom_row=kr[0]
                koyam = wk

            if kr[1] and kr[2]==2:
                wk=Koyam(row.hemvl, rakin_row=row.rakin_row, xoys='af', r_xoy=row.r_xoy, wecun_amci=False, folil_amci=False, chumte=row.chumte,
                 tvfacihemvl=('', ''), chaw=koyam, xoy=Xoy('sI72*', 'af', False,1,False, 'hipotético',True,18))
                wk.kom_row=kr[0]
                koyam = wk

            if kr[1] and kr[2]==3:
                wk=Koyam(row.hemvl, rakin_row=row.rakin_row, xoys='ael', r_xoy=row.r_xoy, wecun_amci=False, folil_amci=False, chumte=row.chumte,
                 tvfacihemvl=('', ''), chaw=koyam, xoy=Xoy('d017*', 'ael', False,2,False, 'sirve para expresar propósito o la acción sin conjugar',True,100))
                wk.kom_row=kr[0]
                koyam = wk
        return koyam,False,5
 
    
    if koyam.xoy.id == "sI71" and a=='a': #A +FU 
        return koyam.kom_row,True,1

    if koyam.xoy.id == "sI72" and a=='a': #A + F 
        return koyam.kom_row,True,2

    if koyam.xoy.id == "dO17" and a=='a': #A + el 
        return koyam.kom_row,True,3
##### [0] #####

## [1] PE + LA
    if koyam.xoy.id == "sI57":
        # Este nivel es PE
        for row in koyam.kom_row:
            kr = kintuxokin(row,n+1,a="pe")
            if kr[1] and kr[2]==1:
                wk=Koyam(row.hemvl, rakin_row=row.rakin_row, xoys='pela', r_xoy=row.r_xoy, wecun_amci=False, folil_amci=False, chumte=row.chumte,
                 tvfacihemvl=('', ''), chaw=koyam, xoy=Xoy('sI71*', 'pela', False,1,False, 'expresión que afirma lo que se dice pero con un poco de duda /Otra opcion es que sea algo que "no pasó hace poco"',True,18))
                wk.kom_row=kr[0]
                koyam = wk

        return koyam,False,5
 
    
    if koyam.xoy.id == "sI66" and a=="pe": #PE + LA
        return koyam.kom_row,True,1

##### [1] #####


    for row in koyam.kom_row:
        kr =kintuxokin(row,n+1)
        if kr[2]==5:
            koyam.setkomrow(kr[0],row)
    return koyam,None,None


def pepikaam_hemvl(hemvla, mvlica=True): 
    hemvla=[hemvl.strip().lower() for hemvl in hemvla.split()]
    for hemvl in hemvla:
        xipaalu = dict()
        wirintukun= chuchiWirintukun(hemvl)
        Nm=0
        koyam=None
        wirina=()
        for wirin in wirintukun:
            kkoyam = Koyam(wirin[1].lower())
            kkoyam.zewmakoyamvn()
            if Nm<len(kkoyam.kom_row):
                Nm=len(kkoyam.kom_row)
                koyam = kkoyam
                wirina = wirin
        
        if mvlica and len(wirintukun)>0 and type(koyam)!= type(None) and Nm>0:
            xipaalu['vy'] = hemvl
            xipaalu['wirintukun'] = wirintukunVy[wirina[0]][0]
            rr = len(koyam.kom_row)
            
            while True:
                koyam.kaxvrowvn()
                if rr == len(koyam.kom_row):
                    break
                else:
                    rr = len(koyam.kom_row)
            
           
            koyam = kintuxokin(koyam,0)[0]            
            hemvlkawe = koyam.wirintuku_hemvl2()
            hemvlkawe =  [wirintukunVy[wirina[0]][1](h) for h in hemvlkawe]
            hemvlkawew = [h.split('-')[1:] for h in hemvlkawe]
            regexkawe = koyam.wirintuku_regex()
            wzkawe = koyam.wirintuku_wz()
            wzkawe = [h.split('-')[1:] for h in wzkawe]
            aux = []
            aux2 = []
            for item in regexkawe:
                if item != '^':
                    aux2.append(item)
                else:
                    aux.append(aux2)
                    aux2 = []
            aux.append(aux2)
            regexkawe = aux
            regexkawe.pop(0)
            del aux
            del aux2
            xapvmal = []
            if rr==0:
                xipaalu['xipai'] = False
            else:
                xipaalu['xipai'] = True
            if len(hemvlkawe) > 0:
                for i in range(len(hemvlkawe)):
                    xapvmal.append((hemvlkawe[i], regexkawe[i],wzkawe[i],hemvlkawew[i]))
                xipaalu['hemvlkawe'] = xapvmal
                

    return xipaalu


def prueba(hemvla, mvlica=True):
    hemvla=[hemvl.strip().lower() for hemvl in hemvla.split()]
    for hemvl in hemvla:
        xipaalu = dict()

        xipaalu['vy'] = hemvl
        rr = len(koyam.kom_row)
            
        while True:
            koyam.kaxvrowvn()
            if rr == len(koyam.kom_row):
                break
            else:
                rr = len(koyam.kom_row)

        
        koyam = kintuxokin(koyam,0)[0]            
        hemvlkawe = koyam.wirintuku_hemvl2()
        hemvlkawe =  [wirintukunVy[wirina[0]][1](h) for h in hemvlkawe]
        hemvlkawew = [h.split('-')[1:] for h in hemvlkawe]
        regexkawe = koyam.wirintuku_regex()
        wzkawe = koyam.wirintuku_wz()
        wzkawe = [h.split('-')[1:] for h in wzkawe]
        aux = []
        aux2 = []
        for item in regexkawe:
            if item != '^':
                aux2.append(item)
            else:
                aux.append(aux2)
                aux2 = []
        aux.append(aux2)
        regexkawe = aux
        regexkawe.pop(0)
        del aux
        del aux2
        xapvmal = []
        if rr==0:
            xipaalu['xipai'] = False
        else:
            xipaalu['xipai'] = True
        if len(hemvlkawe) > 0:
            for i in range(len(hemvlkawe)):
                xapvmal.append((hemvlkawe[i], regexkawe[i],wzkawe[i],hemvlkawew[i]))
            xipaalu['hemvlkawe'] = xapvmal
    return xipaalu