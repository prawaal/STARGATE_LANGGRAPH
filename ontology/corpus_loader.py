from pathlib import Path


class CorpusLoader:

    def __init__(self, folder_path):

        self.folder_path = Path(folder_path)

    def load_documents(self):

        documents = []

        for file in self.folder_path.glob("*.txt"):

            with open(file, "r", encoding="utf-8") as f:

                text = f.read()

                documents.append({
                    "source": file.stem,
                    "text": text
                })

        return documents