from dotenv import load_dotenv
from ko_generation import Generator
import sys
import os


class NoExistingDBError(Exception):
    pass


def initiate_gen(inputs_dir: str, load_docs: bool, deserialization: bool, db_name: str = None):

    # initiate generator instance
    gen = Generator(inputs_dir, 'knowledge_objects')

    if not load_docs and not db_name:
        raise NoExistingDBError('If not loading docs, must pass an existing vector store.')

    # if the user wants to load input documents
    elif load_docs:

        # load all supported input documents
        gen.read_all(ignore=True)

        # scrape websites in .url file and load them
        gen.read_urls()

        # raise error
        if len(gen.docs) == 0:
            raise ValueError(f"There are no valid input documents in directory {inputs_dir}")

        gen.chunk_docs(chunk_size=1000, overlap=200)

        # if there is an existing db to add to make sure to load it
        if db_name:
            gen.ingest_db(db=db_name, deserialization=deserialization)
        else:
            gen.ingest_db()

        save_name = input('How would you like to save the vector DB as? If not saving, simply press Enter')
        if len(save_name) > 0:
            gen.save_db(save_name)

    else:
        gen.load_db(db_name, allow_deserialization=deserialization)

    return gen


if __name__ == "__main__":
    load_dotenv()

    input_dir = sys.argv[1]

    if not os.path.exists(input_dir):
        os.mkdir(input_dir)

    topics = sys.argv[2].split(",")
    if sys.argv[3].lower() == 'true':
        loading = True
    else:
        loading = False

    if sys.argv[4].lower() == 'true':
        deserialize = True
    else:
        deserialize = False

    if len(sys.argv) == 6:
        existing_db = sys.argv[5]
    else:
        existing_db = None

    if not os.path.exists('template.txt'):
        raise FileNotFoundError(f"The path does not contain template.txt file.")

    generator = initiate_gen(input_dir, load_docs=loading, deserialization=deserialize, db_name=existing_db)

    with open('template.txt', 'r') as t:
        sections = [section.strip() for section in t]
        t.close()

    for topic in topics:
        results = []
        for section in sections:
            template = ("You are an expert in {topic}, and you are writing the section " + f"'{section}'" +
                        " of a website on this subject. Based on the following context: {context} "
                        "\nWrite the provided section in markdown format. Include the section title as header 2")

            results.append(generator.create_ko(template, topic))

        output_path = os.path.join(generator.output_dir, f"{topic}.md")
        result = '\n\n'.join(results)
        with open(output_path, 'w', encoding='utf-8') as out_file:
            out_file.write(result)
