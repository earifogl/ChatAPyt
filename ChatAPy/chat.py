print ("Welcome aboard!")
name = input("Username:")
print (name, "has joined the chat!")
repeats = int(8)
for i in range(repeats):
  message = input("Say something")
  print("[",name,"]", message)
  if message == "fuck":
    print (name, "has got warning")
  if message == "Hello":
    print ("Hello", name, "this is your assistant.")
    actions = ["Give me a drink", "Give me some", "Do everything for me"]
  if message == actions[0]:
    print ("Here you go")
    drink = "slurp, slurp, slurp"
  if message == "drink":
    print (drink)
    result = "Im glad ya did"
  if message == "I enjoyed it":
    print (result)

