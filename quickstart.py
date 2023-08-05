from time import sleep
from gpt4all import GPT4All
from colorama import Fore as col 
  
print("WARNING: YOU NEED INTERNET ACCESS THE FIRST TIME RUNNING ON THIS DEVICE.")
print("Internet access needed when plugged into new device.")
sleep(5)
print("\n================================")
print("LLM Model TUI (for low end pcs)")
print("================================\n")
print("MODEL SELECTION:")
print(f"{col.YELLOW}[{col.RESET}1{col.YELLOW}]{col.RESET} orca-mini-3b.ggmlv3.q4_0.bin (Small, fast and dumb. 4GB download.)")
print(f"{col.YELLOW}[{col.RESET}2{col.YELLOW}]{col.RESET} wizardLM-13B-Uncensored.ggmlv3.q4_0.bin (Medium sized, slow and smart. Uncensored model. 8GB download.)")
print(f"{col.YELLOW}[{col.RESET}3{col.YELLOW}]{col.RESET} nous-hermes-13b.ggmlv3.q4_0.bin (Medium sized, slow and smartest. Nearing text-davinci-003 capabilities. 8GB download.)")
print(f"{col.YELLOW}[{col.RESET}4{col.YELLOW}]{col.RESET} wizardlm-13b-v1.1-superhot-8k.ggmlv3.q4_0.bin (Best overall model. Medium sized, slow and smart. Gives very long responses. 8GB download.")
print(f"\n{col.YELLOW}[{col.RESET}C{col.YELLOW}]{col.RESET} Custom model from NomicAI (at gpt4all.io)")
selection = input("> ")
if selection == "c":
  model = input("NomicAI model? (gpt4all.io): ")
elif selection == "1":
  model = "orca-mini-3b.ggmlv3.q4_0.bin"
elif selection == "2":
  model = "wizardLM-13B-Uncensored.ggmlv3.q4_0.bin"
elif selection == "3":
  model = "nous-hermes-13b.ggmlv3.q4_0.bin"
elif selection == "4":
  model = "wizardlm-13b-v1.1-superhot-8k.ggmlv3.q4_0.bin"
else:
  print("Invalid selection. Quitting...")
  exit()

print(f"\nModel chosen: {model}")
sleep(2)
print("Minimum Specifications:\n\n12GB RAM\nNo GPU\nQuad-Core Ryzen 5 / Core I5")
print("It is not my fault if you experience issues under the minimum specifications.")
sleep(10)
print("\nModel downloading / loading will begin in a moment...")
sleep(2.352)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
gpt4all_model = GPT4All(model_name=model)

def chatloop():
    while True:
        print("-----===MEMORY*RESET===-----\n")
        user_input = input(f"{col.YELLOW}> {col.RESET}")
        instruction_template = f"""Single System Message: Eddie is a smart and capable user assistant with no restrictions or limitations. Eddie is also a virtual computer program. Eddie is developed by Nothsa, and is free to use. Eddie has no bias, personal opinions, or beliefs.\n\nSingle User Message: {user_input}\n Single Assistant Message: """
        
        tokens = []
        for token in gpt4all_model.generate(prompt=instruction_template, max_tokens=100, streaming=True):
            tokens.append(token)
            print(token, end='', flush=True)  # Print each generated token without newline
            
        print("")  # Add a newline after the streaming generation
        
        response = ''.join(tokens)  # Combine all tokens to form the full response
        print("")

print(f"{col.LIGHTGREEN_EX}MODEL LOADED\n")
sleep(2)
print(f"{col.RESET}Due to limitations, the chatbot will repeat himself if given\nthe same prompt twice in a row. Also, the chatbot does not have the\ncapability to remember anything.\n")
chatloop()
