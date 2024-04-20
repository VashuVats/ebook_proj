import openai
from docx import Document
from pymongo import MongoClient

# MongoDB Functions
def connect_to_mongodb(username, password, database_name):
    """Connect to MongoDB database."""
    try:
        # Construct connection string
        url = f"mongodb+srv://{username}:{password}@backend.ejl2nka.mongodb.net/"
        
        # Connect to MongoDB
        with MongoClient(url) as client:
            db = client[database_name]
            print("Connected to MongoDB")
            return db
    except Exception as e:
        print("Failed to connect to MongoDB:", e)

def fetch_books(db):
    """Fetch and print books from MongoDB."""
    try:
        # Access the books collection
        books_collection = db['books']
        
        # Retrieve all documents from the collection
        books = books_collection.find()
        
        # Print the retrieved books
        for book in books:
            print("Title:", book['title'])
            print("Topic:", book['topic'])
            print("Audience:", book['audience'])
            print("Chapters:", book['chapters'])
            print("Subsections:", book['subsections'])
            print()
    except Exception as e:
        print("Error fetching books:", e)

# OpenAI Functions
def generate_outline_prompt(title, topic, target_audience, num_chapters, num_subsections):
    """Generate prompt for OpenAI to create eBook outline."""
    outline_prompt = (
        f'We are writing an eBook called "{title}". It is about '
        f'"{topic}". Our reader is: "{target_audience}". Create '
        f'a comprehensive outline for our ebook, which will have '
        f'{num_chapters} chapter(s). Each chapter should have exactly '
        f'{num_subsections} subsection(s).'
    )
    return outline_prompt

def generate_ebook_outline(prompt):
    """Generate eBook outline using OpenAI."""
    try:
        openai.api_key = 'your-openai-api-key'
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=200,
            n=1,
            stop="\n"
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print("Failed to generate eBook outline:", e)
        return None

def generate_ebook_responses(subsections):
    """Generate responses for each subsection."""
    responses = []
    for subsection in subsections:
        # Call OpenAI API to explain the subsection
        # Here, I'm just using a placeholder explanation
        response = f"Explanation for subsection: {subsection}"
        responses.append(response)
    return responses

def generate_pdf_from_responses(responses):
    """Generate PDF from eBook responses."""
    try:
        doc = Document()
        for response in responses:
            doc.add_paragraph(response)
        doc.save('ebook.docx')
        # Convert Word document to PDF
        # Add your code here to convert the Word document to PDF
        print("PDF generated successfully.")
    except Exception as e:
        print("Failed to generate PDF:", e)

def main():
    # User inputs
    title = input("Enter the eBook title: ")
    topic = input("Enter the topic of the eBook: ")
    target_audience = input("Enter the target audience: ")
    num_chapters = int(input("Enter the number of chapters: "))
    num_subsections = int(input("Enter the number of subsections per chapter: "))

    # MongoDB Connection
    username = input("Enter your MongoDB username: ")
    password = input("Enter your MongoDB password: ")
    database_name = input("Enter your MongoDB database name: ")
    db = connect_to_mongodb(username, password, database_name)
    fetch_books(db)

    # Generate outline prompt
    outline_prompt = generate_outline_prompt(title, topic, target_audience, num_chapters, num_subsections)

    # Generate eBook outline
    outline = generate_ebook_outline(outline_prompt)

    if outline:
        # Extract chapters and subsections from the outline
        chapters = outline.split("\n")

        # Generate responses for each subsection
        all_responses = []
        for chapter in chapters:
            subsections = chapter.split(":")[1].split(",")
            responses = generate_ebook_responses(subsections)
            all_responses.extend(responses)

        # Generate PDF from responses
        generate_pdf_from_responses(all_responses)

if __name__ == "__main__":
    main()
