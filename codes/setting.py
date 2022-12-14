

level_map1= [ #DONE 10 segundos
    'xxxxxxxxxxxxxxxxxxxxxxxxx',
    'xxxx                 xxxx',
    'xxxx                 xxxx',
    'xxxx                 xxxx',
    'xxxx                 xxxx',
    'xxxx        E        xxxx',
    'xxxx    xxxxxxxxx    xxxx',
    'xxxx                 xxxx',
    'xxxx                 xxxx',
    'xxxx                 xxxx',
    'xxxx M      P      M xxxx',
    'xxxxxxxxxxxxxxxxxxxxxxxxx',
    'xxxxxxxxxxxxxxxxxxxxxxxxx'
]

level_map2 = [ #done 15 SEGUNDOS    
    'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', 
    'x                                                 xxxx',
    'x                                            M    xxxx',
    'x                                            x    xxxx',
    'x                                                 xxxx',
    'x                                M       xxxxx    xxxx',
    'xM              xxx             xxx              xxxxx',
    'xxxx            xxx             xxx             xxxxxx',
    'x               xxx             xxx           xxxxxxxx',
    'x      xxx      xxx             xxx                xxx',
    'xM  P           xxxSSSSSSSSSSSSSxxx M             Exxx',
    'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'  
]

level_map3 = [ #DONE
    'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    'x                                                   x',
    'x                                                 xxx',
    'x                                   SS            xxx',
    'xES          SSS      S            xxxx       SS Mxxx',
    'xxxxx     xxxxxxxx   xxxxM                   xxxxxxxx',
    'x                        xxxx              SS     xxx',
    'x                                 ss     xxxx     xxx',
    'x                               xxxx              xxx',
    'x                xxxx                             xxx',
    'x            MSS                                  xxx',
    'x   P    xxxxxxxSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSxxx',
    'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
]


level_map4 = [ #possiveis ajustes
    'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    'x                                                xxxxx',
    'x                                                xxxxx',
    'x  Mw   G   Gw   w G    w        w     Gw        xxxxx',
    'x  xxxxxxxxxx     xxxxxx          xxxxxx         xxxxx',
    'x                               wG   w           xxxxx',
    'x              M      w  G  w    xxxx   w G  w   xxxxx',
    'x              xxxx    xxxxx             xxxx    xxxxx',
    'x                                                xxxxx',
    'x                                             xxxx  xx',
    'xEw  P  G    M    G       G   M     G    W    G  wM xx',
    'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
]

level_map5 = [ #DONE
    'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    'xxx                                                xxxx',
    'xxx                                                xxxx',
    'xxx            E          S    S           M       xxxx',
    'xxx           XXF   S     xxxxxx         S         xxxx',
    'xxx                xxx            wG  wS xxxx      xxxx',
    'xxx                          M     xxxxx           xxxx',
    'xxx      M            M   w  G  w           M      xxxx',
    'xxx  P     w  G  w         xxxxx         w   G w   xxxx',
    'xxxxxx      xxxxx  w  G  w       w  G  w  xxxxx    xxxx',
    'xxx                 xxxxx         xxxxx            xxxx',
    'xxxSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSxxxx',
    'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
]

level_map6 = [ #DONE
    'xxxxxxxxxxxxxxxxxxxxxxxxx',
    'xxxx                 xxxx',
    'xxxxM               Mxxxx',
    'xxxxxxxF         Fxxxxxxxx',
    'xxxx                 xxxx',
    'xxxxM               Mxxxx',
    'xxxxxxxxF       Fxxxxxxxx',
    'xxxx                 xxxx',
    'xxxxM               Mxxxx',
    'xxxxxxxxxF     Fxxxxxxxxx',
    'xxxxxxxxxx PE  xxxxxxxxxx',
    'xxxxxxxxxxxxxxxxxxxxxxxxx',
    'xxxxxxxxxxxxxxxxxxxxxxxxx'
]

level_map7 = [ #possiveis ajustes
    'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    'xxxx        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    'xxxx  xxxF  xxxxx            xxx                     xxxxxxxxxxxxxxxxxx',
    'xxxx  xx P  xxxxx    xxxF    Fxx                     xxxxxxxxxxxxxxxxxx',
    'xxxx  xxxxxxxxxxx     xxW G      G w  xxxxxxxxxxxx    xxxxxxxxxxxxxxxxx',
    'xxxx  xxxxxxxxxx xxx    xxxxxxxxxxx   xxxx   xxxxx    xxxxxxxxxxxxxxxxx',
    'xxxx    xxx     Mxxxxx  xxxxxxxxxxx   xxxx   xxxxx    xxxxxxxxxxxxxxxxx',
    'xxxxxF  xxx  xxxxxxxxx        xxxxW    G   wMxxxxx    xxx   xxxxxxxxxxx',
    'xxxx w   G   Wxxxxxxxx  xx       xxxxxxxxxxxxxxxxx        Mxxxxxxxxxxxx',
    'xxxx  xxxxxxxxxxxx      xxx     MxxxxxxxxxxxxxxxxF   Fxxxxxxxxxxxxxxxxx',
    'xxxx  xxxxxxxxxxxx  xx  xx xxxxxxxxxxxxxxxxxxxxxxF   Fxxxxxxxxx xxxxxxx',
    'xxxx                xx    MxxxxxxxxxxxxxxxxxxW G         G   GwExxxxxxx',
    'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
]

level_map8 = [ #possiveis ajustes
    'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    'xxxx                                                              Fxxx',
    'xxxx M  S FF     Fw  GS  wFw SS  SS  SS   SS G   G w    xxxx   M Fxxx',
    'xxxx  xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx            Fxxx',
    'xxxx                                                  w G     wFxxxxx',
    'xxxx                                                    Fxxxxxx  xxxx',
    'xxxx                            w  G w          xxxxxxxx         xxxx',
    'xxxx                            SFxxx     S  S                   xxxx',
    'xxxx                        xxxxx        xxxxxx                  xxxx',
    'xxxx                P      SF                                    xxxx',
    'xxxx            SFxxx   xxxxx                                    xxxx',
    'xxxxE X    G WxxxxxxxSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSxxxx',
    'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
]

tile_size = 56
screen_width = 1200
screen_height = 12 * tile_size #numeros de linhas totais em todos as fases

level_maps = [level_map1, level_map2,level_map3,level_map4,level_map5,level_map6,level_map7,level_map8] #Botei o mapa um no level2 so para testar o level_select
firebreathers_orientations = [[],[],[],[],['r'],['r','l','r','l','r','l','r','l'],['r','r','l','r','r','l','r','l'],['l','l','r','r','l','l','l','l','l','l','l','l']]

timer_maps = [10000,15000,20000,20000,20000,15000,35000,50000]#tempo em milisegundos
