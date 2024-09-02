hangul_to_eng = {
    'ㅂ': 'q', 'ㅈ': 'w', 'ㄷ': 'e', 'ㄱ': 'r', 'ㅅ': 't', 'ㅛ': 'y', 'ㅕ': 'u', 'ㅑ': 'i', 'ㅐ': 'o', 'ㅔ': 'p',
    'ㅁ': 'a', 'ㄴ': 's', 'ㅇ': 'd', 'ㄹ': 'f', 'ㅎ': 'g', 'ㅗ': 'h', 'ㅓ': 'j', 'ㅏ': 'k', 'ㅣ': 'l',
    'ㅋ': 'z', 'ㅌ': 'x', 'ㅊ': 'c', 'ㅍ': 'v', 'ㅠ': 'b', 'ㅜ': 'n', 'ㅡ': 'm',
    'ㅃ': 'shift + q', 'ㅉ': 'shift + w', 'ㄸ': 'shift + e', 'ㄲ': 'shift + r', 'ㅆ': 'shift + t', 'ㅒ': 'shift + o', 'ㅖ': 'shift + p',
    'ㅘ':'h, k', 'ㅙ':'h, o', 'ㅚ':'h, l','ㅝ':'n, j', 'ㅞ':'n, p', 'ㅟ':'n, l', 'ㅢ':'m, l',
    'ㄳ':'r, t', 'ㄵ':'s, w', 'ㄶ':'s, g', 'ㄺ' : 'f, r', 'ㄻ':'f, a', 'ㄼ':'f, q', 'ㄽ':'f, t', 'ㄾ':'f, x', 'ㄿ':'f, v', 'ㅀ' : 'f, g', 'ㅄ':'q, t'
}

chosung_list = "ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ"
jungsung_list = "ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ"
jongsung_list = "ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ"
result =[]
def main(char):
        global result
        if '가' <= char <= '힣':
            char_code = ord(char) - ord('가')
            chosung = char_code // (21 * 28)
            jungsung = (char_code % (21 * 28)) // 28
            jongsung = char_code % 28

            result.append(hangul_to_eng[chosung_list[chosung]])
            result.append(hangul_to_eng[jungsung_list[jungsung]])
            if jongsung != 0:
                result.append(hangul_to_eng[jongsung_list[jongsung - 1]])
        else:
                 try: result.append('space, backspace, ' + hangul_to_eng[char]+ ', space, backspace')
                 except KeyError:
                     result.append(char)