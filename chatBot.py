import google.generativeai as ai;
myKey="AIzaSyADf20vfZhtKPPjtexy4gpK3CqbSfpcuVM";
ai.configure(api_key=myKey);
model=ai.GenerativeModel("gemini-1.5-pro");
chat=model.start_chat();
while True:
    msg=input("User: ");
    if(msg=="exit"):
     break;
    result=chat.send_message(msg);
    print("chatBot: "+result.text);