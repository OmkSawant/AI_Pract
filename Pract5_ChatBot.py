# Simple Customer Service Chatbot for Pizza Ordering

def chatbot():
    print("Welcome to PizzaBot! 🍕")
    print("How can I help you today?")
    print("You can ask about: Menu, Order, Delivery, or say Bye to exit.")

    while True:
        user_input = input("You: ").lower()

        if "menu" in user_input:
            print("PizzaBot: We have Margherita, Farmhouse, Peppy Paneer, and Veggie Supreme pizzas!")
        elif "order" in user_input:
            print("PizzaBot: Great! What pizza would you like to order?")
            pizza_choice = input("You: ")
            print(f"PizzaBot: Awesome! Your {pizza_choice} pizza will be ready soon. 🍕")
        elif "delivery" in user_input:
            print("PizzaBot: We deliver within 30 minutes in your area. 🚚")
        elif "bye" in user_input or "exit" in user_input:
            print("PizzaBot: Thank you for visiting! Have a delicious day! 👋")
            break
        else:
            print("PizzaBot: Sorry, I didn't understand that. Please ask about Menu, Order, Delivery, or say Bye.")

if __name__ == "__main__":
    chatbot()


# OUTPUT---->
# Welcome to PizzaBot! 🍕
# How can I help you today?
# You can ask about: Menu, Order, Delivery, or say Bye to exit.
# You: Menu
# PizzaBot: We have Margherita, Farmhouse, Peppy Paneer, and Veggie Supreme pizzas!
# You: Order
# PizzaBot: Great! What pizza would you like to order?
# You: Farmhouse
# PizzaBot: Awesome! Your Farmhouse pizza will be ready soon. 🍕
# You: Delivery
# PizzaBot: We deliver within 30 minutes in your area. 🚚
# You: Bye
# PizzaBot: Thank you for visiting! Have a delicious day! 👋

