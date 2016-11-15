from random import randint

def vyhodnot( pole ):
    if 'xxx' in pole:
        return 'x'
    elif 'ooo' in pole:
        return 'o'
    elif '-' not in pole:
        return '!'
    else:
        return '-'

def tah( pole, index, symbol ):
    """Vrátí herní pole s daným symbolem umístěným na danou pozici."""
    if pole[ index ] != '-':
        raise ValueError( 'Obsazeno.' )
    else:
        return pole[ :index ] + symbol + pole[ index + 1: ]

def tah_hrace( pole ):
    """Získá od uživatele pozici, kam chce táhnout, a vrátí pole se zaznamenaným tahem hráče."""
    while True:
        try:
            kam_hrat = int( input( 'Kam chceš hrát? (0-{}): '.format( len( pole ) - 1 ) ) )
        except ValueError:
            print( 'To není číslice!' )
        else:
            if kam_hrat < 0 or kam_hrat >= len( pole ):
                print( 'Nemůžeš hrát mimo pole!' )
            elif pole[ kam_hrat ] != '-':
                print( 'Sleponi. Tam není volno!' )
            else:
                return tah( pole, kam_hrat, 'o' )

def tah_pocitace( pole ):
    'PC najde \"idealni\" pole a zahraje na nej.'

    while '-' in pole:
        if 'o' in pole[0] and '-' in pole[1]:
            pc_tahne = 1

        elif 'o' in pole[19] and '-' in pole[18]:
            pc_tahne = 18

        elif '-xx' in pole:
            kde_je_v_poli = pole.index( '-xx' )
            pc_tahne = kde_je_v_poli

        elif 'xx-' in pole:
            kde_je_v_poli = pole.index( 'xx-' )
            pc_tahne = kde_je_v_poli + 2

        elif 'x-x' in pole:
            kde_je_v_poli = pole.index( 'x-x' )
            pc_tahne = kde_je_v_poli + 1

        elif 'xoo-' in pole:
            kde_je_v_poli = pole.index( 'xoo-' )
            pc_tahne = kde_je_v_poli + 3

        elif '-oox' in pole:
            kde_je_v_poli = pole.index( '-oox' )
            pc_tahne = kde_je_v_poli

        elif 'o-o' in pole:
            kde_je_v_poli = pole.index( 'o-o' )
            pc_tahne = kde_je_v_poli + 1

        elif '-x-' in pole:
            kde_je_v_poli = pole.index( '-x-' )
            pc_tahne = kde_je_v_poli

        elif '-o-' in pole:
            kde_je_v_poli = pole.index( '-o-' )
            pc_tahne = kde_je_v_poli

        elif '-oo-' in pole:
            print( 'Ale ne. Už jsem zase prohrál.' )
            break

        elif 'x' not in pole or 'o' not in pole:
            pc_tahne = 9

        else:
            while True:
                a = randint( 0, len( pole ) - 1 )
                if pole[a] == '-':
                    pc_tahne = a
                    break

        return tah( pole, pc_tahne, 'x' )

def piskvorky1d():
    pole = '-' * 20
    i = 0
    while True:
        if i % 2 == 0:
            pole = tah_hrace( pole )
        else:
            pole = tah_pocitace( pole )
        print( pole )

        if vyhodnot( pole ) == 'o':
            print( 'Vyhrál jsi!' )
        elif vyhodnot( pole ) == 'x':
            print( 'Vyhrál jsem! Chachá!' )
        elif vyhodnot( pole ) == '!':
            print( 'Remíza! Jsem stejně dobrej jako ty!' )

        if vyhodnot( pole ) != '-':
            break

        i += 1

piskvorky1d()
