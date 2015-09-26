from default import addDir, art, versao, addLink
from utils import versao_disponivel, addDir, addLink
from resources.lib.daring import tvporpath


def menu_principal():
    if xbmc.getCondVisibility('system.platform.linux') or xbmc.getCondVisibility('system.platform.windows') or xbmc.getCondVisibility('system.platform.osx'):
        addDir('Ver Grava��es','nada',12,tvporpath + art + 'gravador-ver1.png',1,'Aceda � lista das grava��es j� efectuadas',False)
    disponivel=versao_disponivel()
    if disponivel==versao: addLink('�ltima versao (' + versao+ ')','',tvporpath + art + 'versao-ver2.png')
    else: addDir('Instalada v' + versao + ' | Actualiza��o v' + disponivel,'nada',15,tvporpath + art + 'versao-ver2.png',1,'',False)
    addDir("Defini��es do addon",'nada',22,tvporpath + art + 'defs-ver2.png',1,'',False)
    addDir("[COLOR red][B]LER AVISO[/B][/COLOR]",'nada',23,tvporpath + art + 'aviso-ver2.png',1,'',False)
    xbmc.executebuiltin("Container.SetViewMode(500)")