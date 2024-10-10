def check_int(input_str):
    digits=('1','2','3','4','5','6','7','8','9','0')
    for i in range(len(input_str)):
        if (input_str[i] not in digits):
            return False
    else:
        if input_str=='':return False
        else:            return True

def crypt_nn(in_key)->list:
    pass_key = []
    in_key= int(in_key)
    for i in range(1,in_key):
         for ii in range(i,in_key):
            if in_key%(i+ii)==0 and i!=ii:
                        pass_key.append(i)
                        pass_key.append(ii)
    return(pass_key)

in_key=input('-> ')
while check_int(in_key):
    print(crypt_nn(in_key))
    in_key = input('-> ')