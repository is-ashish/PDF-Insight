def chat_loop(chain):
    print("\n🤖 AI Assistant Ready! Type 'exit' or 'quit' to stop.\n")
    print("=" * 50)
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if not user_input:
                continue
                
            if user_input.lower() in ["exit", "quit", "bye"]:
                print("Assistant: Goodbye! 👋")
                break
            
            response = chain.invoke(user_input)
            print(f"\nAssistant: {response}\n")
            print("-" * 50)
            
        except KeyboardInterrupt:
            print("\n\nAssistant: Session ended. Goodbye! 👋")
            break
            
        except Exception as e:
            print(f"Error: {e}")
            continue