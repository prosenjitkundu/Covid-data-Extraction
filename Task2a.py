import sys
import ply.lex as lex
import ply.yacc as yacc
import sys
import re
import requests


if __name__ == "__main__":
    file = open("a_file.txt", "w")
    tokens = [
        'TABLE',
        'THEADS',
        'THEADE',
        'TBODYS',
        'TBODYE',
        'TRS',
        'TDS',
        'TDE',
        'TRE',
        'NOBRS',
        'NOBRE',
        'AS',
        'AE',
        'BRS',
        'NAME',
        'THS',
        'THE',
        'SPANS',
        'SPANE',
        'NBSP'
    ]


    def t_TABLE(t):
        r'<table\sid="main_table_countries_yesterday"\sclass="table\stable-bordered\stable-hover\smain_table_countries"\sstyle="width:100%;margin-top:\s0px\s!important;display:none;">'
        return t

    def t_THEADS(t):
        r'<thead>'
        return t

    def t_THEADE(t):
        r'</thead>'
        return t

    def t_SPANS(t):
        r'<span[^>]*>'
        return t

    def t_SPANE(t):
        r'</span>'
        return t

    def t_TRS(t):
        r'<tr[^>]*>'
        return t

    def t_AS(t):
        r'<a[^>]*>'
        return t

    def t_AE(t):
        r'</a>'
        return t

    def t_THS(t):
        r'<th[^>]*>'
        return t

    def t_TRE(t):
        r'</tr>'
        return t

    def t_THE(t):
        r'</th>'
        return t

    def t_BRS(t):
        r'<br\s/>'
        return t

    def t_NOBRS(t):
        r'<nobr>'
        return t

    def t_NOBRE(t):
        r'</nobr>'
        return t

    def t_TBODYS(t):
        r'<tbody>'
        return t

    def t_TBODYE(t):
        r'</tbody>'
        return t

    def t_NBSP(t):
        r'&nbsp;'
        return t

    def t_TDS(t):
        r'<td[^>]*>'
        return t

    def t_TDE(t):
        r'</td>'
        return t

    def t_NAME(t):
        r'[A-Za-z0-9+-.]+'
        return t

    t_ignore = " \t"

    def t_error(t):
        t.lexer.skip(1)

    def p_start(t):
        '''start : infoall'''

    def p_infoall(t):
        '''infoall : TABLE THEADS idxval THEADE TBODYS contcntry TBODYE'''

    def p_idxval(t):
        '''idxval : TRS val val val val val val val val val val val val val val val val val val val val val val TRE'''

    def p_val(t):
        '''val : THS THE
               | THS txt THE
               | THS txt BRS txt THE
               | THS txt BRS NOBRS txt NOBRE THE
               | THS txt NBSP txt BRS txt THE'''

    def p_contcntry(t):
        '''contcntry : TRS res res res res res res res res res res res res res res res res res res res res res res TRE 
                     | TRS res res res res res res res res res res res res res res res res res res res res res res TRE contcntry'''

        CovidData = []
        CovidData.append(t[2])
        CovidData.append(t[3])
        CovidData.append(t[4])
        CovidData.append(t[5])
        CovidData.append(t[6])
        CovidData.append(t[7])
        CovidData.append(t[8])
        CovidData.append(t[9])
        CovidData.append(t[10])
        CovidData.append(t[11])
        CovidData.append(t[12])
        CovidData.append(t[13])
        CovidData.append(t[14])
        CovidData.append(t[15])
        CovidData.append(t[16])
        CovidData.append(t[17])
        CovidData.append(t[18])
        CovidData.append(t[19])
        CovidData.append(t[20])
        CovidData.append(t[21])
        CovidData.append(t[22])
        CovidData.append(t[23])
        for element in CovidData:
            if element is None or element == '' or element == 'N-A':
                file.write("None ")
            else:
                file.write(element + " ")
        file.write("\n")

    def p_res(t):
        '''res : TDS TDE
               | TDS txt TDE
               | TDS NOBRS txt NOBRE TDE
               | TDS AS txt AE TDE
               | TDS NOBRS NOBRE TDE
               | TDS SPANS txt SPANE TDE'''
        if(len(t) == 4):
            t[0] = t[2]
        elif(len(t) == 6):
            t[0] = t[3]

    def p_txt(t):
        '''txt : NAME 
               | NAME txt'''
        if(len(t) == 2):
            t[0] = t[1]
        elif(len(t) > 2):
            t[0] = t[1]+"-"+t[2]

    def p_error(t):
        pass

    lexer = lex.lex()
    strp = 'https://www.worldometers.info/coronavirus/'
    r = requests.get(strp, allow_redirects=True)
    f = open('world_data.html', 'wb').write(r.content)
    wrld = open('world_data.html')
    s = str(wrld.read())

    lexer.input(s)
    parser = yacc.yacc()
    # Tokenize

    parser.parse(s)
    file.close()
    det = open('details.txt', "a")
    while(1):
        try:
            print("Wanted to know the details of ???")
            print("Enter 1 for Country")
            print("Enter 2 for Continent")
            print("Enter 3 for World")
            c = int(input())
            if(c == 1):
                print("Enter 1 for country Micronesia")
                print("Enter 2 for country Saint-Helena")
                print("Enter 3 for country Marshall-Islands")      
                print("Enter 4 for country Vanuatu")
                print("Enter 5 for country MS-Zaandam")
                print("Enter 6 for country Western-Sahara")        
                print("Enter 7 for country Vatican-City")
                print("Enter 8 for country Samoa")
                print("Enter 9 for country Macao")
                print("Enter 10 for country Falkland-Islands")     
                print("Enter 11 for country Tonga")
                print("Enter 12 for country Montserrat")
                print("Enter 13 for country Wallis-and-Futuna")    
                print("Enter 14 for country Diamond-Princess")     
                print("Enter 15 for country Saint-Pierre-Miquelon")
                print("Enter 16 for country Anguilla")
                print("Enter 17 for country Kiribati")
                print("Enter 18 for country Palau")
                print("Enter 19 for country St.-Barth")
                print("Enter 20 for country Solomon-Islands")
                print("Enter 21 for country Saint-Kitts-and-Nevis")
                print("Enter 22 for country Turks-and-Caicos")
                print("Enter 23 for country Sao-Tome-and-Principe")
                print("Enter 24 for country British-Virgin-Islands")
                print("Enter 25 for country St.-Vincent-Grenadines")
                print("Enter 26 for country Chad")
                print("Enter 27 for country Antigua-and-Barbuda")
                print("Enter 28 for country Liberia")
                print("Enter 29 for country Caribbean-Netherlands")
                print("Enter 30 for country Sierra-Leone")
                print("Enter 31 for country Bhutan")
                print("Enter 32 for country Guinea-Bissau")
                print("Enter 33 for country Comoros")
                print("Enter 34 for country Niger")
                print("Enter 35 for country Monaco")
                print("Enter 36 for country Sint-Maarten")
                print("Enter 37 for country Eritrea")
                print("Enter 38 for country Saint-Martin")
                print("Enter 39 for country Dominica")
                print("Enter 40 for country Liechtenstein")
                print("Enter 41 for country Bermuda")
                print("Enter 42 for country Greenland")
                print("Enter 43 for country Yemen")
                print("Enter 44 for country Gambia")
                print("Enter 45 for country Grenada")
                print("Enter 46 for country San-Marino")
                print("Enter 47 for country CAR")
                print("Enter 48 for country Gibraltar")
                print("Enter 49 for country Djibouti")
                print("Enter 50 for country Equatorial-Guinea")
                print("Enter 51 for country South-Sudan")
                print("Enter 52 for country Tajikistan")
                print("Enter 53 for country Cayman-Islands")
                print("Enter 54 for country Nicaragua")
                print("Enter 55 for country Taiwan")
                print("Enter 56 for country Burkina-Faso")
                print("Enter 57 for country New-Zealand")
                print("Enter 58 for country Timor-Leste")
                print("Enter 59 for country Saint-Lucia")
                print("Enter 60 for country Isle-of-Man")
                print("Enter 61 for country Congo")
                print("Enter 62 for country Brunei")
                print("Enter 63 for country Hong-Kong")
                print("Enter 64 for country Somalia")
                print("Enter 65 for country Benin")
                print("Enter 66 for country Mauritius")
                print("Enter 67 for country Faeroe-Islands")
                print("Enter 68 for country Haiti")
                print("Enter 69 for country Mali")
                print("Enter 70 for country Lesotho")
                print("Enter 71 for country Bahamas")
                print("Enter 72 for country Tanzania")
                print("Enter 73 for country Aruba")
                print("Enter 74 for country Guinea")
                print("Enter 75 for country Mayotte")
                print("Enter 76 for country Togo")
                print("Enter 77 for country Andorra")
                print("Enter 78 for country Burundi")
                print("Enter 79 for country Seychelles")
                print("Enter 80 for country New-Caledonia")
                print("Enter 81 for country Cura-ccedil-ao")
                print("Enter 82 for country Papua-New-Guinea")
                print("Enter 83 for country Channel-Islands")
                print("Enter 84 for country Gabon")
                print("Enter 85 for country Barbados")
                print("Enter 86 for country Syria")
                print("Enter 87 for country Belize")
                print("Enter 88 for country Cabo-Verde")
                print("Enter 89 for country French-Polynesia")
                print("Enter 90 for country Mauritania")
                print("Enter 91 for country Sudan")
                print("Enter 92 for country Guyana")
                print("Enter 93 for country Madagascar")
                print("Enter 94 for country Fiji")
                print("Enter 95 for country Eswatini")
                print("Enter 96 for country Malta")
                print("Enter 97 for country Suriname")
                print("Enter 98 for country French-Guiana")
                print("Enter 99 for country Ivory-Coast")
                print("Enter 100 for country Malawi")
                print("Enter 101 for country Senegal")
                print("Enter 102 for country DRC")
                print("Enter 103 for country Iceland")
                print("Enter 104 for country Angola")
                print("Enter 105 for country Martinique")
                print("Enter 106 for country Cameroon")
                print("Enter 107 for country Guadeloupe")
                print("Enter 108 for country Trinidad-and-Tobago")
                print("Enter 109 for country Cambodia")
                print("Enter 110 for country Jamaica")
                print("Enter 111 for country Rwanda")
                print("Enter 112 for country Laos")
                print("Enter 113 for country El-Salvador")
                print("Enter 114 for country Namibia")
                print("Enter 115 for country Ghana")
                print("Enter 116 for country Maldives")
                print("Enter 117 for country Uganda")
                print("Enter 118 for country Afghanistan")
                print("Enter 119 for country Luxembourg")
                print("Enter 120 for country Kyrgyzstan")
                print("Enter 121 for country Mozambique")
                print("Enter 122 for country Montenegro")
                print("Enter 123 for country Zimbabwe")
                print("Enter 124 for country Uzbekistan")
                print("Enter 125 for country Nigeria")
                print("Enter 126 for country R-eacute-union")
                print("Enter 127 for country Botswana")
                print("Enter 128 for country Algeria")
                print("Enter 129 for country Albania")
                print("Enter 130 for country North-Macedonia")
                print("Enter 131 for country Cyprus")
                print("Enter 132 for country Zambia")
                print("Enter 133 for country Kenya")
                print("Enter 134 for country Qatar")
                print("Enter 135 for country Bosnia-and-Herzegovina")
                print("Enter 136 for country Oman")
                print("Enter 137 for country Honduras")
                print("Enter 138 for country Armenia")
                print("Enter 139 for country Estonia")
                print("Enter 140 for country Mongolia")
                print("Enter 141 for country Egypt")
                print("Enter 142 for country Ethiopia")
                print("Enter 143 for country Bahrain")
                print("Enter 144 for country Libya")
                print("Enter 145 for country Singapore")
                print("Enter 146 for country Moldova")
                print("Enter 147 for country Venezuela")
                print("Enter 148 for country Latvia")
                print("Enter 149 for country Myanmar")
                print("Enter 150 for country Palestine")
                print("Enter 151 for country Dominican-Republic")
                print("Enter 152 for country Finland")
                print("Enter 153 for country Kuwait")
                print("Enter 154 for country Paraguay")
                print("Enter 155 for country Sri-Lanka")
                print("Enter 156 for country Saudi-Arabia")
                print("Enter 157 for country Guatemala")
                print("Enter 158 for country Panama")
                print("Enter 159 for country Azerbaijan")
                print("Enter 160 for country Costa-Rica")
                print("Enter 161 for country Uruguay")
                print("Enter 162 for country Ecuador")
                print("Enter 163 for country Lithuania")
                print("Enter 164 for country Belarus")
                print("Enter 165 for country Slovenia")
                print("Enter 166 for country UAE")
                print("Enter 167 for country Bolivia")
                print("Enter 168 for country Tunisia")
                print("Enter 169 for country Nepal")
                print("Enter 170 for country Croatia")
                print("Enter 171 for country Lebanon")
                print("Enter 172 for country Bulgaria")
                print("Enter 173 for country Norway")
                print("Enter 174 for country Cuba")
                print("Enter 175 for country Morocco")
                print("Enter 176 for country Slovakia")
                print("Enter 177 for country Ireland")
                print("Enter 178 for country Kazakhstan")
                print("Enter 179 for country S.-Korea")
                print("Enter 180 for country Georgia")
                print("Enter 181 for country Pakistan")
                print("Enter 182 for country Jordan")
                print("Enter 183 for country Hungary")
                print("Enter 184 for country Serbia")
                print("Enter 185 for country Bangladesh")
                print("Enter 186 for country Greece")
                print("Enter 187 for country Denmark")
                print("Enter 188 for country Iraq")
                print("Enter 189 for country Austria")
                print("Enter 190 for country Sweden")
                print("Enter 191 for country Vietnam")
                print("Enter 192 for country Romania")
                print("Enter 193 for country Switzerland")
                print("Enter 194 for country Thailand")
                print("Enter 195 for country Chile")
                print("Enter 196 for country Australia")
                print("Enter 197 for country Malaysia")
                print("Enter 198 for country Portugal")
                print("Enter 199 for country Canada")
                print("Enter 200 for country Czechia")
                print("Enter 201 for country Belgium")
                print("Enter 202 for country Peru")
                print("Enter 203 for country Israel")
                print("Enter 204 for country Philippines")
                print("Enter 205 for country South-Africa")
                print("Enter 206 for country Japan")
                print("Enter 207 for country Ukraine")
                print("Enter 208 for country Indonesia")
                print("Enter 209 for country Mexico")
                print("Enter 210 for country Poland")
                print("Enter 211 for country Netherlands")
                print("Enter 212 for country Colombia")
                print("Enter 213 for country Iran")
                print("Enter 214 for country Argentina")
                print("Enter 215 for country Spain")
                print("Enter 216 for country Italy")
                print("Enter 217 for country Germany")
                print("Enter 218 for country Turkey")
                print("Enter 219 for country Russia")
                print("Enter 220 for country UK")
                print("Enter 221 for country France")
                print("Enter 222 for country Brazil")
                print("Enter 223 for country India")
                print("Enter 224 for country USA")
                print("Enter 225 for country China")
                l = int(input())
                if(l > 225 or l < 1):
                    print("Input out of range")
                else:
                    print("Enter the information to be retrive")
                    print("Enter 1 for TOTAL CASES")
                    print("Enter 2 for NEW CASES")
                    print("Enter 3 for TOTAL DEATHS")
                    print("Enter 4 for TOTAL RECOVERED")
                    print("Enter 5 for NEW RECOVERED")
                    print("Enter 6 for ACTIVE CASES")
                    print("Enter 7 for CRITICAL")
                    print("Enter 8 for TOT CASES/1M pop")
                    print("Enter 9 for DEATHS/1M pop")
                    print("Enter 10 for TESTS/1M pop")
                    print("Enter 11 for Population")
                    idx = int(input())
                    if(idx > 11 or idx < 1):
                        print("Input out of range")
                    else:
                        linestr = []
                        with open('a_file.txt') as fn:
                            linestr = fn.readlines()
                        idx = idx + 1
                        print(linestr[l].split()[idx])
                        det.write(linestr[l].split()[idx])
                        det.write("\n")
            elif(c == 2):
                #print("Enter 226 for country World")
                print("Enter 1 for country Other")
                print("Enter 2 for country Oceania")
                print("Enter 3 for country Africa")
                print("Enter 4 for country Europe")
                print("Enter 5 for country South-America")
                print("Enter 6 for country North-America")
                print("Enter 7 for country Asia")
                l = int(input())
                if(l > 7 or l < 1):
                    print("Input out of range")
                else:
                    print("Enter the information to be retrive")
                    print("Enter 1 for TOTAL CASES")
                    print("Enter 2 for NEW CASES")
                    print("Enter 3 for TOTAL DEATHS")
                    print("Enter 4 for TOTAL RECOVERED")
                    print("Enter 5 for NEW RECOVERED")
                    print("Enter 6 for ACTIVE CASES")
                    print("Enter 7 for CRITICAL")
                    print("Enter 8 for TOT CASES/1M pop")
                    print("Enter 9 for DEATHS/1M pop")
                    print("Enter 10 for TESTS/1M pop")
                    print("Enter 11 for Population")
                    idx = int(input())
                    if(idx > 11 or idx < 1):
                        print("Input out of range")
                    else:
                        linestr = []
                        with open('a_file.txt') as fn:
                            linestr = fn.readlines()
                        idx = idx + 1
                        l = l + 225
                        print(linestr[l].split()[idx])
                        det.write(linestr[l].split()[idx])
                        det.write("\n")

            elif(c == 3):
                    print("Enter the information to be retrive")
                    print("Enter 1 for TOTAL CASES")
                    print("Enter 2 for NEW CASES")
                    print("Enter 3 for TOTAL DEATHS")
                    print("Enter 4 for TOTAL RECOVERED")
                    print("Enter 5 for NEW RECOVERED")
                    print("Enter 6 for ACTIVE CASES")
                    print("Enter 7 for CRITICAL")
                    print("Enter 8 for TOT CASES/1M pop")
                    print("Enter 9 for DEATHS/1M pop")
                    print("Enter 10 for TESTS/1M pop")
                    print("Enter 11 for Population")
                    idx = int(input())
                    if(idx > 11 or idx < 1):
                        print("Input out of range")
                    else:
                        linestr = []
                        with open('a_file.txt') as fn:
                            linestr = fn.readlines()
                        idx = idx + 1
                        print(linestr[225].split()[idx])
                        det.write(linestr[225].split()[idx])
                        det.write("\n")
            else:
                print("Invalid input")
        except:
            print("Input is not correct")
        print("Want to retive more specific details????")
        print("Enter 0 for NO")
        print("Enter 1 for YES")
        y = int(input())
        if(y==0):
            det.close()
            break
    
