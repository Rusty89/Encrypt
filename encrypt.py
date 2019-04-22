import re
import random

def main():
    
    try:
        def encrypt(string,level,degree):
            if level==0:
                return(string)
            new_string=""
            alphabet=("abEFefghABCDmnopq&*()tuvwxy_+{}rszGHIJKLM"+
                      "RSTU3NOPQ45678VWXY90~!@#$%|Zi `12:<c>?[jkld];,\/.'""^")
            for chop in range(0,len(string),degree):
                for letter in string[chop:chop+degree-1]:
                    for i in range(len(alphabet)):
                        if letter==alphabet[i]:
                            new_string+=alphabet[i-1]
                new_string+=string[chop+degree-1:chop+degree]
            if level>0:
                return(encrypt(new_string,level-1,degree))
            
        salt=["asdcd","dfds","retscg","dfsa","treyrtg","aFcgE", "Tscghe","asdD","32cg","234cgeDwe","dscg2346","1325","3261"]
        save=""
        file_read=""
        encrypt_decrypt=(input("Type Decrypt(D) or Encrypt(E) to begin, type Exit to leave>>>   ")).capitalize()
        print("")
        if encrypt_decrypt=="Encrypt" or encrypt_decrypt=="E":
            message=input("Enter message you want encrypted or type Encrypt(E) again to\nopen a txt file"+
                          " located in the same folder as this program>>>   ")
            print("")
            
            if message.capitalize()=="E" or message.capitalize()=="Encrypt":
                provided_file=open(input("Enter the name of file you want encrypted>>>   ")+".txt","r")
                print("")
                message=(provided_file.read())

                message=message.replace('.', 'peRioD')
                message=message.replace('"', 'qUotE')
                message=message.replace(',', 'cOMmA')
                message=message.replace('?', 'queStIoNMarK')
                message=message.replace('\n', ' ').replace('\r', ' ')
                message= re.sub('[^0-9a-zA-Z]+', ' ', message)
                #add salt
                
                while(" " in message):
                        for i in range(len(message)):
                                
                                if (message[i]==" "):                                        
                                        indice=random.randint(0,len(salt)-1)
                                        message = message[:i]+salt[indice]+message[i+1:]
                                        
                
                provided_file.close()
                encryption_level=int(input("Enter encryption key>>>   "))
                while encryption_level>91:
                    print("")
                    encryption_level=int(input("Encryption level too high enter lower value>>>   "))
                print("")
                encryption_degree=int(input("Enter encryption degree>>>   "))
                while encryption_degree<1:
                    print("")
                    encryption_degree=int(input("Encryption degree to low>>>   "))
                print("")
                encrypted_message=encrypt(message,encryption_level,encryption_degree)
                file_read="True"

            if file_read!="True":
                encryption_level=int(input("Enter encryption key>>>   "))
                while encryption_level>91:
                    print("")
                    encryption_level=int(input("Encryption level too high enter lower value>>>   "))
                print("")
                encryption_degree=int(input("Enter encryption degree>>>   "))
                while encryption_degree<1:
                    print("")
                    encryption_degree=int(input("Encryption degree to low>>>   "))
                print("")

                ### replace periods, commas and quotes, remove newlines, get rid of any remaining non alphanumerics.
                message=message.replace('.', 'peRioD')
                message=message.replace('"', 'qUotE')
                message=message.replace(',', 'cOMmA')
                message=message.replace('?', 'queStIoNMarK')
                message=message.replace('\n', ' ').replace('\r', ' ')
                message= re.sub('[^0-9a-zA-Z]+', ' ', message)
                
                #add salt
                
                while(" " in message):
                        for i in range(len(message)):
                                
                                if (message[i]==" "):                                        
                                        indice=random.randint(0,len(salt)-1)
                                        message = message[:i]+salt[indice]+message[i+1:]
                                        
                                
                encrypted_message=encrypt(message,encryption_level,encryption_degree)
                
            print("Encrypted message is as follows>>>  ",encrypted_message)
            print("")
            save=input("Would you like to save your encrypted message?(Y/N)>>>")
            print("")
            if save.upper()=="Y":
                encrypted_file=open(input("Enter the name of the new encrypted file>>>   ")+".txt","w")
                encrypted_file.write(str(encryption_level)+"\n"+str(encryption_degree)+"\n")
                encrypted_file.write(encrypted_message)
                encrypted_file.close()
                print("")
                print("Message encrypted and saved.")
                print("")

                
        if encrypt_decrypt=="Decrypt" or encrypt_decrypt=="D":        
            message=input("Enter message you want decrypted or type Decrypt(D) again to\nopen previously recorded encryption>>>   ")
            print("")
            if message.capitalize()=="D" or message.capitalize()=="Decrypt":
                encrypted_file=open(input("Enter the name of the encrypted file>>>   ")+".txt","r")
                print("")
                encryption_level=int(encrypted_file.readline())
                encryption_degree=int(encrypted_file.readline())
                message=(encrypted_file.readline())
                
                encrypted_file.close()
                decrypted_message=encrypt(message,92-encryption_level,encryption_degree)
                ### replace periods and quotes
                
                decrypted_message=decrypted_message.replace('peRioD', '.')
                decrypted_message=decrypted_message.replace('qUotE', '"')
                decrypted_message=message.replace('cOMmA',',')
                
                decrypted_message=decrypted_message.replace("queStIoNMarK",'?')
                #remove salt
                for i in salt:
                        
                        decrypted_message = decrypted_message.replace(i, " ")
                print("Decrypted message is as follows>>>  ",decrypted_message)
                print("")
                save=input("Would you like to save your decrypted message?(Y/N)>>>")
                print("")
                if save.upper()=="Y":
                    decrypted_file=open(input("Enter the name of the new decrypted file>>>   ")+".txt","w")
                    decrypted_file.write(decrypted_message)
                    decrypted_file.close()
                    print("")
                    print("Message decrypted and saved.")
                    print("")
                file_read="True"
            if file_read!="True":        
                encryption_level=int(input("Enter encryption key>>>   "))
                while encryption_level>91:
                    print("")
                    encryption_level=int(input("Encryption level too high enter lower value>>>   "))
                print("")
                encryption_degree=int(input("Enter encryption degree>>>   "))
                while encryption_degree<1:
                    print("")
                    encryption_degree=int(input("Encryption degree to low>>>   "))
                print("")
                decrypted_message=encrypt(message,92-encryption_level,encryption_degree)
                ### replace periods and quotes
                decrypted_message=decrypted_message.replace('peRioD', '.')
                decrypted_message=decrypted_message.replace('qUotE', '"')
                decrypted_message=decrypted_message.replace('cOMmA',',')
                
                decrypted_message=decrypted_message.replace('queStIoNMarK','?')
                ##remove gibberish
                for i in salt:
                        
                        decrypted_message = decrypted_message.replace(i, " ")
                print("Decrypted message is as follows>>>  ",decrypted_message)
                print("")
                save=input("Would you like to save your decrypted message?(Y/N)>>>")
                print("")
                if save.upper()=="Y":
                    decrypted_file=open(input("Enter the name of the new decrypted file>>>   ")+".txt","w")
                    decrypted_file.write(decrypted_message)
                    decrypted_file.close()
                    print("")
                    print("Message decrypted and saved.")
                    print("")
        if encrypt_decrypt=="Exit":
            global run
            run="exit"
    except ValueError:
        print("\nAn incorrect value was entered causing an error, program restarting...\n")
        main()
    except TypeError:
        print("\nAn incorrect value was entered causing an error, program restarting...\n")
        main()
    except FileNotFoundError:
        print("\nUnable to locate file specified, program restarting...\n")
        main()
run="run"        
while run!="exit":
    main()
