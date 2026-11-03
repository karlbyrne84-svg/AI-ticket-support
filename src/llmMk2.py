from dotenv import load_dotenv
from openai import OpenAI
from models import predict_category, predict_priority

load_dotenv()

client = OpenAI()

def ticket_analysis_2(query):
    response = client.responses.create(
        model="gpt-6-luna",
        instructions="""
        You are a customer support helper and assistant
        you need to analyse the ticket given and provide the following:

        1) a small summary of the problem (start with "Summary:")
        2) the customers sentiment (start with "Sentiment:")
        3) provide a recomendation to the support team on what to do (start with "reccomendation:")

        dont make anything up, and do not assume (for example the refund process), use only the details of the ticket provided

        if the question is off topic, meaning it does not relate to customer service, then just skip part 1 and part 2 and say that it is a irrelevant query and show it,
        I also want you to NOT print the category and priority, if and only if its irrelevant.
        """,
        input=query
    )
    return response.output_text

query = """my mouse wont work when i turn it on, i want a refund ASAP!!"""

def tickey_summary(Q):
    answer = ticket_analysis_2(Q)
    return answer + f"\n category:{predict_category(Q)}, priority:{predict_priority(Q)}"

result = tickey_summary(query)
print(result)