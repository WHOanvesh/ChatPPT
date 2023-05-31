from transformers import pipeline

def ask_questions(context):
    # Load the question-answering model
    question_answering = pipeline("question-answering")

    while True:
        question = input("Please enter your question (or 'exit' to quit): ")

        if question.lower() == "exit":
            break

        # Use the question-answering model to find the answer
        result = question_answering(question=question, context=context)

        print("Answer:", result["answer"])
        print("Confidence score:", result["score"])
        print()

# Main program
def main():
    paragraph = input("Please enter the paragraph: ")
    ask_questions(paragraph)

if __name__ == "__main__":
    main()
