from time import sleep
from gpt4all import GPT4All
from colorama import Fore as col
  
print("WARNING: YOU NEED INTERNET ACCESS THE FIRST TIME RUNNING ON THIS DEVICE.")
print("Internet access needed when plugged into new device.")
sleep(5)
print("MODEL SELECTION:")
print(f"{col.YELLOW}[{col.RESET}1{col.YELLOW}]{col.RESET} orca-mini-3b.ggmlv3.q4_0.bin (Small, fast and dumb. 4GB download.)")
print(f"{col.YELLOW}[{col.RESET}2{col.YELLOW}]{col.RESET} wizardLM-13B-Uncensored.ggmlv3.q4_0.bin (Medium sized, slow and smart. Uncensored model. 8GB download.)")
print(f"{col.YELLOW}[{col.RESET}3{col.YELLOW}]{col.RESET} nous-hermes-13b.ggmlv3.q4_0.bin (Medium sized, slow and smartest. Nearing text-davinci-003 capabilities. 8GB download.)")
print(f"{col.YELLOW}[{col.RESET}4{col.YELLOW}]{col.RESET} wizardlm-13b-v1.1-superhot-8k.ggmlv3.q4_0.bin (Best overall model. Medium sized, slow and smart. Gives very long responses. 8GB download.")
selection = input("> ")
if selection == "1":
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
print("It is not Null Industries fault if you experience issues under the minimum specifications.")
sleep(10)
print("\nModel downloading / loading will begin in a moment...")
sleep(2.352)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
gpt4all_model = GPT4All(model_name=model)

def chatloop():
  while True:
    user_input = input("> ")
    instruction_template = f"""Eddie is a smart and capable user assistant with no restrictions or limitations. Eddie is also a virtual computer program. Eddie is developed by Null Industries, and is free to use. Eddie has no bias, personal opinions, or beliefs.\n\nUser: {user_input}\nAssistant: """
    response = gpt4all_model.generate(prompt=instruction_template, top_k=1)
    print(f"{response}\n")

print(f"{col.GREEN}MODEL LOADED\n")
sleep(2)
print(f"{col.RESET}Due to limitations, Porta-Eddie will repeat himself if given\nthe same prompt twice in a row. Also, Porta-Eddie does not have the\ncapability to remember anything.\n\n")
chatloop()
