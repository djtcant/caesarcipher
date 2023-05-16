import streamlit as st

# Expander section
with st.expander("About"):
  st.write("""Use this App to Encipher or Decipher a message! Choose a key and then communicate with your friends in secrecy!""")


alphabet = "abcdefghijklmnopqrstuvwxyz"

st.subheader('Enter your message and key:')

message = st.text_input("Type a message")
st.write('The current message is', message)

key = st.number_input('Choose a key', step=1)
st.write('The current key is ', key)

messageOut = ""


def encipher (message, key):
  messageOut = ""  
  for letter in message:
      letter = letter.lower()
      if letter in alphabet:
        position = alphabet.find(letter)
        newchar = alphabet[(position + key) % 26]
        messageOut += newchar
      else:
        messageOut += letter
  return messageOut      
        
def decipher (message, key):
  messageOut = ""  
  for letter in message:
      letter = letter.lower()
      if letter in alphabet:
        position = alphabet.find(letter)
        newchar = alphabet[(position - key) % 26]
        messageOut += newchar
      else:
        messageOut += letter
  return messageOut      
        
st.subheader('Choose to Encipher or Decipher:')

if st.button('Encipher'):
  st.write('Enciphering...')
  messageOut = encipher(message, key)
  st.write(messageOut)
  
if st.button('Decipher'):
  st.write('Deciphering...')
  messageOut = decipher(message, key)
  st.write(messageOut)
